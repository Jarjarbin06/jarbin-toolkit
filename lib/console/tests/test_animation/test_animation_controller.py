# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : test_animation_controller.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.animation import (
    Animation,
    AnimationController,
    AnimationMode,
    AnimationState,
)
from jarbin_toolkit_console import ConsoleJError


class Clock:


    def __init__(
            self,
            value=0.0,
        ):

        self.value = value


    def tick(
            self,
        ):

        return self.value


    def advance(
            self,
            value,
        ):

        self.value += value



@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def animation():
    return Animation(
        ["A", "B", "C"],
        duration=0.1,
        mode=AnimationMode.ONCE,
    )


@pytest.fixture
def controller(animation, clock):
    return AnimationController(
        animation,
        clock=clock.tick,
    )


def test_controller_basic(controller, animation):
    assert controller.animation is animation
    assert controller.state == AnimationState.READY
    assert controller.running is False
    assert controller.paused is False
    assert controller.stopped is False
    assert controller.finished is False
    assert controller.elapsed == 0.0


def test_controller_start(controller, clock):
    controller.start()

    assert controller.state == AnimationState.RUNNING
    assert controller.running is True

    clock.advance(0.5)

    assert controller.elapsed == 0.5


def test_controller_pause(controller, clock):
    controller.start()

    clock.advance(0.25)
    controller.pause()

    assert controller.state == AnimationState.PAUSED
    assert controller.paused is True
    assert controller.elapsed == 0.25

    clock.advance(1.0)

    assert controller.elapsed == 0.25


def test_controller_resume(controller, clock):
    controller.start()

    clock.advance(0.25)
    controller.pause()

    clock.advance(1.0)
    controller.resume()

    assert controller.state == AnimationState.RUNNING

    clock.advance(0.25)

    assert controller.elapsed == 0.5


def test_controller_stop(controller, clock):
    controller.start()

    clock.advance(0.25)
    controller.stop()

    assert controller.state == AnimationState.STOPPED
    assert controller.stopped is True
    assert controller.elapsed == 0.25


def test_controller_reset(controller, clock):
    controller.start()

    clock.advance(0.25)
    controller.stop()

    controller.reset()

    assert controller.state == AnimationState.READY
    assert controller.elapsed == 0.0
    assert controller.animation.frame == 0


def test_controller_update(controller, clock):
    controller.start()

    clock.advance(0.1)

    frame = controller.update()

    assert str(frame) == "B"
    assert controller.animation.frame == 1


def test_controller_tick(controller, clock):
    controller.start()

    clock.advance(0.1)

    assert controller.tick() is True

    clock.advance(0.01)

    assert controller.tick() is False


def test_controller_completion(controller, clock):
    controller.start()

    clock.advance(0.1)
    controller.update()

    assert controller.state == AnimationState.RUNNING

    clock.advance(0.1)
    controller.update()

    assert controller.state == AnimationState.RUNNING

    clock.advance(0.1)
    controller.update()

    assert controller.state == AnimationState.FINISHED
    assert controller.finished is True
    assert controller.animation.finished is True


def test_controller_start_finished_animation_resets(
        controller,
        clock,
    ):

    controller.start()

    clock.advance(1.0)
    controller.update()

    assert controller.finished is True

    controller.start()

    assert controller.running is True
    assert controller.animation.frame == 0


def test_controller_update_when_not_running(
        controller,
        clock,
    ):

    assert str(controller.update()) == "A"

    clock.advance(1.0)

    assert str(controller.update()) == "A"


def test_controller_pause_when_not_running(controller):
    controller.pause()

    assert controller.state == AnimationState.READY


def test_controller_resume_when_not_paused(controller):
    controller.resume()

    assert controller.state == AnimationState.READY


def test_controller_stop_when_not_running(controller):
    controller.stop()

    assert controller.state == AnimationState.STOPPED


def test_controller_context_manager(controller):
    with controller as active:
        assert active is controller
        assert controller.running is True

    assert controller.stopped is True


def test_controller_context_manager_on_exception(controller):
    with pytest.raises(ConsoleJError):
        with controller:
            raise ConsoleJError("failure")

    assert controller.stopped is True


def test_controller_invalid_animation():
    with pytest.raises(
        ConsoleJError,
        match="Animation must be an Animation",
    ):
        AnimationController("animation")


def test_controller_invalid_clock():
    animation = Animation(["A"])

    with pytest.raises(
        ConsoleJError,
        match="Clock must be callable",
    ):
        AnimationController(
            animation,
            clock=None,
        )


@pytest.mark.parametrize(
    "elapsed",
    [
        -1,
        -0.1,
    ],
)
def test_controller_negative_elapsed(controller, elapsed):
    controller.start()

    with pytest.raises(
        ConsoleJError,
        match="Elapsed time must be non-negative",
    ):
        controller.update(elapsed)
