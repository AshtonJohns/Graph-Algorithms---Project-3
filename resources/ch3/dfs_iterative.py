# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# An iterative DFS implementation 
# 
# -GRAPH: a dictionary of vertex and adjancent list
# -START: starting vertex for traversal
# -VISITED: a set of visited vertices 
#
def _dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        #print('The stack is:', stack)
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def main():
    # # Sample graphs
    # graph = {'A': set(['B', 'C', 'D', 'E']),
    #      'B': set(['A', 'C']),
    #      'C': set(['A', 'B', 'D', 'E']),
    #      'D': set(['A', 'C']),
    #      'E': set(['A', 'C']),
    #      }#'F': set()}

    # # Sample graph1
    # graph1 = {'A': set(['B', 'E']),
    #      'B': set(['A', 'C']),
    #      'C': set(['B', 'D', 'E']),
    #      'D': set(['C']),
    #      'E': set(['A', 'C'])}
    # # Sample graph2, disconnected
    graph2 = {'A': set(['B', 'C', 'D', 'E']),
         'B': set(['A', 'C']),
         'C': set(['A', 'B','E']),
         'D': set(['A']),
         'E': set(['A', 'C']),
	 'H': set(['I', 'J']),
         'I': set(['H', 'J']),
         'J': set(['H', 'I'])}

    v = _dfs(graph2, 'A')
    print(v)

if __name__ == '__main__':
    main()
