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
      self.insert_head(value)
      return

    new_node = Node(value)
    prev_node = self.get(index - 1) 

    if prev_node != None:
      new_node.next = prev_node.next
      prev_node.next = new_node
      self.size += 1
    else:
      print('Index not present')

  def remove_head(self):
    if self.head == None:
        return

    self.size -= 1
    self.head = self.head.next

  def remove_tail(self):
    if self.head == None:
        return

    current_node = self.head
    while current_node.next.next:
      current_node = current_node.next

    self.size -= 1
    current_node.next = None

  def remove(self, index):
    if index < 0 or index >= self.size:
      return None

    if index == 0:
      self.remove_head()
      return

    if index == self.size - 1:
      self.remove_tail()
      return

    prev_node = self.get(index - 1)
    removed_node = prev_node.next
    prev_node.next = removed_node.next
    self.size -= 1

    return removed_node

  def update(self, index, value):
    found_node = self.get(index)

    if found_node:
      found_node.value = value
      return true

    return false

  def print(self):
    current_node = self.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next