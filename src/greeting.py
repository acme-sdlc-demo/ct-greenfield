def greet(name: str) -> str:
    return f"Hello, {name}"


def farewell(name: str) -> str:
    """Return a farewell string for the given name."""
    if not isinstance(name, str):
        raise TypeError(f"name must be a str, got {name!r}")
    if name == "":
        raise ValueError("name must not be empty")
    return f"Goodbye, {name}"
