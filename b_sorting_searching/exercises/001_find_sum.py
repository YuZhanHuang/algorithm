"""
Find Two Numbers That Add Up to "n"

In this problem, you have to implement the find_sum(lst, n) function which will take a list lst and number n as inputs
and return two numbers from the list that add up to n.

tags: sorting, searching
"""


# brute force
def find_sum_brute(lst, n):
    """
    Since we iterate over the entire list of n elements, the time complexity is O(n^2).
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n and i != j:
                return [lst[i], lst[j]]


# sorting the list
def binary_search(lst, item):
    """
    Binary Search helper function
    :param lst: A list of integers
    :param item: An item to be searched in the list
    """

    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if lst[mid] == item:
            found = mid
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def find_sum_with_binary_search(lst, n):
    """
    O(nlog(n))
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    lst.sort()
    for j in lst:
        index = binary_search(lst, n - j)
        if index:
            return [j, n - j]


# using a dictionary
def find_sum_by_dict(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = dict()

    for ele in lst:
        try:
            found_values[n - ele]  # noqa
            return [n - ele, ele]
        except:
            found_values[ele] = 0

    return False


# using the python set
def find_sum_by_set(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = set()

    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)

    return False


if __name__ == '__main__':
    print(find_sum_brute([1, 3, 2, 4], 6))
