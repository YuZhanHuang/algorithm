"""
Given two strings, s1 and s2,
write a function that finds and returns the length of the longest substring of s2 in s1 (if any exists).
"""


def longest_common_substr_length_recursive(s1, s2, i1, i2, count, max_count):
    """
    Finds a longest common substring length
    :param lookup_table: Lookup Table
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """
    if i1 == len(s1) or i2 == len(s2):
        return max(count, max_count)

    if s1[i1] == s2[i2]:
        max_count = longest_common_substr_length_recursive(s1, s2, i1 + 1, i2 + 1, count + 1, max_count)

    max_count = max(max_count, count)

    c1 = longest_common_substr_length_recursive(s1, s2, i1, i2 + 1, 0, max_count)
    c2 = longest_common_substr_length_recursive(s1, s2, i1 + 1, i2, 0, max_count)

    return max(max_count, max(c1, c2))


def longest_common_substr_length(s1, s2):
    return longest_common_substr_length_recursive(s1, s2, 0, 0, 0, 0)


def memoization_helper(s1, s2, i1, i2, count, table):
    # Base Case
    if i1 == len(s1) or i2 == len(s2):
        return count

    if table[i1][i2][count] == -1:
        c1 = count

        if s1[i1] == s2[i2]:
            c1 = memoization_helper(s1, s2, i1 + 1, i2 + 1, count + 1, table)

        c2 = memoization_helper(s1, s2, i1, i2 + 1, 0, table)
        c3 = memoization_helper(s1, s2, i1 + 1, i2, 0, table)
        table[i1][i2][count] = max(c1, max(c2, c3))

    return table[i1][i2][count]


def longest_common_substr_length_memoization(s1, s2):
    max_len = max(len(s1), len(s2))
    table = [[[-1 for _ in range(len(s1))] for _ in range(len(s2))] for _ in range(max_len)]

    return memoization_helper(s1, s2, 0, 0, 0, table)


def longest_common_substr_length_v1(s1, s2):
    lookup_table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    max_length = 0
    for i in range(len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
                max_length = max(max_length, lookup_table[i][j])

    return max_length


# Driver code to test the above function
if __name__ == '__main__':
    # S1 = "0abc321"
    # S2 = "123abcdef"
    # print('S1 is', S1, 'S2 is', S2, longest_common_substr_length(S1, S2))

    # FIXME 下面的字串就會無限迴圈了，不知道為什麼？
    S1 = "educative./"
    S2 = "educative.aa"
    print('S1', S1, 'S2', S2, longest_common_substr_length(S1, S2))
