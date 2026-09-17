# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : test_action.py
#
# Author       : Jarjarbin06
# ============================================================================


import time

import pytest

from jarbin_toolkit_action.action import Action
from jarbin_toolkit_action.enums import (
    ActionStatus,
    ActionAsync,
)
from jarbin_toolkit_action.error import (
    ActionArgumentError,
    ActionExecutionError,
    ActionThreadError,
    ActionValueError,
)


def test_action_valid_construction() -> None:
    def sample(x, y):
        return x + y

    act = Action("sum", sample, x=3, y=4)

    assert act.name == "sum"
    assert act._function is sample
    assert act._kwargs == {"x": 3, "y": 4}


def test_action_automatic_name() -> None:
    def sample():
        return None

    act = Action(sample)

    assert act.name == "Action(sample)"


def test_action_repr() -> None:
    def sample(x, y):
        return x + y

    act = Action("sum", sample, x=3, y=4)

    assert repr(act) == (
        "<Action: sum: sample(x=3, y=4)>"
    )


def test_action_execution() -> None:
    def mul(x: int, y: int) -> int:
        return x * y

    act = Action("multiply", mul, x=3, y=5)

    result = act()

    assert result == 15
    assert act.output == 15
    assert act.status == ActionStatus.SUCCESS
    assert act.error is None
    assert act.duration is not None


def test_action_is_synchronous_by_default() -> None:
    calls = []

    def sample():
        calls.append("executed")
        return 42

    act = Action(sample)

    result = act()

    assert result == 42
    assert calls == ["executed"]
    assert act.status == ActionStatus.SUCCESS


def test_action_call_kwargs_override_defaults() -> None:
    def sample(value):
        return value

    act = Action(sample, value=10)

    assert act() == 10
    assert act(value=42) == 42
    assert act._kwargs == {"value": 10}


def test_action_invalid_kwargs() -> None:
    def sample(x):
        return x

    act = Action(sample, x=1)

    with pytest.raises(ActionValueError):
        act(invalid=2)


def test_action_invalid_execution_kwargs() -> None:
    def sample(x=1):
        return x

    act = Action(sample)

    with pytest.raises(ActionValueError):
        act(invalid=42)


def test_action_caught_execution_error() -> None:
    def fail():
        raise ValueError("failure")

    act = Action(fail)

    with pytest.raises(ActionExecutionError):
        act()

    assert act.status == ActionStatus.FAILED
    assert isinstance(act.error, ValueError)


def test_action_catch_setting() -> None:
    def fail():
        raise ValueError("failure")

    act = Action(fail)
    act.set_settings(catch=True)

    result = act()

    assert result is None
    assert act.status == ActionStatus.FAILED
    assert isinstance(act.error, ValueError)


def test_action_invalid_setting() -> None:
    act = Action(lambda: None)

    with pytest.raises(ActionArgumentError):
        act.set_settings(invalid=True)


def test_action_async_call_is_pending() -> None:
    act = Action(lambda: 42)
    act.set_settings(asynchronous=True)

    result = act()

    assert result == ActionAsync.SUCCESS
    assert act.status == ActionStatus.PENDING
    assert act.output is None


def test_action_async_start() -> None:
    act = Action(lambda: 42)
    act.set_settings(asynchronous=True)

    act()

    assert act.status == ActionStatus.PENDING

    act.start()
    act._thread.join()

    assert act.status == ActionStatus.SUCCESS
    assert act.output == 42
    assert act.error is None
    assert act.duration is not None


def test_action_async_lifecycle() -> None:
    steps = []

    def sample():
        steps.append(1)
        Action.pause_point()
        steps.append(2)
        return "done"

    act = Action(sample, )
    act.set_settings(asynchronous=True)

    result = act()

    assert result == ActionAsync.SUCCESS
    assert act.status == ActionStatus.PENDING

    act.start()

    while act.status == ActionStatus.PENDING:
        time.sleep(0.001)

    assert act.status == ActionStatus.SUCCESS
    assert steps == [1, 2]
    assert act.output == "done"


def test_action_pause_and_resume() -> None:
    from threading import Event

    entered = Event()
    release = Event()
    steps = []

    def sample():
        steps.append(1)
        entered.set()

        release.wait()
        Action.pause_point()

        steps.append(2)
        Action.pause_point()

        steps.append(3)

        return "done"

    act = Action(sample)
    act.set_settings(asynchronous=True)

    act()
    act.start()

    assert entered.wait(timeout=1)

    act.pause()

    assert act.status == ActionStatus.PAUSED

    release.set()
    time.sleep(0.05)

    assert steps == [1]

    act.resume()
    act._thread.join()

    assert act.status == ActionStatus.SUCCESS
    assert steps == [1, 2, 3]
    assert act.output == "done"


def test_action_cancel() -> None:
    steps = []

    def sample():
        while True:
            Action.pause_point()
            steps.append(1)
            time.sleep(0.01)

    act = Action(sample)
    act.set_settings(asynchronous=True)

    act()
    act.start()

    while not steps:
        time.sleep(0.001)

    act.cancel()

    act._thread.join()

    assert act.status == ActionStatus.CANCELLED
    assert act.output is None
    assert act.error is None


def test_action_pending_cancel() -> None:
    act = Action(lambda: 42)
    act.set_settings(asynchronous=True)

    act()

    assert act.status == ActionStatus.PENDING

    act.cancel()

    assert act.status == ActionStatus.CANCELLED
    assert act.output is None


def test_action_cannot_start_without_async_call() -> None:
    act = Action(lambda: 42)

    with pytest.raises(ActionThreadError):
        act.start()


def test_action_cannot_start_twice() -> None:
    act = Action(lambda: time.sleep(0.1))
    act.set_settings(asynchronous=True)

    act()
    act.start()

    with pytest.raises(ActionThreadError):
        act.start()

    act._thread.join()


def test_action_cannot_execute_while_running() -> None:
    act = Action(lambda: time.sleep(0.1))
    act.set_settings(asynchronous=True)

    act()
    act.start()

    while act.status == ActionStatus.PENDING:
        time.sleep(0.001)

    with pytest.raises(ActionExecutionError):
        act()

    act._thread.join()


def test_action_can_switch_from_async_to_sync() -> None:
    act = Action(lambda: 42)

    act.set_settings(asynchronous=True)

    act()
    act.start()
    act._thread.join()

    assert act.status == ActionStatus.SUCCESS
    assert act.output == 42

    act.set_settings(asynchronous=False)

    result = act()

    assert result == 42
    assert act.status == ActionStatus.SUCCESS
    assert act.output == 42


def test_action_can_switch_from_sync_to_async() -> None:
    act = Action(lambda: 42)

    result = act()

    assert result == 42
    assert act.status == ActionStatus.SUCCESS

    act.set_settings(asynchronous=True)

    result = act()

    assert result == ActionAsync.SUCCESS
    assert act.status == ActionStatus.PENDING

    act.start()
    act._thread.join()

    assert act.status == ActionStatus.SUCCESS
    assert act.output == 42
