def decimalToBinary(test_var):
    # Base Case
    if test_var <= 1:
        return str(test_var)

    # Recursive Case
    else:
        return decimalToBinary(test_var // 2) + decimalToBinary(test_var % 2)  # Floor division - 
        # division that results into whole number adjusted to the left in the number line


# Driver Code
if __name__ == '__main__':
    print(decimalToBinary(11))
