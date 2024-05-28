"""
Edit distance is a metric to quantify how dissimilar two strings are to one another by counting the minimum number
of operations required to transform one string into the other.

Edit distances find several applications in the real world.
For example, it is used to figure out which word is misspelled in automatic spelling correction.
In bioinformatics, it’s used to quantify the similarity between two DNA sequences.

Different definitions of an edit distance use different sets of string operations to determine the ‘distance’.
The Levenshtein distance operations are the most famous: removal, insertion,
or substitution of a character in the string.
Levenshtein distance operations are what we will follow in this example.
"""


def min_edit_dist(str1, str2):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :return: minimum Levenshtein distance operations
    """

    # Write your code here!
    pass


# Driver code to test the above function
if __name__ == '__main__':
    str1 = "sunday"
    str2 = "saturday"

    print(min_edit_dist(str1, str2))
