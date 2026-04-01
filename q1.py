def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Validate numeric inputs (exclude bool)
    if type(x) not in (int, float) or type(y) not in (int, float):
        return -1

    # Swap using only x and y (no temp variable)
    x, y = y, x
    print(f"x = {x}, y = {y}")
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
print(swap("Apple", 10))  # expected: -1
print(swap(9, 17))        # expected: prints x = 17, y = 9 and returns (17, 9)
