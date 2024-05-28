"""
Search in a 2D List

Implement a function that tells whether a given number is present in a row-wise and column wise sorted 2D list or not.
"""


def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """
    if not lst:
        return False

    rows = len(lst)
    cols = len(lst[0])

    if cols == 0:
        return False

    i, j = 0, rows - 1

    if rows > 1:
        mid = None
        while i <= j:
            mid = i + (j - i) // 2

            if lst[mid][cols - 1] == number:
                return True

            if lst[mid][cols - 1] < number:
                i = mid + 1
            else:
                j = mid - 1

        if lst[mid][cols - 1] < number:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0

    if rows >= len(lst):
        return False

    i, j = 0, cols - 1

    while i <= j:
        mid = i + (j - i) // 2

        if lst[rows][mid] == number:
            return True

        if lst[rows][mid] < number:
            i = mid + 1
        else:
            j = mid - 1

    return False


# Driver to test above code
if __name__ == '__main__':
    lst = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]
    ]

    # Example 1
    print(find_in(lst, 30))

    # Example 2
    print(find_in(lst, 100))
