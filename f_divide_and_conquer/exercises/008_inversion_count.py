"""
Inversion count represents how far or close a list is from being sorted.
If a list is sorted, the inversion count will be 0.
But if it’s sorted in the reverse order, the inversion count will be maximum.

Consider indices i and j, such that i < j and lst[i] > lst[j], then there is an inversion in the list.
"""


def inversion_count(lst):
    """
    Function to find Inversion Count
    :param lst: List of integers
    :return: The inversion count of the list
    """

    # Write your code here!
    pass


# Driver code to test above functions
if __name__ == '__main__':
    lst = [3, 8, 2, 7, 5, 6]
    n = len(lst)
    result = inversion_count(lst, n)
    print("Number of inversions are", result)
