def fib(num, lookup_table):
    """
    Finds nth fibonacci number
    :param num: An integer number
    :param lookup_table: Stores already calculated fibonacci number
    :return: nth fibonacci number
    """
    if lookup_table[num] == -1:
        if num <= 1:
            lookup_table[num] = num
        else:
            lookup_table[num] = fib(num - 1, lookup_table) + fib(num - 2, lookup_table)

    return lookup_table[num]


# Driver code to test above function
if __name__ == '__main__':
    num = 6  # Finding the nth Fibonacci number
    lookup_table = [-1] * (num + 1)  # Initializing the lookup table to have -1 of size num + 1
    print(fib(num, lookup_table))
