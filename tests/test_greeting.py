from greeting import greet


def test_greet() -> None:
    assert greet("CT") == "Hello, CT"
