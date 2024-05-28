"""
Find the Maximum Product of Two Integers in a List

Implement a function find_max_prod(lst) that takes a list of numbers and returns a maximum product pair.
"""

from decimal import Decimal


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """
    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('Infinity')

    for n in lst:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n

        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n

    if max1 * max2 > min1 * min2:
        return max2, max1

    return min2, min1


# Driver to test above code
if __name__ == '__main__':
    lst = [1, 3, 5, 2, 6]
    print(lst)
    num1, num2 = find_max_prod(lst)
    print(num1, num2)

    lst = [1, -3, -5, 2, 6]
    print(lst)
    num1, num2 = find_max_prod(lst)
    print(num1, num2)

    lst = [1, 3, 5, 2, 6]
    print(lst)
    n1, n2 = find_max_prod([1, 3, 5, 2, 6])
    print(n1, n2)
