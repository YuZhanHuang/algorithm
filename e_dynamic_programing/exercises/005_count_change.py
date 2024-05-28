"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
write some code to calculate the number of ways to represent n cents.
"""


def count_change(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    # Write your code here!
    pass


# Driver code to test the above function
if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms), 10))
