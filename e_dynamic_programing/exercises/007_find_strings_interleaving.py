"""
Given three strings `m`, `n`, and `p`, write a function to find out if `p` has been formed by interleaving `m` and `n`.
`p` should be considered to be an interleaved form of `m` and `n`,
if it contains all the letters from m and n in a preserved order.

"""


def find_strings_interleaving(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :return: True if the strings are interleaving, otherwise False
    """

    # Write your code here!
    pass


# Driver code to test the above function
if __name__ == '__main__':
    print(find_strings_interleaving("abd", "cef", "adcbef"))
    print(find_strings_interleaving("abc", "def", "abdccf"))
    print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))
