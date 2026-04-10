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
