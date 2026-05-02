def greet(name: str = "World") -> str:
    """
    A simple function that returns a greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet())
