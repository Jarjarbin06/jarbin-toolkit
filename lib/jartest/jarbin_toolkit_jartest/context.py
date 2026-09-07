#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
###   ----context.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from typing import Any, Optional, Callable
from sys import version
import os
import subprocess
from shlex import split

from jarbin_toolkit_console import Console, ANSI


class Context:


    _C = {
        "DIM": ANSI.Color(ANSI.Color.C_FG_DARK).s,
        "RESET": ANSI.Color(ANSI.Color.C_RESET).s,
        "TITLE": ANSI.Color.rgb_fg(255, 160, 0).s,
        "KEY": ANSI.Color.rgb_fg(255, 160, 0).s,
        "VALUE": ANSI.Color.rgb_fg(0, 255, 255).s,
        "TYPE": ANSI.Color.rgb_fg(100, 100, 255).s,
        "SUCCESS": ANSI.Color.rgb_fg(100, 255, 100).s,
        "WARNING": ANSI.Color.rgb_fg(255, 160, 0).s,
        "ERROR": ANSI.Color.rgb_fg(255, 100, 100).s,
        "CRITICAL": ANSI.Color.rgb_fg(255, 0, 255).s,
    }


    class Decorators:


        @staticmethod
        def output(
                **variables: str
            ):

            def decorator(
                    function: Callable[[], None]
                ):
                context = getattr(
                    function,
                    "_jartest_context",
                    Context()
                )

                context._output.update(variables)
                function._jartest_context = context

                return function

            return decorator


        @staticmethod
        def env(
                **variables: str
            ):

            def decorator(
                    function: Callable[[], None]
                ):
                context = getattr(
                    function,
                    "_jartest_context",
                    Context()
                )

                context._env.update(variables)
                function._jartest_context = context

                return function

            return decorator


        @staticmethod
        def command(
                setup: Optional[str] = None,
                teardown: Optional[str] = None
            ):

            def decorator(
                    function: Callable[[], None]
                ):
                context = getattr(
                    function,
                    "_jartest_context",
                    Context()
                )

                context._command.append((setup, teardown))
                function._jartest_context = context

                return function

            return decorator


    def __init__(
            self,
            *,
            output: Optional[dict[str, Any]] = None,
            env: Optional[dict[str, str]] = None,
            python: Optional[dict[str, Any]] = None,
            command: Optional[list[tuple[Optional[str], Optional[str]]]] = None,
            condition: Optional[dict[str, dict[Any, Any]]] = None,
        ) -> None:

        output = (output or {}).copy()
        env = (env or {}).copy()
        python = (python or {}).copy()
        command = (command or []).copy()
        condition = (condition or {}).copy()

        self._output: dict[str, Any] = {
            "show_test": output.get("show_test", True),
            "show_result": output.get("show_result", True),
            "show_output": output.get("show_output", True),
            "show_context": output.get("show_context", False),
        }
        self._env: dict[str, str] = env
        self._python: dict[str, Any] = {
            "version": python.get("version", version),
        }
        self._command: list[tuple[Optional[str], Optional[str]]] = [(cmd if isinstance(cmd, tuple) else (cmd, None)) for cmd in command]
        self._condition: dict[str, Any] = {
            "eq": condition.get("eq", {}),
            "neq": condition.get("neq", {}),
            "contain": condition.get("contain", {}),
            "ncontain": condition.get("ncontain", {}),
        }
        self._save: dict[str, Any] = {}


    def get(
            self,
            category: str,
            setting: str,
            default: Any = None
        ) -> Any:
        return getattr(self, f"_{category}").get(setting, default)


    def inherit(
            self,
            parent: "Context"
        ) -> None:

        #self._output.update(parent._output)
        #self._env.update(parent._env)
        #self._python.update(parent._python)
        #self._command = parent._command.copy() + self._command
        #for key in parent._condition:
        #    self._condition[key].update(parent._condition[key])
        pass


    @staticmethod
    def _show_backslashes(string: str) -> str:
        result = []
        current = None

        def add(
                text: str,
                color: str
        ) -> None:
            nonlocal current

            if current != color:
                result.append(color)
                current = color

            result.append(text)

        i = 0

        while i < len(string):
            char = string[i]

            if char == "\x1b":
                add("\\x1b", Context._C["TYPE"])
            elif char == "\n":
                add("\\n", Context._C["TYPE"])
            elif char == "\r":
                add("\\r", Context._C["TYPE"])
            elif char == "\t":
                add("\\t", Context._C["TYPE"])
            elif char == "\\":
                add("\\\\", Context._C["TYPE"])
            else:
                add(char, Context._C["VALUE"])

            i += 1

        result.append(Context._C["RESET"])

        return "".join(result)


    def setup(
            self,
            *,
            jt_wide: bool = False
        ) -> None:

        tab = "   " if jt_wide else "       "

        if self._output["show_context"]:
            Console.print(f"{Context._C["TITLE"]}{tab}Setup {Context._C["DIM"]}({'JarTest' if jt_wide else 'Benchmark'})")


        self._save["env"] = dict(os.environ)

        if self._output["show_context"]:
            Console.print(
                f"{tab} - ENV | " + Context._C["VALUE"]
                + "env saved"
            )


        for env, var in self._env.items():
            os.environ[env] = var

            if self._output["show_context"]:
                Console.print(
                    f"{tab} - ENV | " + Context._C["VALUE"]
                    + f"{env} = {var}"
                )


        for cmd in self._command:
            if cmd[0] is not None:
                process = subprocess.run(split(cmd[0]), capture_output=True)

                if self._output["show_context"]:
                    Console.print(
                        f"{tab} - COMMAND"
                        + (Context._C["SUCCESS"] if not process.returncode else Context._C["ERROR"])
                        + f" ({process.returncode})" + Context._C["RESET"]
                        + (
                            " | command: " + Context._C["VALUE"]
                            + Context._show_backslashes(cmd[0])
                            if cmd[0] else ""
                        )
                        + (
                            " | output: " + Context._C["VALUE"]
                            + Context._show_backslashes(process.stdout.decode())
                            if process.stdout else ""
                        )
                        + (
                            " | error: " + Context._C["VALUE"]
                            + Context._show_backslashes(process.stderr.decode())
                            if process.stderr else ""
                        )
                    )


    def teardown(
            self,
            *,
            jt_wide: bool = False
        ) -> None:

        tab = "   " if jt_wide else "       "

        if self._output["show_context"]:
            Console.print(f"{Context._C["TITLE"]}{tab}Teardown {Context._C["DIM"]}({'JarTest' if jt_wide else 'Benchmark'})")


        os.environ.clear()
        os.environ.update(self._save["env"])

        if self._output["show_context"]:
            Console.print(
                f"{tab} - ENV | " + Context._C["VALUE"]
                + "env restored"
            )


        for cmd in self._command[::-1]:
            if cmd[1] is not None:
                process = subprocess.run(split(cmd[1]), capture_output=True)

                if self._output["show_context"]:
                    Console.print(
                        f"{tab} - COMMAND"
                        + (Context._C["SUCCESS"] if not process.returncode else Context._C["ERROR"])
                        + f" ({process.returncode})" + Context._C["RESET"]
                        + (
                            " | command: " + Context._C["VALUE"]
                            + Context._show_backslashes(cmd[1])
                            if cmd[1] else ""
                        )
                        + (
                            " | output: " + Context._C["VALUE"]
                            + Context._show_backslashes(process.stdout.decode())
                            if process.stdout else ""
                        )
                        + (
                            " | error: " + Context._C["VALUE"]
                            + Context._show_backslashes(process.stderr.decode())
                            if process.stderr else ""
                        )
                    )


    def __enter__(
            self
        ) -> "Context":
        self.setup()
        return self


    def __exit__(
            self,
            exc_type,
            exc_val,
            exc_tb
        ) -> bool:
        self.teardown()
        return False
