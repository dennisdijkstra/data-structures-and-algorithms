from binary_search import binary_search

def test_binary_search():
  arr = [2, 3, 4, 10, 40]
  x = 10

  indexOfX = binary_search(arr, x, 0, len(arr) - 1)
  assert indexOfX == 3