import pytest

from greeting import farewell, greet, shout


def test_greet() -> None:
    assert greet("CT") == "Hello, CT"


# AC-1: farewell returns the correct goodbye string


def test_farewell_normal_ac1() -> None:
    """farewell("Ada") returns "Goodbye, Ada"."""
    assert farewell("Ada") == "Goodbye, Ada"


def test_farewell_whitespace_name_ac1() -> None:
    """Whitespace-only name is accepted and embedded verbatim in the result."""
    assert farewell("  ") == "Goodbye,   "


def test_farewell_type_error_ac1() -> None:
    """farewell raises TypeError when name is not a str."""
    with pytest.raises(TypeError):
        farewell(123)  # type: ignore[arg-type]


def test_farewell_empty_raises_ac1() -> None:
    """farewell raises ValueError when name is an empty string."""
    with pytest.raises(ValueError):
        farewell("")


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
