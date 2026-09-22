# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : action_batch.py
# Class        : ActionBatch
#
# Author       : Jarjarbin06
# ============================================================================


from time import monotonic

from jarbin_toolkit_action.action import Action
from jarbin_toolkit_action.errors import (
    ActionTypeJError,
    ActionArgumentJError,
    ActionThreadJError,
    ActionExecutionJError,
)
from jarbin_toolkit_action.enums import ActionStatus
from jarbin_toolkit_action.time import ActionTimer


class ActionBatch:


    def _save_status(
            self,
        ):
        self._previous_status = self._status
        self._status = ActionStatus.INACTIVE


    def _prepare_execution(
            self,
        ):
        self._timer.reset()
        self._status = ActionStatus.PENDING


    def __init__(
            self,
            *args,
        ):

        self._actions = []

        for arg in args:
            if isinstance(arg, Action):
                self._actions.append(arg)
            elif isinstance(arg, ActionBatch):
                self._actions += arg._actions
            else:
                raise ActionTypeJError(
                    "\nArguments must all be of type Action"
                )

        self._status = ActionStatus.INACTIVE
        self._previous_status = None
        self._timer = ActionTimer()
        self._actions_settings = {
            "asynchronous": None,
        }
        self._settings = {
            "max_worker": len(self._actions) or None,
            "time_out": None,
        }


    def __call__(
            self,
        ):

        if self._status in (
                ActionStatus.PENDING,
                ActionStatus.RUNNING,
                ActionStatus.PAUSED,
            ):
            raise ActionExecutionJError(
                f"\nCannot execute ActionBatch from status {self.status}"
            )

        self._prepare_execution()

        for action in self._actions:
            action()


    def __add__(
            self,
            other,
        ):

        if isinstance(other, Action | ActionBatch):
            return ActionBatch(self, other)

        raise ActionTypeJError(
            f"\n{type(other)} cannot be added with {type(self)}"
        )


    def __iadd__(
            self,
            other,
        ):

        if isinstance(other, ActionBatch):
            self._actions += other._action

        elif isinstance(other, Action):
            self._actions.append(other)

        raise ActionTypeJError(
            f"\n{type(other)} cannot be added to {type(self)}"
        )


    def __repr__(
            self,
        ):

        return f"<ActionBatch: {', '.join(f'{action!r}' for action in self._actions)}>"


    def set_settings(
            self,
            **kwargs,
        ):

        for key, value in kwargs.items():

            if key not in self._settings:
                raise ActionArgumentJError(
                    f"\nInvalid setting: {key}={value}"
                )

            if (
                (key == "max_worker" and value <= 0)
                or
                (key == "time_out" and value is not None and value < 0)
            ):
                raise ActionArgumentJError(
                    f"\nInvalid setting's value: {key}={value}"
                )

            self._settings[key] = value


    def set_actions_settings(
            self,
            **kwargs,
        ):

        for action in self._actions:
            action.set_settings(**kwargs)

    def run(
            self,
        ):

        if self._status != ActionStatus.PENDING:
            raise ActionExecutionJError(
                f"\nCannot start ActionBatch from status {self.status}"
            )

        self._status = ActionStatus.RUNNING
        self._timer.start()

        pending = []
        running = {}

        try:

            if self._settings["max_worker"]:

                for action in self._actions:
                    if action.status == ActionStatus.PENDING:
                        pending.append(action)

                while pending or running:

                    while (
                            pending and
                            len(running) < self._settings["max_worker"]
                    ):
                        action = pending.pop(0)

                        action.start()

                        running[action] = monotonic()

                    for action, start_time in list(running.items()):

                        if action.status not in (
                                ActionStatus.PENDING,
                                ActionStatus.RUNNING,
                        ):
                            running.pop(action)
                            continue

                        time_out = self._settings["time_out"]

                        if (
                                time_out is not None and
                                monotonic() - start_time >= time_out
                        ):
                            action.cancel()

            self._status = ActionStatus.SUCCESS

        finally:
            self._timer.stop()
            self._save_status()


    @property
    def status(
            self,
        ):

        return (
            self._previous_status
            if self._status == ActionStatus.INACTIVE else
            self._status
        )


    @property
    def duration(
            self,
        ):

        return self._timer.elapsed() if self._previous_status is not None else None


__all__ = [
    'ActionBatch',
]
