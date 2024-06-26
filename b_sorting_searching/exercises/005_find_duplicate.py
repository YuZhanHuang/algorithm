"""
Find Duplicates in a List With No Repetition

Given a list of integers, find all the duplicates that exist in that list.
"""
from collections import defaultdict


def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    seen = {}  # A dictionary to store already observed elements

    for x in lst:  # traverse the list
        if x not in seen:  # if element is not already iterated
            seen[x] = 1  # put 1 at that index in seen
        else:
            if seen[x] == 1:  # if that element is iterated and already present in dictionary
                result.append(x)  # add that element in the dupes
            seen[x] += 1  # increment the dictionary value by 1

    return result


# Driver to test above code
if __name__ == '__main__':
    lst = [1, 2, 5, 1, 4, 2, 1, 1]

    print(find_duplicates(lst))
