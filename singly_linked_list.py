class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def set_head(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node

    self.size += 1
    return self.head
      
  def set_tail(self, value):
    pass

  def insert(self, index):
    pass

  def remove(self, index):
    pass

  def get(self, index):
    pass

  def length(self):
    pass




