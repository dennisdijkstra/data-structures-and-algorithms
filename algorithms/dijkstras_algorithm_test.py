from dijkstras_algorithm import dijkstra
from data_structures.graph import Graph

def test_dijkstras_algorithm():
  graph = Graph()
  print(graph)
  vertices = ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Y']

  for vertex in vertices:
    graph.add_vertex(vertex)

  edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'Y', 2),
    ('H', 'G', 2),
    ('Y', 'G', 2),
    ('C', 'L', 2),
    ('L', 'I', 4),
    ('L', 'J', 1),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('K', 'Y', 5), 
  ]

  for edge in edges:
    graph.add_edge(*edge)

  result = dijkstra(graph, 'X', 'Y')
  assert result == ['X', 'B', 'H', 'G', 'Y']