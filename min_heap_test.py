from min_heap import MinHeap

def test_graph_init():
  min_heap = MinHeap()

  assert min_heap.heap == []
  assert min_heap.size == 0