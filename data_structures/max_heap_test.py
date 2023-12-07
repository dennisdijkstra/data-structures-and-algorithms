from data_structures.max_heap import MaxHeap

def test_max_heap_init():
  heap = MaxHeap()

  assert heap.heap == []

def test_max_heap_add():
  heap = MaxHeap()

  heap.add(85)
  assert heap.peek() == 85

  heap.add(33)
  assert heap.peek() == 85

  heap.add(100)
  assert heap.peek() == 100

  heap.add(105)
  assert heap.peek() == 105

def test_max_heap_remove_from_empty_heap():
  heap = MaxHeap()

  assert heap.remove() == None

def test_max_heap_remove():
  heap = MaxHeap()

  heap.add(12)
  heap.add(5)
  heap.add(11)
  heap.add(44)
  heap.add(1)
  heap.remove()

  assert heap.peek() == 12

def test_max_heap_build():
  heap = MaxHeap()
  heap.build([88, 4, 12, 99, 13, 50, 2, 1, 17])

  assert len(heap.heap) == 9
  assert heap.heap == [99, 88, 50, 17, 13, 12, 2, 1, 4]