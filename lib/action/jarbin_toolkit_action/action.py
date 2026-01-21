#############################
###                       ###
###    Epitech Console    ###
###   ----action.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Action:
    """
        Action class.

        Action object to save a function and its arguments and call it later.
    """


    from collections.abc import Callable


    def __init__(
            self,
            name : str,
            function : Callable,
            *args : Any,
            **kwargs : Any
        ) -> None:
        """
            Save a function and its arguments.

            Parameters:
                name (str): Name of the call.
                function (Callable): Function to be saved.
                *args (Any, optional): Function's args.
                **kwargs (Any, optional): Function's kwargs.
        """

        from collections.abc import Callable

        self.name = name
        self.function : Callable = function
        self.args : list = list(args)
        self.kwargs : dict = dict(kwargs)


    def __str__(
            self
        ) -> str:
        """
            Return the string representation of the Action object.
        """

        return f"\'{self.name}\' : {self.function.__name__}(*args = {self.args}, **kwargs = {self.kwargs})"


    def __add__(
            self,
            other
        ) -> Any:
        """
            Create Actions object with the 2 given actions.

            Parameters:
                other (Action): Action to add.
        """

        return Actions([self, other])


    def __call__(
            self
        ) -> Any:
        """
            Call the saved function with its arguments.

        Returns:
            Any: Return of the function's call.
        """

        return self.function(*self.args, **self.kwargs)


    def __repr__(
            self
        ) -> str:
        """
            Convert Action object to string.

            Returns:
                str: Action string
        """

        return f"Action(\'{self.name}\', function={self.function.__name__}, args={repr(self.args)}, kwargs={repr(self.kwargs)})"


class Actions:
    """
        Actions class.

        List of action to save.
    """


    def __init__(
            self,
            actions : list[Action] | Action | None = None,
        ) -> None:
        """
            Save a list of actions.

            Parameters:
                actions (list[Action] | Action | None, optional): list of actions to save.
        """

        self.actions : list[Action] = []

        if type(actions) in [list]:
            for action in actions:
                self.actions.append(action)

        elif type(actions) in [Action]:
            self.actions = [actions]


    def __str__(
            self
        ) -> str:
        """
            Return the string representation of the Actions object.

            Returns:
                str: String representation of the Actions object.
        """

        string : str = ""

        for idx in range(len(self.actions)):
            string += f"{idx + 1} :\n"
            string += f"    name = \'{self.actions[idx].name}\'\n"
            string += f"    function = {self.actions[idx].function.__name__}\n"
            string += f"    args = {self.actions[idx].args}\n"
            string += f"    kwargs = {self.actions[idx].kwargs}\n\n"

        return string[:-2]


    def __add__(self,
            other : Any
        ) -> Any:
        """
            Add Actions or Action together.
        """

        if type(other) in [Actions]:
            return Actions(self.actions + other.actions)

        elif type(other) in [Action]:
            return Actions(self.actions + [other])

        else:
            return Actions()



    def __call__(
            self
        ) -> dict[str, Any]:
        """
            Call the saved functions with their arguments.

            Returns:
                dict[str, Any]: Dictionary of functions' return values.
        """

        returns : dict[str, Any] = {}

        for action in self.actions:
            returns[action.name] = action()

        return returns


    def __len__(
            self
        ) -> int:
        """
            Return the length of the Actions object.
        """

        return len(self.actions)


    def __getitem__(
            self,
            item : int
        ) -> Any:
        """
            Return the Action at position 'item'.

            Parameters:
                item (int): Position index.

            Returns:
                Action: Action at position 'item'.
        """

        return self.actions[item]


    def __repr__(
            self
        ) -> str:
        """
            Convert Actions object to string.

            Returns:
                str: Actions string
        """

        return f"Actions({repr(self.actions)})"
