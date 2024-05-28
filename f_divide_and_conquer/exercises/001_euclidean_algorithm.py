"""
The Euclidean algorithm is a technique used to compute the greatest common divisor (GCD) of two numbers,
i.e., the largest number that divides both of them without leaving a remainder.
"""


def euclidean_algorithm(x, y):
    """
    Finds the euclidean of two numbers
    :param x: First number
    :param y: Second number
    :return: Returns the euclidean of two given numbers i.e. x and y
    """
    if x == 0:
        return y
    print('x', x, '|', 'y', y, '|', 'y % x =', y % x)
    return euclidean_algorithm(y % x, x)


# Driver code to test above function
if __name__ == '__main__':
    num1 = 1071
    num2 = 462

    result = euclidean_algorithm(num1, num2)
    print('The GCD of ', num1, 'and ', num2, 'is ', result)
