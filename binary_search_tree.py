class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0
    
  def insert(self, value):
    new_node = Node(value)
    
    if self.root is None:
      self.root = new_node
      self.size += 1
      return
    
    current_node = self.root
    while current_node:
      if value == current_node.value:
        return
      
      if value < current_node.value:
        if current_node.left:
          current_node = current_node.left
          continue
        else:
          current_node.left = new_node
          self.size += 1
          break
      else:
        if current_node.right:
          current_node = current_node.right
          continue
        else:
          current_node.right = new_node
          self.size += 1
          break  
  
  def find(self, value):
    if self.root is None:
      return None
    
    current_node = self.root
    
    while current_node:
      if current_node.value == value:
          return current_node
        
      if value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
  
  def find_min(self):
    current_node = self.root
    while current_node.left:
        current_node = current_node.left

    return current_node
  
  def find_max(self):
    current_node = self.root
    while current_node.right:
        current_node = current_node.right

    return current_node
  
  def remove(self):
    pass
  
  def contains(self):
    pass

  def pre_order(self):
    pass

  def in_order(self):
    pass

  def post_order(self):
    pass