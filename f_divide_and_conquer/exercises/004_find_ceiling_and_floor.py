"""
You need to implement two functions in this challenge:
    1. find_floor(lst, low, high, x)
    2. find_ceiling(lst, low, high, x)

These function prototypes are identical to the binary search function.

> Note: We have already implemented the function find_floor_ceiling(lst, x) which is responsible for calling
> find_floor and find_ceiling.
"""


def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    position = None
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            position = mid
            break

        if lst[mid] < x:
            low = mid + 1
            position = mid + 1
        else:
            high = mid - 1
            position = mid

    if position == 0:
        return -1

    return lst[position - 1]


def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """
    position = None
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            position = mid
            break

        if lst[mid] < x:
            low = mid + 1
            position = mid + 1
        else:
            high = mid - 1
            position = mid

    if position == 0:
        return lst[1]
    elif position + 1 >= len(lst):
        return -1

    return lst[position]


def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)


# Driver code to test above function
if __name__ == '__main__':
    lst = [1, 2, 3, 5, 7]
    x = 4
    print("Floor and Ceil of ", x, ": ", find_floor_ceiling(lst, x))