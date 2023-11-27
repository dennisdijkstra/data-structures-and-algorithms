from graph import Graph

def test_graph_init():
  graph = Graph()

  assert graph.size == 0
  assert graph.graph == {}

def test_graph_add_node():
  graph = Graph()
  graph.add_node('A')
  graph.add_node('B')

  assert graph.size == 2

def test_graph_add_edge():
  graph = Graph()
  node_a = 'A'
  node_b = 'B'
  node_c = 'C'

  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_edge(node_a, node_b)
  graph.add_edge(node_a, node_c)

  assert len(graph.graph[node_a]) == 2
  assert len(graph.graph[node_b]) == 1
  assert len(graph.graph[node_c]) == 1
  
def test_graph_remove_node():
  graph = Graph()

  node_a = 'A'
  node_b = 'B'
  node_c = 'C'
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_edge(node_a, node_b)
  graph.add_edge(node_a, node_c)
  graph.remove_node(node_b)

  assert len(graph.graph[node_a]) == 1
  assert len(graph.graph[node_c]) == 1

def test_graph_remove_edge():
  graph = Graph()

  node_a = 'A'
  node_b = 'B'
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_edge(node_a, node_b)
  graph.remove_edge(node_a, node_b)

  assert len(graph.graph[node_a]) == 0