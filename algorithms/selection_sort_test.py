from selection_sort import selection_sort


def test_selection_sort():
    array = [5, 1, 32, 67, 3, 99, 23, 127]

    selection_sort(array)
    assert array == [1, 3, 5, 23, 32, 67, 99, 127]
