from linear_search import linear_search

def test_linear_search():
  arr = [2, 3, 4, 10, 40]
  x = 10

  indexOfX = linear_search(arr, x)
  assert indexOfX == 3