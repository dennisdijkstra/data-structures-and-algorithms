class Queue:  
  def __init__(self):  
    self.queue = list()

  def size(self):  
    return len(self.queue) 

  def add(self,value):  
    self.queue.insert(0, value)  

  def remove(self):
    if len(self.queue) > 0:
      return self.queue.pop()
    return ('Queue is empty')
  
  def peek(self):
    return self.queue[-1]
