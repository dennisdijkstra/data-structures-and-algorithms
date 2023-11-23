class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class BinaryTree:
  def __init__(self):
      self.root = None
      self.size = 0
  
  def insert(self, value):
    node = Node(value)

    if self.root is None:
      self.root = node
      self.size += 1
      return

    queue = [self.root]

    while queue:
      current_node = queue.pop(0)

      if current_node.left is None:
        current_node.left = node
        self.size += 1
        break
      else:
        queue.append(current_node.left)

      if current_node.right is None:
        current_node.right = node
        self.size += 1
        break
      else:
        queue.append(current_node.right)