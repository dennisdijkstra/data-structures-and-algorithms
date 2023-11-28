class Graph:
  def __init__(self):
    self.vertices = {}
    self.size = 0
    
  def get_vertex(self, key):
    return self.vertices[key]

  def add_vertex(self, vertex):
    if vertex not in self.vertices:
      self.vertices[vertex] = []
      self.size += 1

  def remove_vertex(self, vertex):
    if self.vertices[vertex] is None:
      return None

    for key in self.vertices:
      self.remove_edge(key, vertex)

    del self.vertices[vertex]
    self.size -= 1

  def add_edge(self, from_vertex, to_vertex):
    self.vertices[from_vertex].append(to_vertex)
    self.vertices[to_vertex].append(from_vertex)

  def remove_edge(self, from_vertex, to_vertex):
    if to_vertex in self.vertices[from_vertex]:
      self.vertices[from_vertex].remove(to_vertex)

    if from_vertex in self.vertices[to_vertex]:
      self.vertices[to_vertex].remove(from_vertex)