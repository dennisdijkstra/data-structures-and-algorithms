def dijkstra(graph, start, end):
  shortest_paths = {
    start: (None, 0)
  }
  current_node = start
  visited = set()

  while current_node != end:
    visited.add(current_node)
    destinations = graph.vertices[current_node]
    weight_to_current_node = shortest_paths[current_node][1]

    for next_node in destinations:
      weight = graph.weights[(current_node, next_node)] + weight_to_current_node
      if next_node not in shortest_paths:
          shortest_paths[next_node] = (current_node, weight)
      else:
        current_shortest_weight = shortest_paths[next_node][1]
        if current_shortest_weight > weight:
          shortest_paths[next_node] = (current_node, weight)
      
    next_destinations = { node: shortest_paths[node] for node in shortest_paths if node not in visited }
    if not next_destinations:
      return False

    current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
  
  path = []
  while current_node is not None:
    path.append(current_node)
    next_node = shortest_paths[current_node][0]
    current_node = next_node

  path = path[::-1]
  return path