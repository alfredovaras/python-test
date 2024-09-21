def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    """
    >>> division(10, 0)
    Traceback (most recent call last):
    ValueError: Can't divide by zero
    """
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b
