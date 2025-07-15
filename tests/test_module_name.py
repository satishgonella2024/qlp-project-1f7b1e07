Here are some test cases for the factorial function in Python:

def test_factorial_small_numbers():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_large_numbers():
    assert factorial(20) == 2432902008176640000
    assert factorial(30) == 265252859812191058636308480000000

def test_factorial_edge_cases():
    assert factorial(-1) == 1  # Factorial of negative numbers is 1
    assert factorial(1.5) == 1  # Factorial of non-integers is 1
    assert factorial(0.0) == 1  # Factorial of 0.0 is 1

def factorial(n):
    if n < 0:
        return 1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

The test cases cover the following scenarios:

1. Small numbers (0, 1, 5, 10) to ensure the function works correctly for small inputs.
2. Large numbers (20, 30) to ensure the function can handle large inputs without overflow errors.
3. Edge cases:
   - Negative numbers (-1) to ensure the function returns 1 for negative inputs.
   - Non-integer inputs (1.5) to ensure the function returns 1 for non-integer inputs.
   - 0.0 to ensure the function returns 1 for 0.0 input.

These test cases should help ensure that the factorial function handles small, large, and edge cases correctly.