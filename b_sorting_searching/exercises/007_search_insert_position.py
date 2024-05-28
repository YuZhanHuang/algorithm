"""
Search Position

Given a sorted list and a target value, return the index of the target value if the value is present in the list.
If the value is not present, return the index at which the value should be inserted.

You may assume that no duplicates are in the list.
"""


def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """
    left, right = 0, len(lst) - 1
    position = None
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return mid

        if lst[mid] < value:
            left = mid + 1
            position = mid + 1
        else:
            right = mid - 1
            position = mid

    return position


# Driver to test above code
if __name__ == '__main__':
    lst = [1, 3, 5, 6]

    value = 7
    print(search_insert_position(lst, value))

    value = 2
    print(search_insert_position(lst, value))

    value = 0
    print(search_insert_position(lst, value))
