import pytest


from jarbin_toolkit_time import Time


def test_time_wait(
    ) -> None:
    elapsed = Time.wait(0.05)

    assert 0.05 < elapsed < 0.06

def test_time_wait_negative(
    ) -> None:
    elapsed = Time.wait(-1)

    assert 0 < elapsed < 0.01
