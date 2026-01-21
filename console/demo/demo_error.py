#!/usr/bin/env python3
"""
    FULL EPITECH_CONSOLE – ERROR MODULE DEMO
    =======================================

    This script is a REAL MANUAL TEST of the Error module.

    It covers:
    - Error default constructor
    - Custom error name
    - Custom message
    - Link (file, line)
    - Printing Error directly
    - Raising Error as exception
    - Catching Error
    - Chaining Error usage
    - Edge cases (empty message, empty error name)
    - Error used as display-only
    - Error used as control-flow exception

    Run in a REAL terminal.
"""


def error_demo(
    ) -> None:
    from epitech_console.Error import Error
    from epitech_console import System

    Console = System.Console
    Time = System.Time


    # ============================================================
    # BASIC ERROR (DEFAULT)
    # ============================================================

    print("\n=== BASIC ERROR (DEFAULT) ===")

    err = Error()
    Console.print(err)

    print("\n(Default error message and name should be shown)")


    # ============================================================
    # CUSTOM MESSAGE
    # ============================================================

    print("\n=== CUSTOM ERROR MESSAGE ===")

    err = Error(message="Something went wrong")
    Console.print(err)


    # ============================================================
    # CUSTOM MULTIPLE LINE MESSAGE
    # ============================================================

    print("\n=== CUSTOM MULTIPLE LINE MESSAGE ===")

    err = Error(message="On the left side of my brain, there's nothing right.\nAnd on the right side, there's nothing left.")
    Console.print(err)


    # ============================================================
    # CUSTOM ERROR NAME
    # ============================================================

    print("\n=== CUSTOM ERROR NAME ===")

    err = Error(
        message="Invalid configuration detected",
        error="ConfigError"
    )
    Console.print(err)


    # ============================================================
    # ERROR WITH FILE LINK
    # ============================================================

    print("\n=== ERROR WITH FILE LINK ===")

    err = Error(
        message="Failed to parse configuration file",
        error="ConfigError",
        link=("epitech_console/config.ini", 12)
    )
    Console.print(err)

    print("\n(The file path and line number should be visible)")


    # ============================================================
    # ERROR WITHOUT LINE NUMBER
    # ============================================================

    print("\n=== ERROR WITH FILE LINK (NO LINE) ===")

    err = Error(
        message="Missing environment variable",
        error="EnvError",
        link=("demo/demo_error.py", None)
    )
    Console.print(err)


    # ============================================================
    # ERROR USED AS DISPLAY-ONLY (NO EXCEPTION)
    # ============================================================

    print("\n=== DISPLAY-ONLY ERROR ===")

    def display_error_only():
        err = Error(
            message="This error is only displayed",
            error="DisplayError"
        )
        Console.print(err)

    display_error_only()

    print("\n(Program continues normally)")


    # ============================================================
    # ERROR RAISED AS EXCEPTION
    # ============================================================

    print("\n=== ERROR RAISED AS EXCEPTION ===")

    try:
        raise Error(
            message="Fatal error occurred",
            error="FatalError"
        )
    except Error as e:
        print("Caught Error:")
        Console.print(e)


    # ============================================================
    # ERROR WITH LINK RAISED
    # ============================================================

    print("\n=== ERROR WITH LINK RAISED ===")

    try:
        raise Error(
            message="Division by zero",
            error="MathError",
            link=("calculator.py", 42)
        )
    except Error as e:
        Console.print(e)


    # ============================================================
    # ERROR IN FUNCTION CONTROL FLOW
    # ============================================================

    print("\n=== ERROR USED FOR CONTROL FLOW ===")

    def divide(a, b):
        if b == 0:
            raise Error(
                message="Cannot divide by zero",
                error="MathError",
                link=("epitech_console/demo/demo_error.py", 156)
            )
        return a / b

    try:
        divide(10, 0)
    except Error as e:
        Console.print(e)

    print("\n(Function execution stopped correctly)")


    # ============================================================
    # MULTIPLE ERRORS IN SEQUENCE
    # ============================================================

    print("\n=== MULTIPLE ERRORS SEQUENCE ===")

    errors = [
        Error("First error", error="TestError"),
        Error("Second error", error="TestError"),
        Error("Third error", error="TestError", link=("sequence.py", 99)),
    ]

    for e in errors:
        Console.print(e)
        Time.wait(0.1)


    # ============================================================
    # EMPTY MESSAGE
    # ============================================================

    print("\n=== EMPTY MESSAGE ===")

    err = Error(message="")
    Console.print(err)


    # ============================================================
    # EMPTY ERROR NAME
    # ============================================================

    print("\n=== EMPTY ERROR NAME ===")

    err = Error(
        message="Error without a name",
        error=""
    )
    Console.print(err)


    # ============================================================
    # BOTH MESSAGE AND ERROR EMPTY
    # ============================================================

    print("\n=== EMPTY MESSAGE AND ERROR NAME ===")

    err = Error(message="", error="")
    Console.print(err)


    # ============================================================
    # ERROR STORED AND PRINTED LATER
    # ============================================================

    print("\n=== ERROR STORED AND PRINTED LATER ===")

    stored_error = Error(
        message="Deferred error display",
        error="DelayedError",
        link=("later.py", 7)
    )

    print("Doing some work...")
    Time.wait(1)

    print("Now displaying stored error:")
    Console.print(stored_error)


    # ============================================================
    # ERROR INSIDE LOOP
    # ============================================================

    print("\n=== ERROR INSIDE LOOP ===")

    for i in range(5):
        try:
            if i == 3:
                raise Error(
                    message=f"Loop failed at iteration {i}",
                    error="LoopError"
                )
            print(f"Loop iteration {i} OK")
        except Error as e:
            Console.print(e)
            break


    # ============================================================
    # ERROR AS RETURN VALUE (ANTI-PATTERN TEST)
    # ============================================================

    print("\n=== ERROR AS RETURN VALUE (ANTI-PATTERN) ===")

    def bad_function():
        return Error(
            message="Returned instead of raised",
            error="BadPractice"
        )

    result = bad_function()
    Console.print(result)

    print("\n(This should NOT stop execution, but is discouraged)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== ERROR MODULE DEMO COMPLETE ===")
    print("If all error messages displayed correctly, the Error module works as expected.")


if __name__ == "__main__":
    error_demo()
