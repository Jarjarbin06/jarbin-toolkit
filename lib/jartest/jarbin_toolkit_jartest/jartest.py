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
from typing import Callable, Any
from jarbin_toolkit_jartest.benchmark import Benchmark


class JarTest:
    """
        JarTest class.

        JarTest object to test any program.
    """


    def __init__(
            self
        ) -> None :
        """
            Log class constructor.
        """

        self.tests : dict[str, Benchmark] = {}


    def run(
            self,
            **kwargs
        ) -> None :
        """
            Run and show results of JarTests.

            Parameters:

            n (int): amount of tests per function.
        """

        from jarbin_toolkit_jartest.benchmark import Benchmark
        from jarbin_toolkit_console import Console, ANSI

        def show_tests(test_name: str):

            test = self.tests[test_name]

            test(kw_n)

            if test.error is not None:
                status = "CRITIC"
            elif test.assertion is not None:
                status = "FAIL"
            else:
                status = "SUCCESS"

            Console.print(f"{app_c["DIM"]}{list(self.tests.keys()).index(test.name):03d}{app_c["RESET"]} " + f"{app_c[status]}{test.name.removeprefix("JT_")}", f"{app_c["DIM"]}({test_name}){app_c["RESET"]}")

        def show_results(test: Benchmark):

            if test.error is not None:
                status = "CRITIC"
            elif test.assertion is not None:
                status = "FAIL"
            else:
                status = "SUCCESS"

            Console.print(
                (("╠═" if status == "CRITIC" else "├ ") if status != "SUCCESS" else "│ ") + app_c["DIM"] + f"{list(self.tests.keys()).index(test.name):03d}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + (f" {app_c[status]}{app_i[status]}{app_c["RESET"]} "),
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c[status] + f"{app_c["BOLD"] if status == "CRITIC" else ""}{f" {(test.name if len(test.name) < 50 else (test.name[:50] + "...")).removeprefix("JT_")} ".center(50, ("═" if status == "CRITIC" else ("─" if status == "FAIL" else " "))):40}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["TIME"] + f"{(f" {("0.000s" if status == "CRITIC" or test.time == 0 else test.time_str)} ").center(15, ("═" if status == "CRITIC" else ("─" if status == "FAIL" else " "))):}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["RUN"] + f"{test.test_amount:03}",
                (("═╬═" if status == "CRITIC" else " ┼ ") if status != "SUCCESS" else " │ ") + app_c["ERROR"] + f"{(f" {app_c["BOLD"]}{test.error!r}" if status == "CRITIC" else (f"Assertion failed: \"{test.assertion if len(str(test.assertion)) > 0 else "No message"}\"" if status == "FAIL" else "-".center(19)))}",
                (" │" if status == "SUCCESS" else ""),
                separator=""
            )

        def run_once():

            Console.print(line)
            Console.print(app_c["TITLE"] + "─── JarTest ───".center(term_width))
            Console.print(line)
            Console.print(app_c["TITLE"] + "─── TESTS ───".center(112, "="))

            for test_name in to_run:
                show_tests(test_name)

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
                show_results(self.tests[name])

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
            "CRITIC": "⛔",
        }
        term_width, term_height = Console.get_size()
        line = app_c["TITLE"] + ("-" * term_width)
        to_run = list(kwargs.get("test", self.tests.keys()))
        kw_n = int(kwargs.get("n", 1))

        run_once()


    def fetch(
            self,
            *,
            prefix : str = "JT_",
            module : Any = None,
            name_prefix : str = ""
        ) -> list[tuple[str, Callable[[], None]]] :
        """
            Fetch all tests from JarTest object.
        """

        from sys import modules
        from inspect import Signature, signature

        def clean_dict(
            ) -> None :

            items_cpy = items.copy()

            for item in items_cpy:
                if item.startswith("__") or item.startswith("jarbin_toolkit") :
                    items.pop(item)

        def check_name(
            ) -> bool :

            try :
                assert name.startswith(prefix)
                assert callable(items[name])
                assert len(signature(items[name]).parameters) == 0

            except AssertionError :
                return False

            else :
                return True

        def get_fail(
            ) -> None :
                try :
                    sign = signature(items[name])

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
        failed_append : list[tuple[str, str, Signature | None]] = []

        clean_dict()

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

        from sys import modules
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
