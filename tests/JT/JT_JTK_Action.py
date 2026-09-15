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

from jarbin_toolkit import Action


# ---------------------------------------------------------------------------
# Action
# ---------------------------------------------------------------------------

def JT_action_call():
    called = {"v": False}

    def fn():
        called["v"] = True

    action = Action.Action("fn", fn)
    action()

    Assertion(called["v"] is True, "called[v] must be True")


def JT_action_repr():
    action = Action.Action("print 'hello'", print, "hello")

    Assertion.contain(repr(action), "Action", "invalid representation")


def JT_actions_container():
    result = []

    def add(x):
        result.append(x)

    actions = Action.Actions()

    actions += Action.Action("add 1", add, 1)
    actions += Action.Action("add 2", add, 2)

    Assertion.eq(len(actions), 2, "invalid number of actions")

    actions()

    Assertion.eq(result, [1, 2], "result is not equal to expected")


def JT_actions_getitem():
    actions = Action.Actions()
    action = Action.Action("print 'A'", print, "A")

    actions += action

    Assertion.eq(actions[0], action, "action not added")


def JT_action_kwargs():
    result = []

    def add(value, increment=0):
        result.append(value + increment)

    action = Action.Action(
        "add",
        add,
        10,
        increment=5
    )

    action()

    Assertion.eq(result, [15], "kwargs were not passed correctly")


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Action = JarTest()
JTT_JTK_Action.fetch()
