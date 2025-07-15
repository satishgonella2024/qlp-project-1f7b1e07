def factorial(n):
    """
    Calculates the factorial of a given number using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of the given number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)