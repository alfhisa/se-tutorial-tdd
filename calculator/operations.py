def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
    pass


def multiply(a, b):
    return a * b
    pass


def divide(a, b):
    if(b == 0):
        raise ValueError("Cannot divide by zero")
    return a / b
    pass
