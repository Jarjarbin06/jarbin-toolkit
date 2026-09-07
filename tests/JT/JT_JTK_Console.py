from jarbin_toolkit_jartest import (
    JarTest,
    Get,
    Show,
    Assertion,
    Context,
    env,
    command,
    output
)

from jarbin_toolkit import Console


# ---------------------------------------------------------------------------
# Console
# ---------------------------------------------------------------------------

def JT_console_print():
    output, _ = Get.Redirect.stdout(
        Console.Console.print,
        "Hello",
        auto_reset=False,
        end=""
    )

    Assertion.eq(output, "Hello", "output is not valid")


def JT_text_formatting():
    Text = Console.Text.Text
    text = Text("hello")

    Assertion(
        isinstance(text.bold(), Text),
        "apply not returning type according to argument type"
    )
    Assertion(
        isinstance(text.underline().s, str),
        "property 'str' not working"
    )


def JT_progress_bar():
    pb = Console.Animation.ProgressBar(10)

    pb.update(5)
    rendered = pb.render()

    Assertion(
        isinstance(rendered, Console.Text.Text),
        "output is of the wrong type"
    )


def JT_cursor():
    Console.ANSI.Cursor.up(1)
    Console.ANSI.Cursor.down(1)
    Console.ANSI.Cursor.left(1)
    Console.ANSI.Cursor.right(1)

    Assertion(True)


def JT_line():
    Console.ANSI.Line.clear_line()
    Console.ANSI.Line.clear()

    Assertion(True)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Console = JarTest()
JTT_JTK_Console.fetch()
