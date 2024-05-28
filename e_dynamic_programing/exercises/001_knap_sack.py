"""
Let’s look at the 0/1 knapsack problem. Imagine that you’re a burglar at a jewelry store with a knapsack.
Your goal is to choose a combination of jewelry that results in the most profit.
Let’s see how you would code this problem.

Given two integer lists that represent the weights and profits of N items,
implement a function knap_sack() that finds a subset of these items which will give us the maximum profit,
so that their cumulative weight is not more than a given number capacity.
Each item can only be selected once, which means we either skip it or put it in the knapsack.
"""


# Solution1: brute force
# Solution2: top-down dynamic programming approach with memoization
# Solution3: bottom-up dynamic programming with tabulation
# Solution4: optimizing the tabulated version for space


def knap_sack_recursive(profits, profits_length, weights, current_index, capacity):
    if current_index >= profits_length or capacity < 0:
        return 0

    profits1 = 0
    if capacity >= weights[current_index]:
        profits1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights, current_index + 1,
                                                                capacity - weights[current_index])

    profits2 = knap_sack_recursive(profits, profits_length, weights, current_index + 1, capacity)

    return max(profits1, profits2)


def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each item
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """
    return knap_sack_recursive(profits, profits_length, weights, 0, capacity)


def knap_sack_memoization_recursive(lookup_table, profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_memoization_recursive(lookup_table, profits,
                                                                           profits_length, weights,
                                                                           capacity - weights[current_index],
                                                                           current_index + 1)

    profit2 = knap_sack_memoization_recursive(lookup_table, profits, profits_length,
                                              weights, capacity, current_index + 1)

    lookup_table[current_index][capacity] = max(profit1, profit2)
    return lookup_table[current_index][capacity]


def knap_sack_memoization(profits, profits_length, weights, capacity):
    table = [[0 for _ in range(capacity + 1)] for _ in range(profits_length + 1)]

    return knap_sack_memoization_recursive(table, profits, profits_length, weights, capacity, 0)


def knap_sack_tabulation_v1(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    # Basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [[0 for x in range(capacity + 1)] for _ in range(profits_length + 1)]

    # Building the lookup table in bottom up manner
    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif weights[i - 1] <= j:
                lookup_table[i][j] = max(profits[i - 1] + lookup_table[i - 1][j - weights[i - 1]],
                                         lookup_table[i - 1][j])
            else:
                lookup_table[i][j] = lookup_table[i - 1][j]

    return lookup_table[profits_length][capacity]


def knap_sack_tabulation_v2(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """
    # Basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [0 for x in range(capacity + 1)]
    # if we have only one weight, we will take it if it is not more than the
    # capacity
    for i in range(capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]

    # process all sub-lists for all the capacities
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):

            profit1 = 0

            # include the item, if it is not more than the capacity
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j - weights[i]]
            # exclude the item
            profit2 = lookup_table[j]

            # take maximum
            lookup_table[j] = max(profit1, profit2)

    return lookup_table[capacity]


if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, 4, weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, 4, weights, 6))
