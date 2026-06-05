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

from typing import Any
from jarbin_toolkit_jartest.assertion import AssertionResult
from jarbin_toolkit_jartest.benchmark import Benchmark
from jarbin_toolkit_error import Error


class JarTest:
    """
        JarTest class.

        JarTest object to test any program.
    """


    def __init__(
            self
        ) -> None :

        self.tests : dict[str, Benchmark] = {}


    def run(
            self,
            **kwargs
        ) -> None :

        from jarbin_toolkit_jartest.benchmark import Benchmark
        from jarbin_toolkit_console import Console, ANSI, Text

        def get_last_assertions(test: Benchmark) -> list[AssertionResult]:
            if test.assertion is None:
                return []
            return test.assertion

        def has_failed_assertions(test: Benchmark):
            return any(not a.passed for a in get_last_assertions(test))

        def format_assertions(test: Benchmark):
            asserts = get_last_assertions(test)

            if not asserts:
                return "-".center(19)

            failed = [a for a in asserts if not a.passed]

            if not failed:
                return "-".center(19)

            a: AssertionResult = failed[0]

            msg = (f"{a.message}: " if a.message else "") + f"{a.actual!r} {a.meta.get("operator", "?")} {a.expected!r} (failed)"

            if len(msg) > (len(Console) - 10) - 100:
                msg = (f"{a.message}: " if a.message else "") + f"A {a.meta.get("operator", "?")} B (failed)"

            return f"{msg}"

        def get_status(test: Benchmark):

            if test.error is not None:
                return "CRITIC"
            elif has_failed_assertions(test):
                return "FAIL"
            else:
                return "SUCCESS"

        def run_test(test_name: str):

            test = self.tests[test_name]

            test(kw_n)

            status = get_status(test)

            Console.print(f"{app_c["DIM"]}{list(self.tests.keys()).index(test_name):03d}{app_c["RESET"]} " + f"{app_c[status]}{self.tests[test_name].name.removeprefix("JT_")}", ANSI.Cursor.move_column(59).s, f"{app_c["DIM"]}({test_name}){app_c["RESET"]}")

        def show_results(key: str, test: Benchmark):

            status = get_status(test)

            Console.print(
                (("╠═" if status == "CRITIC" else "├ ") if status != "SUCCESS" else "│ ") + app_c["DIM"] + f"{list(self.tests.keys()).index(key):03d}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + (f" {app_c[status]}{app_i[status]}{app_c["RESET"]} "),
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c[status] + f"{app_c["BOLD"] if status == "CRITIC" else ""}{f" {(test.name if len(test.name) < 50 else (test.name[:50] + "...")).removeprefix("JT_")} ".center(50, ("═" if status == "CRITIC" else ("─" if status == "FAIL" else " "))):40}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["TIME"] + f"{(f" {("0.000s" if status == "CRITIC" or test.time == 0 else test.time_str)} ").center(15, ("═" if status == "CRITIC" else ("─" if status == "FAIL" else " "))):}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["RUN"] + f"{test.test_amount:03}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["ERROR"] + f"{(f" {app_c["BOLD"]}{f"{test.error.error}: {test.error.message}" if isinstance(test.error, Error) else test.error}" if status == "CRITIC" else format_assertions(test))}",
                (" │" if status == "SUCCESS" else ""),
                separator=""
            )

        def run_tests():

            Console.print(line)
            Console.print(app_c["TITLE"] + "─── JarTest ───".center(term_width))
            Console.print(line)
            Console.print(app_c["TITLE"] + "─── TESTS ───".center(112, "="))

            for name in self.tests:
                run_test(name)

            Console.print(app_c["TITLE"] + "─── RESULTS ───".center(112, "="))

            Console.print(f"┌{"─" * 5}┬{"─" * 5}┬{"─" * 52}┬{"─" * 17}┬{"─" * 5}┬{"─" * 21}┐")
            Console.print(
                f"│ {app_c["BOLD"] + app_c["WHITE"]}idx",
                f"│ {app_c["BOLD"] + app_c["WHITE"]}stt",
                f"│ {app_c["BOLD"] + app_c["WHITE"]}{"name".center(50):}",
                f"│ {app_c["BOLD"] + app_c["WHITE"]}{app_c["TIME"]}{"time".center(15)}",
                f"│ {app_c["BOLD"] + app_c["WHITE"]}{app_c["RUN"]}run",
                f"│ {app_c["BOLD"] + app_c["WHITE"]}{app_c["ERROR"]}{"assertion/error".center(20)}{app_c["RESET"]}│"
            )
            Console.print(f"├{"─" * 5}┼{"─" * 5}┼{"─" * 52}┼{"─" * 17}┼{"─" * 5}┼{"─" * 21}┤")

            for name in self.tests:
                show_results(name, self.tests[name])

            Console.print(f"└{"─" * 5}┴{"─" * 5}┴{"─" * 52}┴{"─" * 17}┴{"─" * 5}┴{"─" * 21}┘")

        app_c : dict[str, str] = {
            "TITLE" : ANSI.Color.rgb_fg(255, 160, 0).s,
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
        app_i : dict[str, str] = {
            "SUCCESS": "✔",
            "FAIL": "✘",
            "CRITIC": "☢"
        }
        term_width, term_height = Console.get_size()
        line = app_c["TITLE"] + ("-" * term_width)
        kw_n = int(kwargs.get("n", 1))

        try:
            run_tests()

        except KeyboardInterrupt:
            Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- interrupt (^C) -- {app_i["CRITIC"]}", app_c["CRITIC"]))

        except SystemExit:
            Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- exit (sys-exit) -- {app_i["FAIL"]}", app_c["FAIL"]))

        else:
            Console.print(ANSI.Line.clear_line() + Text.Format.apply(f"\n-- end -- {app_i["SUCCESS"]}", app_c["WHITE"]))


    def fetch(
            self,
            *,
            prefix : str = "JT_",
            module : Any = None,
            name_prefix : str = ""
        ) -> list[tuple[str, str, inspect.Signature | None]] :
        """
            Fetch all tests from JarTest object.
        """

        def check_name(
            ) -> bool :

            try :
                assert name.startswith(prefix)
                assert callable(items[name])
                assert len(inspect.signature(items[name]).parameters) == 0

            except AssertionError :
                return False

            else :
                return True

        def get_fail(
            ) -> None :
                try :
                    sign = inspect.signature(items[name])

                except TypeError :
                    sign = None

                failed_append.append(
                    (
                        name,
                        f"{repr(items[name]):.50s}",
                        sign
                    )
                )

        if module is None:

            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])

        items : dict[str, Any] = module.__dict__
        temp_dict : dict[str, Benchmark] = {}
        failed_append : list[tuple[str, str, inspect.Signature | None]] = []

        for name in items :
            if check_name() :
                temp_dict[name] = Benchmark(items[name])
            else :
                get_fail()

        for name in temp_dict :
            if name in self.tests :
                get_fail()
            else :
                self.tests[name_prefix + name] = temp_dict[name]

        return failed_append

    def fetch_tests(
            self,
            *,
            module: Any = None,
            name_prefix: str = "",
            _visited: set = None
    ) -> list[str]:

        from types import ModuleType

        if _visited is None:
            _visited = set()

        failed: list[str] = []

        if module is None:
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])

        if id(module) in _visited:
            return failed

        _visited.add(id(module))

        items = module.__dict__

        for name, obj in items.items():

            if name.startswith("__"):
                continue

            if isinstance(obj, ModuleType):
                failed += self.fetch_tests(
                    module=obj,
                    name_prefix=name_prefix + name + "/",
                    _visited=_visited
                )
                continue

            if isinstance(obj, JarTest):

                tests_cpy = obj.tests.copy()

                for test_name, test_obj in tests_cpy.items():

                    final_name = name_prefix + name + "/" + test_name

                    if final_name in self.tests or not final_name.startswith("JT_") :
                        failed.append(final_name)
                        continue

                    self.tests[final_name] = test_obj

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
        test_names = list(self.tests.keys())
        return f"JarTest(tests={test_names})"
