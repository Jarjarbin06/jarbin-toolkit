from typing import Any, overload, Callable, Optional


class Action:
    """
        Represent a deferred callable execution with configurable keyword arguments.

        Attributes
        ----------
        name : str
            Name of the action.
        output : Any
            Output of the action after execution.

        Methods
        ----------
        Action(name: str, function: Callable[..., Any], **kwargs: Any) -> None
            Initialize an Action with an explicit name.
        Action(function: Callable[..., Any], **kwargs: Any) -> None
            Initialize an Action using the function's name.
    """


    name: str
    output: Optional[Any]


    @overload
    def __init__(
            self,
            name: str,
            function: Callable[..., Any],
            **kwargs: Any
        ) -> None:
        """
            Initialize an Action with an explicit name.

            Parameters
            ----------
            name : str
                Name of the action.
            function : Callable[..., Any]
                Function executed by the action.
            **kwargs : Any
                Keyword arguments passed to the function.
        """
        ...


    @overload
    def __init__(
            self,
            function: Callable[..., Any],
            **kwargs: Any
        ) -> None:
        """
            Initialize an Action using the function's name.

            Parameters
            ----------
            function : Callable[..., Any]
                Function executed by the action.
            **kwargs : Any
                Keyword arguments passed to the function.
        """
        ...


    def __call__(
            self,
            **kwargs: Any
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
        """
        ...


    def __repr__(
            self
        ) -> str:
        """
            Return a string representation of the Action.

            Returns
            -------
            str
                String representation of the Action.
        """
        ...


__all__: list[str]
