def printPascal(test_var):
    # Base Case
    if test_var == 0:
        return [1]

    else:
        line = [1]

        # Recursive Case
        previousLine = printPascal(test_var - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])
        line += [1]
    return line


# Driver Code
if __name__ == '__main__':
    print(printPascal(5))
