#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
###   ----jartest.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from __future__ import annotations

import inspect
from typing import Any, Optional

from jarbin_toolkit_error import BaseError
from jarbin_toolkit_console import Console, ANSI, Text

from jarbin_toolkit_jartest.assertion import AssertionResult
from jarbin_toolkit_jartest.benchmark import Benchmark
from jarbin_toolkit_jartest.show import Show
from jarbin_toolkit_jartest import Context


class JarTest:
    """
        JarTest testing object.
    """


    _C: dict[str, str] = {
        "TITLE": ANSI.Color.rgb_fg(255, 160, 0).s,
        "ERROR": ANSI.Color.rgb_fg(255, 0, 255).s,
        "TIME": ANSI.Color.rgb_fg(0, 255, 255).s,
        "RUN": ANSI.Color.rgb_fg(100, 100, 255).s,
        "SUCCESS": ANSI.Color.rgb_fg(100, 255, 100).s,
        "FAIL": ANSI.Color.rgb_fg(255, 100, 100).s,
        "CRITIC": ANSI.Color.rgb_fg(255, 100, 100).s,
        "WHITE": ANSI.Color.rgb_fg(255, 255, 255).s,
        "DIM": ANSI.Color(ANSI.Color.C_FG_DARK).s,
        "BOLD": ANSI.Color(ANSI.Color.C_BOLD).s,
        "RESET": ANSI.Color(ANSI.Color.C_RESET).s
    }

    _I: dict[str, str] = {
        "SUCCESS": "✔",
        "FAIL": "✘",
        "CRITIC": "☢"
    }


    def __init__(
            self,
            *,
            context: Optional[Context] = None
        ) -> None :
        """
            Initialize JarTest object.
            
            Parameters:
                context (Optional[Context]): JarTest context.
        """

        self.tests : dict[str, Benchmark] = {}
        self.jartests : dict[str, JarTest] = {}
        self.context: Context = context or Context()
        self._name: str = "?"

        Show._show_output = self.context.get("output", "show_output", True)


    def _get_last_assertions(
            self,
            test: Benchmark
        ) -> list[AssertionResult] | None:
        if test.assertion is None:
            return []
        return test.assertion


    def _has_failed_assertions(
            self,
            test: Benchmark
        ) -> bool:
        return any(not a.passed for a in (self._get_last_assertions(test) or []))


    def _format_assertions(
            self,
            test: Benchmark
        ) -> str:
        asserts = self._get_last_assertions(test)

        if not asserts:
            return "-".center(19)

        failed = [a for a in asserts if not a.passed]

        if not failed:
            return "-".center(19)

        a: AssertionResult = failed[0]

        msg = (f"{a.message}" if a.message else "") + (": " if a.message and a.values else "") + (f"{a.actual!r} {a.meta.get('operator', '?')} {a.expected}" if a.values else "") + " (failed)"

        if len(msg) > (len(Console) - 10) - 100:
            msg = (f"{a.message}: " if a.message else "") + f"A {a.meta.get('operator', '?')} B (failed)"

        return f"{msg}"

    def _get_status(
            self,
            test: Benchmark
        ) -> str:

        if test.error is not None:
            return "CRITIC"
        elif self._has_failed_assertions(test):
            return "FAIL"
        else:
            return "SUCCESS"

    def _run_test(
            self,
            test_name: str,
            kw_n: int,
            idx: int,
            path: str,
        ) -> None:

        test = self.tests[test_name]

        Show._show_output = test.context.get("output", "show_output", True)

        with test.context:
            test(kw_n)

            Show._close()

            Show._show_output = self.context.get("output", "show_output", True)

            if self.context.get("output", "show_test", True):
                status = self._get_status(test)
                Console.print(
                    f"{JarTest._C['DIM']}{idx:03d}{JarTest._C['RESET']} "
                    + f"{JarTest._C[status]}{self.tests[test_name].name.removeprefix('JT_')}",
                    ANSI.Cursor.move_column(59).s,
                    f"{JarTest._C['DIM']}({path} / {test_name}){JarTest._C['RESET']}"
                )

    def _show_results(
            self,
            test: Benchmark,
            idx: int,
        ) -> None:

        status = self._get_status(test)

        Console.print(
            (("╠═" if status == "CRITIC" else "├ ") if status != "SUCCESS" else "│ ") + JarTest._C["DIM"] + f"{idx:03d}",
            (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + f" {JarTest._C[status]}{JarTest._I[status]}{JarTest._C['RESET']} ",
            (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + JarTest._C[
                status] + f"{JarTest._C['BOLD'] if status == 'CRITIC' else ''}{f" {(test.name if len(test.name) < 50 else (test.name[:50] + '...')).removeprefix('JT_')} ".center(50, ('=' if status == 'CRITIC' else ('─' if status == 'FAIL' else ' '))):40}",
            (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + JarTest._C[
                "TIME"] + f"{f' {('0.000s' if status == 'CRITIC' or test.time == 0 else test.time_str)} '.center(15, ('═' if status == 'CRITIC' else ('─' if status == 'FAIL' else ' '))):}",
            (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + JarTest._C["RUN"] + f"{test.test_amount:03}",
            (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + JarTest._C[
                "ERROR"] + f"{(f' {JarTest._C['BOLD']}{f'{test.error.error}: {test.error.message}' if isinstance(test.error, BaseError) else test.error}' if status == 'CRITIC' else self._format_assertions(test))}",
            (" │" if status == "SUCCESS" else ""),
            separator=""
        )

    def _run_tests(
            self,
            kw_n: int,
            results: list[tuple[int, "JarTest", str, Benchmark]],
            idx: int,
            path: str,
            is_main: bool = False,
            _visited: set[int] | None = None
        ) -> int:

        if _visited is None:
            _visited = set()

        if id(self) in _visited:
            return

        _visited.add(id(self))

        term_width, term_height = Console.get_size()
        line = JarTest._C["TITLE"] + ("-" * term_width)

        if is_main and self.context.get("output", "show_test", True):
            Console.print(line)
            Console.print(JarTest._C["TITLE"] + "─── JarTest ───".center(term_width))
            Console.print(line)
            Console.print(JarTest._C["TITLE"] + "─── TESTS ───".center(112, "="))

        self.context.setup(jt_wide=True)

        for name, test in self.tests.items():
            self._run_test(name, kw_n, idx, path)

            results.append(
                (
                    idx,
                    self,
                    name,
                    test
                )
            )
            idx += 1

        for name, jartest in self.jartests.items():
            idx = jartest._run_tests(
                kw_n,
                results,
                idx,
                f"{path} / {name}"
            )

        self.context.teardown(jt_wide=True)

        return idx

    def run(
            self,
            **kwargs
        ) -> int :

        kw_n = int(kwargs.get("n", 1))
        e_success, e_failure, e_critic = 0, 1, 84
        results: list[tuple[int, JarTest, str, Benchmark]] = []

        try:
            self._run_tests(kw_n, results, 0, self._name, True)

        except KeyboardInterrupt:
            Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- interrupt (^C) -- {JarTest._I["CRITIC"]}", JarTest._C["CRITIC"]))
            return e_critic

        except SystemExit:
            Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- exit (sys-exit) -- {JarTest._I["FAIL"]}", JarTest._C["FAIL"]))
            return e_failure

        else:

            if self.context.get("output", "show_result", True):
                Console.print(JarTest._C["TITLE"] + "─── RESULTS ───".center(112, "="))

                Console.print(f"┌{'─' * 5}┬{'─' * 5}┬{'─' * 52}┬{'─' * 17}┬{'─' * 5}┬{'─' * 21}┐")
                Console.print(
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}idx",
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}stt",
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}{"name".center(50)}",
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}{JarTest._C['TIME']}{'time'.center(15)}",
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}{JarTest._C['RUN']}run",
                    f"│ {JarTest._C['BOLD'] + JarTest._C['WHITE']}{JarTest._C['ERROR']}{'assertion/error'.center(20)}{JarTest._C['RESET']}│"
                )
                Console.print(f"├{'─' * 5}┼{'─' * 5}┼{'─' * 52}┼{'─' * 17}┼{'─' * 5}┼{'─' * 21}┤")

                for idx, jt, name, bm in results:
                    if bm.context.get("output", "show_result", True):
                        jt._show_results(bm, idx)

                Console.print(f"└{'─' * 5}┴{'─' * 5}┴{'─' * 52}┴{'─' * 17}┴{'─' * 5}┴{'─' * 21}┘")

            if self.context.get("output", "show_test", True) or self.context.get("output", "show_result", True) or self.context.get("output", "show_output", True):
                Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- end -- {JarTest._I["SUCCESS"]}", JarTest._C["WHITE"]))

            for test in self.tests.values():
                if self._get_status(test) == "FAIL":
                    return e_failure
                if self._get_status(test) == "CRITIC":
                    return e_critic

            return e_success


    def fetch(
            self,
            *,
            prefix: str = "JT_",
            module: Any = None,
            name_prefix: str = "",
            _visited: set[int] | None = None
        ) -> list[tuple[str, str, inspect.Signature | None]]:
        """
            Fetch tests and sub-JarTests from a module.
        """

        from types import ModuleType

        if _visited is None:
            _visited = set()

        if module is None:
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])

        if module is None or id(module) in _visited:
            return []

        _visited.add(id(module))

        items = module.__dict__
        failed: list[tuple[str, str, inspect.Signature | None]] = []

        for name, obj in items.items():
            if obj is self or name.startswith("__"):
                self._name = name
                continue

            final_name = name_prefix + name

            if isinstance(obj, ModuleType):
                module_jartests = [
                    child
                    for child in obj.__dict__.values()
                    if isinstance(child, JarTest)
                ]

                if module_jartests:
                    for child in module_jartests:
                        if child is self:
                            continue

                        child_name = next(
                            (
                                child_name
                                for child_name, child_obj in obj.__dict__.items()
                                if child_obj is child
                            ),
                            None
                        )

                        if child_name is None:
                            continue

                        if child_name in self.jartests:
                            failed.append(
                                (
                                    final_name,
                                    repr(child),
                                    None
                                )
                            )
                            continue

                        self.jartests[child_name] = child

                    continue

                failed += self.fetch(
                    prefix=prefix,
                    module=obj,
                    name_prefix=final_name + "/",
                    _visited=_visited
                )
                continue

            if isinstance(obj, JarTest):
                if name in self.jartests:
                    failed.append(
                        (
                            final_name,
                            repr(obj),
                            None
                        )
                    )
                    continue

                self.jartests[name] = obj
                continue

            if not name.startswith(prefix):
                continue

            if not callable(obj):
                continue

            try:
                signature = inspect.signature(obj)

                if len(signature.parameters) != 0:
                    failed.append(
                        (
                            final_name,
                            f"{repr(obj):.50s}",
                            signature
                        )
                    )
                    continue

            except TypeError:
                failed.append(
                    (
                        final_name,
                        f"{repr(obj):.50s}",
                        None
                    )
                )
                continue

            if final_name in self.tests:
                failed.append(
                    (
                        final_name,
                        f"{repr(obj):.50s}",
                        signature
                    )
                )
                continue

            self.tests[final_name] = Benchmark(obj)

        return failed


    def get_tests(
            self
        ) -> dict[str, Benchmark] :
        return self.tests


    def __len__(
            self
        ) -> int:
        return len(self.tests)


    def __call__(
            self,
            *,
            prefix : str = "JT_",
            module : Any = None,
            name_prefix : str = "",
            **kwargs
        ) -> None :

        if module is None:

            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])

        self.fetch(prefix=prefix, module=module, name_prefix=name_prefix)
        self.run(**kwargs)


    def __repr__(
            self
        ) -> str:
        tests = list(self.tests.keys())
        return f"JarTest({tests=!r})"
