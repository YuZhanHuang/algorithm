"""
In any given sorted list, the closest number to a given number is the one whose absolute difference
with the given number is closest to zero.

"""


def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """

    # Write your code here!
    pass


# Driver code to test above function
if __name__ == '__main__':
    print(find_closest([-9, -4, -2, 0, 1, 3, 4, 10], 5))
    print(find_closest([1, 2, 5, 10, 23, 25, 30, 50], 100))
