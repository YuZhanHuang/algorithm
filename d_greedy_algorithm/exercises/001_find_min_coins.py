"""
Given an infinite number of quarters (25cents), dimes (10cents), nickels (5cents), and pennies (1cent),
implement a function to calculate the minimum number of coins to represent v cents.

Sample input
    v = 19
    available_coins = [1, 5, 10, 25]
The available coins are in the ascending order.

Sample output
    result = [10, 5, 1, 1, 1, 1]
"""


def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """
    n = len(coins_available)
    result = []
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])

    return result


# Main program to test the above code
if __name__ == "__main__":
    coins_available = [1, 5, 10, 25]  # The available coins are in increasing order
    print(find_min_coins(19, coins_available))
