from bubble_sort import bubble_sort


def test_bubble_sort():
    array = [5, 1, 32, 67, 3, 99, 23, 127]

    bubble_sort(array)
    assert array == [1, 3, 5, 23, 32, 67, 99, 127]
