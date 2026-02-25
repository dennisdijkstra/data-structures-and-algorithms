from binary_search import binary_search


def test_binary_search():
    array = [2, 3, 4, 10, 40]
    x = 10

    indexOfX = binary_search(array, x, 0, len(array) - 1)
    assert indexOfX == 3
