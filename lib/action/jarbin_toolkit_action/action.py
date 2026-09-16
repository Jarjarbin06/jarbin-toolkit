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
from ctypes import (
    c_ulong,
    py_object,
    pythonapi,
)
from threading import (
    Event,
    Lock,
    Thread,
    get_ident,
)

from jarbin_toolkit_action.error import (
    ActionTypeError,
    ActionValueError,
    ActionArgumentError,
    ActionExecutionError,
    ActionThreadError
)
from jarbin_toolkit_action.enums import (
    ActionStatus,
    ActionAsync
)
from jarbin_toolkit_action.time import ActionTimer


class _ActionCancelled(BaseException):
    pass


class Action:


    _thread_actions = {}
    _thread_actions_lock = Lock()


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
            self,
        ):
        self._previous_status = self._status
        self._status = ActionStatus.INACTIVE


    def _prepare_execution(
            self,
            kwargs,
        ):
        self._timer.reset()
        self._status = ActionStatus.PENDING
        self._error = None
        self._output = None
        self._execution_kwargs = self._validate_kwargs(self._kwargs | kwargs)
        self._thread = None
        self._cancel_event.clear()
        self._pause_event.set()


    def _execute_synchronous(
            self,
        ):

        self._status = ActionStatus.RUNNING

        try:
            self._timer.start()
            self._output = self._function(**self._execution_kwargs)
            self._timer.stop()
        except Exception as error:
            self._status = ActionStatus.FAILED
            self._error = error
        else:
            self._status = ActionStatus.SUCCESS
        finally:
            self._save_status()


    def _execute_asynchronous(
            self,
        ):

        self._thread = Thread(
            target=self._thread_execution,
            name=self.name,
            daemon=True,
        )

        return ActionAsync.SUCCESS

    def _thread_execution(
            self,
        ):

        thread_id = get_ident()

        with Action._thread_actions_lock:
            Action._thread_actions[thread_id] = self

        self._status = ActionStatus.RUNNING
        timer_started = False

        try:
            self._pause_event.wait()

            if self._cancel_event.is_set():
                raise _ActionCancelled

            self._timer.start()
            timer_started = True

            self._output = self._function(
                **self._execution_kwargs
            )
        except _ActionCancelled:
            self._status = ActionStatus.CANCELLED
        except Exception as error:
            self._error = error
            self._status = ActionStatus.FAILED
        else:
            self._status = ActionStatus.SUCCESS
        finally:
            if timer_started:
                self._timer.stop()

            with Action._thread_actions_lock:
                Action._thread_actions.pop(
                    thread_id,
                    None
                )

            self._save_status()

    def _kill_thread(
            self,
        ):

        if self._thread is None:
            return

        if not self._thread.is_alive():
            return

        thread_id = self._thread.ident

        if thread_id is None:
            return

        result = pythonapi.PyThreadState_SetAsyncExc(
            c_ulong(thread_id),
            py_object(_ActionCancelled),
        )

        if result == 0:
            raise ActionThreadError(
                "\nFailed to cancel Action thread"
            )

        if result > 1:
            pythonapi.PyThreadState_SetAsyncExc(
                c_ulong(thread_id),
                None,
            )

            raise ActionThreadError(
                "\nFailed to cancel Action thread safely"
            )


    @staticmethod
    def _get_current_action(
        ):

        thread_id = get_ident()

        with Action._thread_actions_lock:
            return Action._thread_actions.get(thread_id)


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
            name = f"Action({getattr(function, '__name__', '')})"

        if not isinstance(name, str):
            raise ActionTypeError(
                "\nName must be a string"
            )

        self.name = name
        self._function = function
        self._signature = signature(function)
        self._output = None
        self._kwargs = self._validate_kwargs(kwargs)
        self._execution_kwargs = self._kwargs | {}
        self._status = ActionStatus.INACTIVE
        self._previous_status = None
        self._error = None
        self._timer = ActionTimer()
        self._settings = {
            "catch": False,
            "asynchronous": False,
        }
        self._thread = None
        self._pause_event = Event()
        self._cancel_event = Event()
        self._execution_lock = Lock()

    def __call__(
            self,
            **kwargs,
        ):

        with self._execution_lock:

            if self._status in (
                    ActionStatus.PENDING,
                    ActionStatus.RUNNING,
                    ActionStatus.PAUSED,
            ):
                raise ActionThreadError(
                    f"\nCannot execute Action from status {self.status}"
                )

            self._prepare_execution(kwargs)

            if self._settings["asynchronous"]:
                return self._execute_asynchronous()

            else:
                self._execute_synchronous()

        if self._error and not self._settings["catch"]:
            raise ActionExecutionError(
                f"\nException caught during execution of {self}"
            ) from self._error

        return self._output


    def __repr__(
            self,
        ):

        return f"<Action: {self.name}: {self._function.__name__}({', '.join(f'{key}={value!r}' for key, value in self._kwargs.items())})>"


    def set_settings(
            self,
            **kwargs,
        ):

        for key, value in kwargs.items():

            if not key in self._settings:
                raise ActionArgumentError(f"\nInvalid setting: {key}={value}")

            self._settings[key] = value

    def start(
            self,
        ):

        with self._execution_lock:

            if self._thread is None:
                raise ActionThreadError(
                    "\nAction has no pending asynchronous execution"
                )

            if self._status != ActionStatus.PENDING:
                raise ActionThreadError(
                    f"\nCannot start Action from status {self.status}"
                )

            if self._thread.is_alive():
                raise ActionThreadError(
                    "\nAction thread is already running"
                )

            self._thread.start()

    def pause(
            self,
        ):

        with self._execution_lock:
            if self._status != ActionStatus.RUNNING:
                raise ActionThreadError(
                    f"\nCannot pause Action from status {self.status}"
                )

            self._pause_event.clear()
            self._status = ActionStatus.PAUSED

    def resume(
            self,
        ):

        with self._execution_lock:
            if self._status != ActionStatus.PAUSED:
                raise ActionThreadError(
                    f"\nCannot resume Action from status {self.status}"
                )

            self._pause_event.set()
            self._status = ActionStatus.RUNNING

    def cancel(
            self,
        ):

        with self._execution_lock:

            if self._status not in (
                    ActionStatus.PENDING,
                    ActionStatus.RUNNING,
                    ActionStatus.PAUSED,
            ):
                raise ActionThreadError(
                    f"\nCannot cancel Action from status {self.status}"
                )

            self._cancel_event.set()
            self._pause_event.set()

            if self._status == ActionStatus.PENDING:
                self._status = ActionStatus.CANCELLED
                self._save_status()
                return

            self._kill_thread()


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


    @staticmethod
    def pause_point(
        ):

        action = Action._get_current_action()

        if action is None:
            return

        if action._cancel_event.is_set():
            raise _ActionCancelled

        action._pause_event.wait()

        if action._cancel_event.is_set():
            raise _ActionCancelled


__all__ = [
    'Action',
]
