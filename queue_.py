class Queue:  
  def __init__(self):  
    self.queue = list()
    self.size = 0

  def size(self):  
    return len(self.queue) 

  def enqueue(self,value):
    self.queue.insert(0, value)
    self.size += 1

  def dequeue(self):
    if len(self.queue) > 0:
      self.size -= 1
      return self.queue.pop()

    return ('Queue is empty')
  
  def peek(self):
    return self.queue[-1]