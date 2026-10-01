import pytest

from greeting import greet, shout


def test_greet() -> None:
    assert greet("CT") == "Hello, CT"


def test_shout_mixed_case_ac1() -> None:
    assert shout("Ada") == "HELLO, ADA!"


def test_shout_already_upper_ac1() -> None:
    assert shout("ADA") == "HELLO, ADA!"


def test_shout_already_lower_ac1() -> None:
    assert shout("ada") == "HELLO, ADA!"


def test_shout_empty_string_ac1() -> None:
    with pytest.raises(ValueError):
        shout("")


def test_shout_non_string_int_ac1() -> None:
    with pytest.raises(TypeError):
        shout(42)  # type: ignore[arg-type]


def test_shout_non_string_none_ac1() -> None:
    with pytest.raises(TypeError):
        shout(None)  # type: ignore[arg-type]
