"""
Suppose that you are given an array of contiguous integers starting from 1 to n, with one integer missing in the middle,
like so:

[1, 2, 3, 4, 6, 7, 8, 9, 10]
            ^
            |
            |
            5  Missing Number
"""


def missing_number(lst):
    """
    Finds a missing number from the list which contains sorted numbers from 1 to onwards
    :param lst: List of sorted integers
    :return: Missing number in the sorted list
    """

    # Write your code here!
    pass


# Driver code to test above function
if __name__ == '__main__':
    print(missing_number([1, 2, 4]))
    print(missing_number([1, 2, 3, 4, 6]))
    print(missing_number([2, 3, 4, 5, 6]))
    print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
