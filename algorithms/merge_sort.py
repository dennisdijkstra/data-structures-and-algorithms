def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_index = len(array) // 2
    left_array = array[:mid_index]
    right_array = array[mid_index:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge(array, left_array, right_array)


def merge(array, left_array, right_array):
    left_index = right_index = main_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[main_index] = left_array[left_index]
            left_index += 1
        else:
            array[main_index] = right_array[right_index]
            right_index += 1

        main_index += 1

    while left_index < len(left_array):
        array[main_index] = left_array[left_index]
        left_index += 1
        main_index += 1

    while right_index < len(right_array):
        array[main_index] = right_array[right_index]
        right_index += 1
        main_index += 1
