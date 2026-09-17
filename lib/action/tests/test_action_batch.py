# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : test_action_batch.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

import time

from jarbin_toolkit_action import (
    Action,
    ActionBatch,
    ActionArgumentError,
    ActionThreadError,
    ActionTypeError,
    ActionExecutionError,
)
from jarbin_toolkit_action import _Enums


def test_action_batch_init() -> None:
    action_1 = Action(lambda: 1)
    action_2 = Action(lambda: 2)

    batch = ActionBatch(action_1, action_2)

    assert batch._actions == [action_1, action_2]
    assert batch.status is None
    assert batch.duration is None
    assert batch._actions_settings == {
        "asynchronous": None,
    }
    assert batch._settings == {
        "max_worker": 2,
        "time_out": None,
    }


def test_action_batch_empty() -> None:
    batch = ActionBatch()

    assert batch._actions == []
    assert batch._settings["max_worker"] is None
    assert batch.status is None


def test_action_batch_invalid_action() -> None:
    with pytest.raises(ActionTypeError):
        ActionBatch(Action(lambda: 1), "invalid")


def test_action_batch_repr() -> None:
    action_1 = Action("first", lambda: 1)
    action_2 = Action("second", lambda: 2)

    batch = ActionBatch(action_1, action_2)

    assert repr(batch) == (
        f"<ActionBatch: {action_1!r}, {action_2!r}>"
    )


def test_action_batch_set_settings() -> None:
    batch = ActionBatch(Action(lambda: 1), Action(lambda: 2))

    batch.set_settings(
        max_worker=1,
        time_out=5,
    )

    assert batch._settings["max_worker"] == 1
    assert batch._settings["time_out"] == 5


def test_action_batch_set_settings_partial() -> None:
    batch = ActionBatch(Action(lambda: 1), Action(lambda: 2))

    batch.set_settings(max_worker=1)

    assert batch._settings["max_worker"] == 1
    assert batch._settings["time_out"] is None


def test_action_batch_invalid_setting() -> None:
    batch = ActionBatch(Action(lambda: 1))

    with pytest.raises(ActionArgumentError):
        batch.set_settings(invalid=True)


def test_action_batch_set_actions_settings() -> None:
    action_1 = Action(lambda: 1)
    action_2 = Action(lambda: 2)

    batch = ActionBatch(action_1, action_2)

    batch.set_actions_settings(asynchronous=True)

    assert action_1._settings["asynchronous"] is True
    assert action_2._settings["asynchronous"] is True


def test_action_batch_set_actions_settings_overrides_defaults() -> None:
    action_1 = Action(lambda: 1)
    action_2 = Action(lambda: 2)

    action_1.set_settings(asynchronous=False)
    action_2.set_settings(asynchronous=False)

    batch = ActionBatch(action_1, action_2)

    batch.set_actions_settings(asynchronous=True)

    assert action_1._settings["asynchronous"] is True
    assert action_2._settings["asynchronous"] is True


def test_action_batch_call() -> None:
    results = []

    def first():
        results.append(1)

    def second():
        results.append(2)

    batch = ActionBatch(
        Action(first),
        Action(second),
    )

    batch()

    assert batch.status == _Enums.ActionStatus.PENDING
    assert results == [1, 2]


def test_action_batch_call_prepares_async_actions() -> None:
    results = []

    def first():
        results.append(1)

    def second():
        results.append(2)

    action_1 = Action(first)
    action_2 = Action(second)

    batch = ActionBatch(action_1, action_2)
    batch.set_actions_settings(asynchronous=True)

    batch()

    assert batch.status == _Enums.ActionStatus.PENDING
    assert action_1.status == _Enums.ActionStatus.PENDING
    assert action_2.status == _Enums.ActionStatus.PENDING
    assert results == []


def test_action_batch_cannot_call_while_pending() -> None:
    batch = ActionBatch(Action(lambda: None))

    batch()

    with pytest.raises(ActionExecutionError):
        batch()


def test_action_batch_run_requires_pending() -> None:
    batch = ActionBatch(Action(lambda: None))

    with pytest.raises(ActionExecutionError):
        batch.run()


def test_action_batch_run_synchronous() -> None:
    results = []

    def first():
        results.append(1)
        return "first"

    def second():
        results.append(2)
        return "second"

    batch = ActionBatch(
        Action(first),
        Action(second),
    )

    batch()

    assert results == [1, 2]

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert results == [1, 2]


