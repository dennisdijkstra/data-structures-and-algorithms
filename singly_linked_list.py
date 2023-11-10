class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def get(self, index):
    if index < 0 or index >= self.size:
      return None
    
    current_node = self.head
    counter = 0

    while current_node != None and counter + 1 != index:
      counter += 1
      current_node = current_node.next

    return current_node

  def insert_head(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node

    self.size += 1
    return self.head

  def insert_tail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return
    
    current_node = self.head
    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node
    self.size += 1
    return current_node

  def insert(self, value, index):
    if index < 0 or index >= self.size:
      return None

    if index == 0:
      self.set_head(value)
      return
    
    new_node = Node(value)
    previous_node = self.get(index - 1) 

    if previous_node != None:
      new_node.next = previous_node.next
      previous_node.next = new_node
      self.size += 1
    else:
      print('Index not present')

  def remove_head(self):
    pass

  def remove_tail(self):
    pass

  def remove(self, index):
    pass

  def update(self, index, value):
    pass

  def print(self):
    current_node = self.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next