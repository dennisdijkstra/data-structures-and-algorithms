from graph import Graph

def test_graph_init():
  graph = Graph()

  assert graph.size == 0
  assert graph.vertices == {}

def test_graph_add_vertex():
  graph = Graph()
  graph.add_vertex('A')
  graph.add_vertex('B')

  assert graph.size == 2

def test_graph_add_edge():
  graph = Graph()
  vertex_a = 'A'
  vertex_b = 'B'
  vertex_c = 'C'

  graph.add_vertex(vertex_a)
  graph.add_vertex(vertex_b)
  graph.add_vertex(vertex_c)
  graph.add_edge(vertex_a, vertex_b)
  graph.add_edge(vertex_a, vertex_c)

  assert len(graph.vertices[vertex_a]) == 2
  assert len(graph.vertices[vertex_b]) == 1
  assert len(graph.vertices[vertex_c]) == 1
  
def test_graph_remove_vertex():
  graph = Graph()

  vertex_a = 'A'
  vertex_b = 'B'
  vertex_c = 'C'
  graph.add_vertex(vertex_a)
  graph.add_vertex(vertex_b)
  graph.add_vertex(vertex_c)
  graph.add_edge(vertex_a, vertex_b)
  graph.add_edge(vertex_a, vertex_c)
  graph.remove_vertex(vertex_b)

  assert len(graph.vertices[vertex_a]) == 1
  assert len(graph.vertices[vertex_c]) == 1

def test_graph_remove_edge():
  graph = Graph()

  vertex_a = 'A'
  vertex_b = 'B'
  graph.add_vertex(vertex_a)
  graph.add_vertex(vertex_b)
  graph.add_edge(vertex_a, vertex_b)
  graph.remove_edge(vertex_a, vertex_b)

  assert len(graph.vertices[vertex_a]) == 0