def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []
    pivot = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > pivot:
            right.append(lst[i])
        else:
            left.append(lst[i])

    left_result = quick_sort(left)
    p = [pivot]
    right_result = quick_sort(right)

    return left_result + p + right_result


if __name__ == '__main__':
    arr = [50, 90, 70, 20, 10, 30, 40, 60, 80]
    print('original', arr)
    sorted_arr = quick_sort(arr)
    print('sorted', sorted_arr)
