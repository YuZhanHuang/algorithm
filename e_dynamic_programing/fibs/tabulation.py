def fib_v1(num, lookup_table):
    """
    Finds nth fibonacci number
    :param num: An integer number
    :param lookup_table: Stores already calculated fibonacci number
    :return: nth fibonacci number
    """
    # Set 0th and first values
    lookup_table[0] = 0
    lookup_table[1] = 1

    for i in range(2, num + 1):
        # Fill up the table by summing up previous two values
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2]

    return lookup_table[num]  # Return the nth Fibonacci number


def fib_v2(num):
    """
    Finds nth fibonacci number
    :param num: An integer number
    :return: nth fibonacci number
    """
    # Base Case
    if num <= 1:
        return num

    second_last = 0  # The 0th
    last = 1  # The first
    current = 0

    #     0,      1,      1,      2,      3,      5,      8,     13,      21,    34
    # fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6), fib(7), fib(8), fib(0)
    for i in range(2, num + 1):
        # current is the sum of the last plus second last number before the current one
        print(f'fib({i}) = fib({i-1}) + fib({i-2}) = {last} + {second_last} = {last + second_last}')
        current, second_last = second_last + last, last
        print(f'second last become last: {second_last}')
        last = current
        print(f'last become current: {last}')
        print('----' * 10)

    return current


# Driver code to test above function
if __name__ == '__main__':
    num = 8
    print(fib_v2(num))
