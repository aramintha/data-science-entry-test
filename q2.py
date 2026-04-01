def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # Approach:
    # 1) Validate that lst is a list.
    # 2) Loop through indices so we can replace items in-place.
    # 3) Replace every occurrence of find_val with replace_val and return the list.

    if type(lst) is not list:
        return -1

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
