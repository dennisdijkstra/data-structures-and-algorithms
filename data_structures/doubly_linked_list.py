class Node:
  def __init__(self, value):
    self.value = value 
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def get(self, index):
    if index < 0 or index > self.size:
      return None

    current_node = None
    counter = 0

    if index <= self.size / 2:
      current_node = self.head
      counter = 0

      while current_node != None and counter != index:
        current_node = current_node.next
        counter += 1
    else:
      current_node = self.tail
      counter = self.size - 1

      while current_node != None and counter != index:
        current_node = current_node.prev
        counter -= 1

    return current_node

  def insert_head(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node

    self.size += 1
    return self.head

  def insert_tail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

    self.size += 1
    return self.tail

  def insert(self, value, index):
    if index < 0 or index > self.size:
      return None

    if index == 0:
      self.insert_head(value)
      return

    if index == self.size:
      self.insert_tail(value)
      return

    new_node = Node(value)
    prev_node = self.get(index - 1)
    next_node = prev_node.next

    if prev_node != None and next_node != None:
      prev_node.next = new_node
      new_node.prev = prev_node
      new_node.next = next_node
      next_node.prev = new_node

    self.size += 1
    return new_node

  def remove_head(self):
    if self.head == None:
      return

    self.head = self.head.next
    self.head.prev = None
    self.size -= 1

  def remove_tail(self):
    if self.head == None:
      return
    
    current_node = self.tail
    self.tail = current_node.prev
    self.tail.next = None
    self.size -= 1

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

  def update(self, value, index):
    found_node = self.get(index)

    if found_node:
      found_node.value = value
      return True

    return False

  def print(self):
    current_node = self.head
    while current_node:
      print(current_node.value)
      current_node = current_node.next