def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    
    # Performance test
    assert factorial(100) == math.factorial(100)

if __name__ == "__main__":
    test_factorial()
    print("All test cases passed!")