from typing import Optional, Any

from jarbin_toolkit_action.action import Action
from jarbin_toolkit_action.enums import ActionStatus
from jarbin_toolkit_action.time import ActionTimer


class ActionBatch:
    """
        Action list runner with configurable keyword arguments.

        Attributes
        ----------
        status : ActionStatus
            Status of the action  after execution.

        duration : float
            Duration of the action after execution.
    """


    status: ActionStatus
    duration: Optional[float]


    def __init__(
            self,
            *args: Action | ActionBatch,
        ) -> None:
        """
            Initialize an ActionBatch

            Parameters
            ----------
            *args : Action | ActionBatch
                Actions the ActionBatch will contain.

            Raises
            ----------
            ActionTypeError
                Invalid argument type
        """
        ...

    def __call__(
            self,
        ) -> None:
        """
            Execute the actions (if not async, otherwise prepare threads).

            Raises
            ----------
            ActionExecutionError
                Action already pending, running or paused
        """
        ...


    def __add__(
            self,
            other: Action | ActionBatch,
        ) -> ActionBatch:
        """
            Combine Actions together

            Parameters
            ----------
            other : Action | ActionBatch
                Other action(s) to combine with the current ones

            Returns
            ----------
            ActionBatch
                Combination of self with other

            Raises
            ----------
            ActionTypeError
                Invalid argument type
        """
        ...


    def __iadd__(
            self,
            other: Action | ActionBatch,
        ) -> None:
        """
            Combine Actions together

            Parameters
            ----------
            other : Action | ActionBatch
                Other action(s) to combine with the current ones

            Raises
            ----------
            ActionTypeError
                Invalid argument type
        """
        ...


    def __repr__(
            self,
        ) -> str:
        """
            Return a string representation of the ActionBatch.

            Returns
            -------
            str
                String representation of the ActionBatch.
        """
        ...


    def set_settings(
            self,
            *,
            max_worker: Optional[int] = None,
            time_out: Optional[float] = None,
        ) -> None:
        """
            Set/override global action's settings

            Parameters
            ----------
            max_worker : Optional[int]
                Set maximum workers (how many threads running at the same time).

            time_out: Optional[float]
                Time out before canceling actions

            Raises
            ----------
            ActionArgumentError
                Invalid setting.
                Invalid value.
        """
        ...


    def set_actions_settings(
            self,
            *,
            catch: Optional[bool] = None,
            asynchronous: Optional[bool] = None,
        ) -> None:
        """
            Set/override all action's settings

            Parameters
            ----------
            catch : Optional[bool]
                Catch exceptions at action call.

            asynchronous: Optional[bool]
                Execute the action asynchronous (if True, run in thread)

            Raises
            ----------
            ActionArgumentError
                Invalid setting.
                Invalid value.
        """
        ...


    def run(
            self,
        ) -> None:
        """
            Launch all pending asynchronous Actions (requires `ActionBatch()` in order to set every async Actions to pending)

            Raises
            ----------
            ActionExecutionError
                No pending async execution.
        """
        ...


    _actions: list[Action]
    _status: ActionStatus
    _previous_status: Optional[ActionStatus]
    _timer: ActionTimer
    _actions_settings: dict[str, Any]
    _settings: dict[str, Any]


    def _save_status(
            self,
        ) -> None:
        ...


    def _prepare_execution(
            self,
        ) -> None:
        ...


__all__ = [
    'ActionBatch',
]
