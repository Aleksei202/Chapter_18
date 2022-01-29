def partition(array, start, end):
    pivot = array[end] #my code
    low = start #my code
    high = end - 1 #my code

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp
        else:
            break

    array[end] = array[low] #my code
    array[low] = pivot #my code

    return low #my code


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
quick_sort(array, 0, len(array) - 1)
print(array)
