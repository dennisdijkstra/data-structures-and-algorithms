from max_heap import MaxHeap 

class PriorityQueue:
  def __init__(self):
    self.heap = MaxHeap(lambda a,b: a['priority'] > b['priority'])

  def enqueue(self, value):
    self.heap.add(value)

  def dequeue(self):
    self.heap.remove()

  def peek(self):
    return self.heap.peek()