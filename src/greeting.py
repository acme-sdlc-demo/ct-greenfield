def greet(name: str) -> str:
    return f"Hello, {name}"


def shout(name: str) -> str:
    """Return an emphatic, upper-cased greeting for name."""
    if not isinstance(name, str):
        raise TypeError(f"name must be a str, got {name}")
    if name == "":
        raise ValueError("name must not be empty")
    return f"HELLO, {name.upper()}!"
