def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if type(s) is not str:
        return -1  # optional safety

    return s[::-1]


# Task 2
print(string_reverse("Hello World"))  # expected: "dlroW olleH"
print(string_reverse("Python"))       # expected: "nohtyP"
