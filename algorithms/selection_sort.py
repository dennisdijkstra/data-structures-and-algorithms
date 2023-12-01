def selection_sort(array):
  lenght = len(array)

  for i in range(lenght-1):
    min = i
    for j in range(i + 1, lenght):
      if array[min] > array[j]:
        min = j

    array[i], array[min] = array[min], array[i]