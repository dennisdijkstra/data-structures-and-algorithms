def binary_search(array, x, low = 0, high = None):
  if high is None:
    high = len(array) - 1
    
  if low > high:
    return False
  
  mid = (high + low) // 2
  if array[mid] == x:
    return mid

  if array[mid] < x:
    return binary_search(array, x, low, mid - 1)

  return binary_search(array, x, mid + 1, high)