Here's a Python function to calculate the factorial of a number using a recursive approach:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)