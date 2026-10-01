import pytest

from greeting import farewell, greet

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
