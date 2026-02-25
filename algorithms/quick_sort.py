def quick_sort(array, start_index, end_index):
    if start_index < end_index:
        pivot_index = partition(array, start_index, end_index)

        quick_sort(array, start_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end_index)


def partition(array, start_index, end_index):
    pivot = array[end_index]
    pivot_index = start_index

    for i in range(start_index, end_index):
        if array[i] <= pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1

    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]

    return pivot_index
