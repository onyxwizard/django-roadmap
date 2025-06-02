# calculator/operations.py

def add(a:float,b:float) -> float:
    """Returns the sum of two numbers"""
    return a+b

def subtract(a:float,b:float)-> float:
    """Returns the difference between two numbers"""
    return a-b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Returns the division of a by b. Raises ValueError if b is zero."""
    if b ==0:
        raise ValueError("Cannot divide by Zero")
    return a/b