from data_structures.heap import Heap

class MaxHeap(Heap):
  def __init__(self, comparator = lambda a,b: a > b):
    super().__init__(comparator)