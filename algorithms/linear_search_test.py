from linear_search import linear_search

def test_linear_search():
  array = [2, 3, 4, 10, 40]
  x = 10

  indexOfX = linear_search(array, x)
  assert indexOfX == 3

def test_linear_search_non_existing():
  array = [2, 3, 4, 10, 40]
  x = 55

  indexOfX = linear_search(array, x)
  assert indexOfX == -1