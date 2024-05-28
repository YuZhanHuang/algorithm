"""
Python3 implementation QuickSort using Lomuto's partition
Scheme.
"""


def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

    return arr


def partition(arr, start, end):
    pivot = arr[end]
    next_index = start

    for i in range(start, len(arr) - 1):
        if arr[i] < pivot:
            arr[next_index], arr[i] = arr[i], arr[next_index]
            next_index += 1

    arr[next_index], arr[end] = arr[end], arr[next_index]

    return next_index


# Example usage
if __name__ == '__main__':
    lst = [8, 7, 6, 1, 0, 9, 2]
    n = len(lst)
    quick_sort(lst, 0, n - 1)
    print("Sorted array:", lst)
