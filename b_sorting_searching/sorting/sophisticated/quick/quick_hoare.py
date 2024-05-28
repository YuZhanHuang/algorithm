def partition(arr, start, end):
    """

    :param arr:
    :param start:
    :param end:
    :return:
    """
    left = start + 1  # 找到大於pivot
    right = end  # 找到小於pivot
    pivot = arr[start]

    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    return right


def quick_sort(lst, left, right):
    """
    Quick sort function
    :param lst: lst of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    if left < right:
        pi = partition(lst, left, right)
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)


# Driver code to test above
if __name__ == '__main__':
    lst = [5, 4, 2, 1, 3]
    quick_sort(lst, 0, len(lst) - 1)

    # Printing Sorted list
    print("Sorted list: ", lst)
