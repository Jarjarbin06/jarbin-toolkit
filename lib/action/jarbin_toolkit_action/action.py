# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : action.py
# Class        : Action
#
# Author       : Jarjarbin06
# ============================================================================


from inspect import signature

from jarbin_toolkit_action.error import ActionTypeError, ActionValueError


class Action:


    def _validate_kwargs(
            self,
            kwargs
        ):

        try:
            bound = self._signature.bind(**kwargs)
            bound.apply_defaults()

            return dict(bound.arguments)
        except TypeError as error:
            raise ActionValueError(
                f"\nAction() invalid arguments: {error}"
            ) from error


    def __init__(
            self,
            *args,
            **kwargs
        ):

        if len(args) == 1:
            function = args[0]
            name = None
        elif len(args) == 2:
            name, function = args
        else:
            raise ActionValueError(
                f"\nAction() takes 1 or 2 positional arguments but {len(args)} were given"
            )

        if not callable(function):
            raise ActionTypeError(
                "\nAction() function must be callable"
            )

        if name is None:
            name = f"Action({function.__name__})"

        if not isinstance(name, str):
            raise ActionTypeError(
                "\nAction() name must be a string"
            )

        self.name = name
        self._function = function
        self._signature = signature(function)
        self._output = None
        self._kwargs = self._validate_kwargs(kwargs)



    @property
    def output(
            self
        ):

        return self._output


    def __call__(
            self,
            **kwargs
        ):

        kwargs = self._validate_kwargs(self._kwargs | kwargs)

        self._output = self._function(**kwargs)

        return self._output


    def __repr__(
            self
        ):

        return f"<Action: {self.name}: {self._function.__name__}({', '.join(f'{key}={value!r}' for key, value in self._kwargs.items())})>"


__all__ = [
    'Action'
]
