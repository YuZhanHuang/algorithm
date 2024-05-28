"""
A girl lost the key to her locker (note: The key is only numeric).
She remembers the number of digits N as well as the sum S of all the digits of her password.
She also knows that her password is the largest number of N digits that can be possible with a given sum S.

Implement a function that would help her retrieve her key.
"""


def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    # Write your code here!
    pass


# Driver code to test above function
if __name__ == '__main__':
    sum_of_digits = 20
    number_of_digits = 3

    print(find_largest_number(number_of_digits, sum_of_digits))

    sum_of_digits = 100
    number_of_digits = 2

    print(find_largest_number(number_of_digits, sum_of_digits))
