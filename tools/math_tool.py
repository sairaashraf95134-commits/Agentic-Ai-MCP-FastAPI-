def add(
        a: int,
        b: int
):
    """
    Add two numbers
    """

    return a + b


def subtract(
        a: int,
        b: int
):
    """
    Subtract two numbers
    """

    return a - b


def multiply(
        a: int,
        b: int
):
    """
    Multiply two numbers
    """

    return a * b


def divide(
        a: int,
        b: int
):
    """
    Divide two numbers
    """

    if b == 0:
        return "Cannot divide by zero"

    return a / b