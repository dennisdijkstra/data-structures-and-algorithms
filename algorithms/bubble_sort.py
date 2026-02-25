def bubble_sort(array):
    length = len(array)
    isSwapped = False

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                isSwapped = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not isSwapped:
            return
