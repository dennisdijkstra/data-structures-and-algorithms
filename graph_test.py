from graph import Graph

def test_graph_init():
  graph = Graph()

  print(graph)
  assert graph.graph == {}