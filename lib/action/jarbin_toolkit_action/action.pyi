from typing import Any, overload, Callable, Optional

from jarbin_toolkit_action.enums import ActionStatus


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

        Methods
        ----------
        Action(name: str, function: Callable[..., Any], **kwargs: Any) -> None
            Initialize an Action with an explicit name.

        Action(function: Callable[..., Any], **kwargs: Any) -> None
            Initialize an Action using the function's name.
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
            ActionValueError
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
            ActionValueError
                Invalid positional arguments.
                Invalid keyword arguments (for the given function).
        """
        ...


    def __call__(
            self,
            **kwargs: Any,
        ) -> Any:
        """
            Execute the action with optional overriding keyword arguments.

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
            ActionValueError
                Invalid keyword arguments (for the given function).

            ActionExecutionError
                Caught exception during action execution (if `catch` setting disabled)
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


    def set_setting(
            self,
            *,
            catch: Optional[bool] = None
        ) -> None:
        """
            Set/override action's settings

            Parameters
            ----------
            catch : Optional[bool]
                Catch exceptions at action call.

            Raises
            ----------
            ActionArgumentError
                Invalid setting.
        """
        ...


__all__: list[str]
