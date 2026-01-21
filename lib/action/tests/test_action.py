import pytest


from jarbin_toolkit_action import Action, Actions


def test_action_valid_construction(
    ) -> None:
    def sample(x, y): return x + y
    act = Action("sum", sample, 3, 4)

    assert act.name == "sum"
    assert act.function is sample
    assert act.args == [3, 4]
    assert act.kwargs == {}


def test_action_str():
    def sample(x, y): return x + y
    act = Action("sum", sample, 3, 4)

    assert str(act) == "\'sum\' : sample(*args = [3, 4], **kwargs = {})"


def test_action_repr():
    def sample(x, y): return x + y
    act = Action("sum", sample, 3, 4)

    assert repr(act) == "Action(\'sum\', function=sample, args=[3, 4], kwargs={})"


def test_action_execution(
    ) -> None:
    def mul(x : int, y : int) -> int: return x * y
    act = Action("multiply", mul, 3, 5)
    result = act()
    assert result == 15


def test_actions_add_action():
    a1 = Action("a", lambda: None)
    a2 = Action("b", lambda: None)

    actions = a1 + a2

    assert len(actions) == 2
    assert actions[1] is a2


def test_actions_add_actions():
    a1 = Action("a", lambda: None)
    a2 = Action("b", lambda: None)
    a3 = Action("c", lambda: None)
    a4 = Action("d", lambda: None)

    actions1 = a1 + a2
    actions2 = a3 + a4
    actions3 = actions1 + actions2

    assert len(actions1) == 2
    assert actions1[1] is a2
    assert len(actions2) == 2
    assert actions2[0] is a3
    assert len(actions3) == 4
    assert actions3[3] is a4


def test_actions_add_invalid():
    a1 = Action("a", lambda: None)
    a2 = Action("b", lambda: None)

    actions1 = a1 + a2
    actions2 = 5
    actions3 = actions1 + actions2

    assert len(actions1) == 2
    assert actions1[1] is a2
    assert len(actions3) == 0


def test_actions_is_iterable():
    a1 = Action("a", lambda: 1)
    a2 = Action("b", lambda: 2)
    actions = Actions([a1, a2])

    collected = [act.name for act in list(actions.actions)]
    assert collected == ["a", "b"]


def test_actions_str():
    def sample(x, y): return x + y
    a1 = Action("a", sample, 3, 5)
    a2 = Action("b", sample, 5, 3)
    actions = Actions([a1, a2])

    assert str(actions) == "1 :\n    name = \'a\'\n    function = sample\n    args = [3, 5]\n    kwargs = {}\n\n2 :\n    name = \'b\'\n    function = sample\n    args = [5, 3]\n    kwargs = {}"


def test_actions_repr():
    def sample(x, y): return x + y
    a1 = Action("sum", sample, 3, 4)
    a2 = Action("sum", sample, 3, 4)

    actions = a1 + a2

    assert repr(actions) == "Actions([Action(\'sum\', function=sample, args=[3, 4], kwargs={}), Action(\'sum\', function=sample, args=[3, 4], kwargs={})])"


def test_actions_index_access():
    a1 = Action("a", lambda: 10)
    actions = Actions(a1)

    assert actions[0] is a1


def test_actions_len():
    a1 = Action("a", lambda: None)
    a2 = Action("b", lambda: None)
    a3 = Action("c", lambda: None)

    actions = Actions([a1, a2, a3])
    assert len(actions) == 3


def test_actions_add_action_method():
    a1 = Action("a", lambda: None)
    a2 = Action("b", lambda: None)

    actions = Actions(a1)
    actions += a2

    assert len(actions) == 2
    assert actions[1] is a2


def test_actions_execute_all(monkeypatch):
    calls = []

    def f1(): calls.append("f1")
    def f2(): calls.append("f2")

    a1 = Action("first", f1)
    a2 = Action("second", f2)

    actions = Actions([a1, a2])

    # simulate an "execute_all" helper if it exists.
    # If you don't have one yet, I can generate it for you.
    actions()

    assert calls == ["f1", "f2"]
