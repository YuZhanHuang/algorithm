"""
Arrange a Binary List

Implement a function sort_binary_list(lst) that takes a binary list of numbers and returns a sorted list.
"""


def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    j = 0

    for i in range(len(lst)):
        if lst[i] < 1:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1

    return lst


# Driver to test above code
if __name__ == '__main__':
    lst = [1, 0, 1, 0, 1, 0, 1, 0]
    result = sort_binary_list(lst)

    print(result)
