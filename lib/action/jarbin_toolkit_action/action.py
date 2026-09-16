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

from jarbin_toolkit_action.error import (
    ActionTypeError,
    ActionValueError,
    ActionArgumentError,
    ActionExecutionError
)
from jarbin_toolkit_action.enums import ActionStatus
from jarbin_toolkit_action.time import ActionTimer


class Action:


    def _validate_kwargs(
            self,
            kwargs,
        ):

        try:
            bound = self._signature.bind(**kwargs)
            bound.apply_defaults()

            return dict(bound.arguments)
        except TypeError as error:
            raise ActionValueError(
                f"\nInvalid arguments: {error}"
            ) from error


    def _save_status(
            self
        ):
        self._previous_status = self._status
        self._status = ActionStatus.INACTIVE


    def __init__(
            self,
            *args,
            **kwargs,
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
                "\nFunction must be callable"
            )

        if name is None:
            name = f"Action({getattr(function, "__name__", "")})"

        if not isinstance(name, str):
            raise ActionTypeError(
                "\nName must be a string"
            )

        self.name = name
        self._function = function
        self._signature = signature(function)
        self._output = None
        self._kwargs = self._validate_kwargs(kwargs)
        self._status = ActionStatus.INACTIVE
        self._previous_status = None
        self._duration = None
        self._error = None
        self._timer = ActionTimer()
        self._settings = {
            "catch": False,
        }


    def __call__(
            self,
            **kwargs,
        ):

        self._timer.reset()
        self._status = ActionStatus.PENDING
        self._error = None

        self._output = None
        kwargs = self._validate_kwargs(self._kwargs | kwargs)

        self._status = ActionStatus.RUNNING

        try:
            self._timer.start()
            self._output = self._function(**kwargs)
            self._timer.stop()
        except Exception as error:
            self._status = ActionStatus.FAILED
            self._error = error
        else:
            self._status = ActionStatus.SUCCESS
        finally:
            self._save_status()

        if self._error and not self._settings["catch"]:
            raise ActionExecutionError(f"\nException caught during execution of {self}") from self._error

        return self._output


    def __repr__(
            self,
        ):

        return f"<Action: {self.name}: {self._function.__name__}({', '.join(f'{key}={value!r}' for key, value in self._kwargs.items())})>"


    def set_setting(
            self,
            **kwargs,
        ):

        for key, value in kwargs.items():

            if not key in self._settings:
                raise ActionArgumentError(f"\nInvalid setting: {key}={value}")

            self._settings[key] = value

    @property
    def output(
            self,
        ):

        return self._output


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
    def error(
            self,
        ):

        return self._error


    @property
    def duration(
            self,
        ):

        return self._timer.elapsed() if self._previous_status is not None else None


__all__ = [
    'Action',
]
