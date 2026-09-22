from inspect import Signature
from typing import (
    Any,
    overload,
    Callable,
    Optional,
)
from threading import (
    Event,
    Lock,
    Thread,
)

from jarbin_toolkit_action.enums import (
    ActionStatus,
    ActionAsync,
)
from jarbin_toolkit_action.time import ActionTimer


class Action:
    """
        Represent a deferred callable execution with configurable keyword arguments.

        Attributes
        ----------
        name : str
            Name of the action.

        output : Any
            Output of the action after execution.

        status : ActionStatus
            Status of the action  after execution.

        error : Exception
            Caught error during execution.

        duration : float
            Duration of the action after execution.
    """


    name: str
    output: Optional[Any]
    status: ActionStatus
    error: Optional[Exception]
    duration: Optional[float]


    @overload
    def __init__(
            self,
            name: str,
            function: Callable[..., Any],
            **kwargs: Any,
        ) -> None:
        """
            Initialize an Action with an explicit name.

            Settings:
                `catch` = False.

            Parameters
            ----------
            name : str
                Name of the action.

            function : Callable[..., Any]
                Function executed by the action.

            **kwargs : Any
                Keyword arguments passed to the function.

            Raises
            ----------
            ActionValueJError
                Invalid positional arguments.
                Invalid keyword arguments (for the given function).
        """
        ...


    @overload
    def __init__(
            self,
            function: Callable[..., Any],
            **kwargs: Any,
        ) -> None:
        """
            Initialize an Action using the function's name.

            Parameters
            ----------
            function : Callable[..., Any]
                Function executed by the action.

            **kwargs : Any
                Keyword arguments passed to the function.

            Raises
            ----------
            ActionValueJError
                Invalid positional arguments.
                Invalid keyword arguments (for the given function).
        """
        ...


    def __call__(
            self,
            **kwargs: Any,
        ) -> Any | ActionAsync:
        """
            Execute the action (if not async, otherwise prepare thread) with optional overriding keyword arguments.

            Parameters
            ----------
            **kwargs : Any
                Keyword arguments passed to the function.

            Returns
            -------
            Any
                Output of the action after execution.

            Raises
            ----------
            ActionValueJError
                Invalid keyword arguments (for the given function).

            ActionExecutionError
                Caught exception during action execution (if `catch` setting disabled).
                Action already pending, running or paused
        """
        ...


    def __repr__(
            self,
        ) -> str:
        """
            Return a string representation of the Action.

            Returns
            -------
            str
                String representation of the Action.
        """
        ...


    def set_settings(
            self,
            *,
            catch: Optional[bool] = None,
            asynchronous: Optional[bool] = None,
        ) -> None:
        """
            Set/override action's settings

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
        """
        ...


    def start(
            self,
        ) -> None:
        """
            Start the thread

            Raises
            ----------
            ActionThreadError
                No pending async execution.
                Action not pending.
                Thread already running.
        """
        ...


    def pause(
            self,
        ):
        """
            Pause the thread

            Raises
            ----------
            ActionThreadError
                Action not running.
        """
        ...


    def resume(
            self,
        ):
        """
            Resume the thread

            Raises
            ----------
            ActionThreadError
                Action not paused.
        """
        ...


    def cancel(
            self,
        ):
        """
            Cancel the thread

            Raises
            ----------
            ActionThreadError
                Action not pending, running nor paused.
        """
        ...


    @staticmethod
    def pause_point(
        ) -> None:
        """
            Put a checkpoint for action threading (listen for pause event)
        """


    _thread_actions: dict[int, Any]
    _thread_actions_lock: Lock
    _function: Callable[[...], Any]
    _signature: Signature
    _output: Optional[Any]
    _kwargs: dict[str, Any]
    _execution_kwargs: dict[str, Any]
    _status: ActionStatus | int
    _previous_status: Optional[ActionStatus | int]
    _error: Optional[Exception]
    _timer: ActionTimer
    _settings: dict[str, Any]
    _thread: Optional[Thread]
    _pause_event: Event
    _cancel_event: Event
    _execution_lock: Lock


    def _validate_kwargs(
            self,
            kwargs: dict[str, Any],
        ) -> dict[str, Any]:
        ...


    def _save_status(
            self,
        ):
        ...


    def _prepare_execution(
            self,
            kwargs: dict[str, Any],
        ):
        ...


    def _execute_synchronous(
            self,
        ):
        ...


    def _execute_asynchronous(
            self,
        ) -> ActionAsync:
        ...


    def _thread_execution(
            self,
        ) -> None:
        ...


    def _kill_thread(
            self,
        ):
        ...


    @staticmethod
    def _get_current_action(
        ) -> Any:
        ...


__all__: list[str]
