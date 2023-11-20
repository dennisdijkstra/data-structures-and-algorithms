class Graph:
  def __init__(self):
    self.graph = {}
    self.size = 0
    
  def get_edges(self):
    pass

  def add_node(self, node):
    if node not in self.graph:
      self.graph[node] = []
      self.size += 1

  def remove_node(self, node):
    if self.graph[node] is None:
      return None

    for key in self.graph:
      self.remove_edge(key, node)

    del self.graph[node]
    self.size -= 1

  def add_edge(self, from_node, to_node):
    self.graph[from_node].append(to_node)
    self.graph[to_node].append(from_node)

  def remove_edge(self, from_node, to_node):
    if to_node in self.graph[from_node]:
      self.graph[from_node].remove(to_node)

    if from_node in self.graph[to_node]:
      self.graph[to_node].remove(from_node)