def test_action_batch_run_asynchronous() -> None:
    results = []

    def first():
        results.append(1)
        time.sleep(0.02)

    def second():
        results.append(2)
        time.sleep(0.02)

    action_1 = Action(first)
    action_2 = Action(second)

    batch = ActionBatch(action_1, action_2)
    batch.set_actions_settings(asynchronous=True)

    batch()

    assert action_1.status == _Enums.ActionStatus.PENDING
    assert action_2.status == _Enums.ActionStatus.PENDING
    assert results == []

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert action_1.status == _Enums.ActionStatus.SUCCESS
    assert action_2.status == _Enums.ActionStatus.SUCCESS
    assert sorted(results) == [1, 2]


def test_action_batch_max_worker() -> None:
    running = 0
    max_running = 0

    def sample():
        nonlocal running, max_running

        running += 1
        max_running = max(max_running, running)

        time.sleep(0.05)

        running -= 1

    actions = [
        Action(sample)
        for _ in range(4)
    ]

    batch = ActionBatch(*actions)

    batch.set_settings(max_worker=2)
    batch.set_actions_settings(asynchronous=True)

    batch()

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert max_running <= 2
    assert all(
        action.status == _Enums.ActionStatus.SUCCESS
        for action in actions
    )


def test_action_batch_max_worker_one() -> None:
    execution_order = []

    def first():
        execution_order.append(1)
        time.sleep(0.02)

    def second():
        execution_order.append(2)
        time.sleep(0.02)

    action_1 = Action(first)
    action_2 = Action(second)

    batch = ActionBatch(action_1, action_2)

    batch.set_settings(max_worker=1)
    batch.set_actions_settings(asynchronous=True)

    batch()

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert execution_order == [1, 2]


def test_action_batch_timeout() -> None:
    def slow():
        time.sleep(1)

    action = Action(slow)

    batch = ActionBatch(action)

    batch.set_settings(time_out=0.01)
    batch.set_actions_settings(asynchronous=True)

    batch()

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert action.status == _Enums.ActionStatus.CANCELLED


def test_action_batch_timeout_does_not_cancel_fast_action() -> None:
    def fast():
        time.sleep(0.01)

    action = Action(fast)

    batch = ActionBatch(action)

    batch.set_settings(time_out=1)
    batch.set_actions_settings(asynchronous=True)

    batch()

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert action.status == _Enums.ActionStatus.SUCCESS


def test_action_batch_timeout_only_applies_after_start() -> None:
    execution_order = []

    def sample():
        execution_order.append(1)
        time.sleep(0.02)

    actions = [
        Action(sample),
        Action(sample),
    ]

    batch = ActionBatch(*actions)

    batch.set_settings(
        max_worker=1,
        time_out=0.1,
    )
    batch.set_actions_settings(asynchronous=True)

    batch()

    batch.run()

    assert batch.status == _Enums.ActionStatus.SUCCESS
    assert execution_order == [1, 1]
    assert all(
        action.status == _Enums.ActionStatus.SUCCESS
        for action in actions
    )


def test_action_batch_duration() -> None:
    action = Action(lambda: time.sleep(0.01))

    batch = ActionBatch(action)

    batch()

    assert batch.duration is None

    batch.run()

    assert batch.duration is not None
    assert batch.duration >= 0


def test_action_batch_status_after_run() -> None:
    batch = ActionBatch(
        Action(lambda: None),
        Action(lambda: None),
    )

    batch()

    assert batch._status == _Enums.ActionStatus.PENDING
    assert batch.status == _Enums.ActionStatus.PENDING

    batch.run()

    assert batch._status == _Enums.ActionStatus.INACTIVE
    assert batch._previous_status == _Enums.ActionStatus.SUCCESS
    assert batch.status == _Enums.ActionStatus.SUCCESS


def test_action_batch_multiple_runs() -> None:
    counter = 0

    def sample():
        nonlocal counter
        counter += 1

    action = Action(sample)
    batch = ActionBatch(action)

    batch()
    batch.run()

    batch()
    batch.run()

    assert counter == 2
    assert batch.status == _Enums.ActionStatus.SUCCESS
