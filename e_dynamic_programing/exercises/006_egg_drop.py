"""
Given a tall skyscraper and a few eggs, write a function to figure out how many tries it would take to
find which floor of the skyscraper from which the eggs can be safely dropped without breaking.

Here are some rules:
    1. An egg that survives a fall can be used again. A broken egg must be discarded
    2. The effect of a fall is the same for all eggs
    3. If an egg breaks when dropped, then, it would break if dropped from a higher floor
    4. If an egg survives a fall, then it would survive a shorter fall
"""


def egg_drop(eggs, floors):
    """
    Figures out which floor of the skyscraper that the eggs can be safely dropped from without breaking.
    :param eggs: Number of stories of the skyscraper
    :param floors: Number of eggs
    :return: Return the floor
    """

    # Write your code here!
    pass


# Driver code to test the above function
if __name__ == '__main__':
    print(egg_drop(2, 13))
