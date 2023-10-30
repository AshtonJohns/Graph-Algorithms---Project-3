# Python implementation of Dijkstra's algorithm
#https://gist.github.com/econchick/4666413

import collections

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
                                        
def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

def main():
    graph = Graph()
    ''' The sample graph is on page 111 of printed text (p116 ebook)
           B-----D
         /||\   /| 
       A  || \ / |
        \ ||  \  | 
         \|| / \ | 
           C ----E
    '''
    graph.nodes = {'A','B','C','D','E'}
    graph.edges = {'A': ['B', 'C'], 'B':['C', 'D', 'E'], \
                'C':['B', 'D', 'E'], 'D':['B', 'C', 'E'],\
                'E': ['B', 'C', 'D']}
    graph.distance = {('A', 'B'):4, ('A', 'C'):2, ('B', 'C'):3,\
                  ('C', 'B'):1, ('B', 'D'):2, ('D', 'B'):2,\
                  ('B', 'E'):3, ('E', 'B'):3, ('C', 'D'):4,\
                  ('D', 'C'):4, ('C', 'E'):5, ('E', 'C'):5,\
                  ('D', 'E'):1, ('E', 'D'):1,
                   }

    v, path = dijkstra(graph, 'A')
    print('Visited: ', v)
    print('Path :', path)

if __name__ == "__main__":
    main()
