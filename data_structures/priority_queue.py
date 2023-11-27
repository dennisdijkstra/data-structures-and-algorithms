from max_heap import MaxHeap 

class PriorityQueue:
  def __init__(self):
    self.heap = MaxHeap(lambda a,b: a['priority'] > b['priority'])
    self.size = 0

  def enqueue(self, value):
    self.heap.add(value)
    self.size += 1

  def dequeue(self):
    self.heap.remove()
    self.size -= 1

  def peek(self):
    return self.heap.peek()