Here is the Python code for the factorial function using a recursive approach:

def factorial(n):
    """
    Calculates the factorial of a given number using recursion.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

Recursive Approach:
The factorial function uses a recursive approach to calculate the factorial of a given number. The function works as follows:

1. The base case is when the input `n` is 0. In this case, the function returns 1, as the factorial of 0 is defined as 1.
2. For any other non-negative integer `n`, the function recursively calls itself with `n - 1` as the argument, and multiplies the result by `n`.
3. The recursion continues until the base case is reached (when `n` becomes 0), and the final result is calculated by multiplying all the intermediate results.

Complexity Analysis:
The time complexity of the recursive factorial function is O(n), where n is the input number. This is because the function calls itself n times, with each call performing a constant amount of work (the multiplication operation).

The space complexity of the recursive factorial function is also O(n), due to the recursive calls that are stored on the call stack. Each recursive call adds a new frame to the call stack, and the maximum depth of the call stack is equal to the value of n.