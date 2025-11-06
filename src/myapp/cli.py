"""Simple CLI functions for myapp."""

def greet(name: str) -> str:
    """Return a greeting for name.

    Args:
        name: person's name

    Returns:
        Greeting string
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"


def main() -> None:
    """Simple command-line entrypoint."""
    import sys

    name = " ".join(sys.argv[1:]).strip()
    print(greet(name))


if __name__ == "__main__":
    main()
