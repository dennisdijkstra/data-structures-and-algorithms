from min_heap import MinHeap

def test_min_heap_init():
  heap = MinHeap()

  assert heap.heap == []

def test_min_heap_add():
  heap = MinHeap()

  heap.add(85)
  assert heap.peek() == 85

  heap.add(33)
  assert heap.peek() == 33

  heap.add(28)
  assert heap.peek() == 28

  heap.add(100)
  assert heap.peek() == 28

def test_min_heap_remove_from_empty_heap():
  heap = MinHeap()

  assert heap.remove() == None

def test_min_heap_remove():
  heap = MinHeap()

  heap.add(12)
  heap.add(5)
  heap.add(11)
  heap.add(44)
  heap.add(1)
  heap.remove()

  assert heap.peek() == 5

def test_min_heap_build():
  heap = MinHeap()
  heap.build([88, 4, 12, 99, 13, 50, 2, 1, 17])

  assert len(heap.heap) == 9
  assert heap.heap == [1, 4, 2, 17, 13, 50, 12, 99, 88]