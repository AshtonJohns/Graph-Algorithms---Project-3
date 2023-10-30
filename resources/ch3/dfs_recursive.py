# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# The DFS function is a recursive implementation of
# the Depth-First-Search algorithm
# 
# -GRAPH: a dictionary of vertex and sdjancent list
# -START: starting vertex for traversal
# -VISITED: a set of visited vertices 
#

def dfs(graph, start, visited=None):
    
    # Tracking total number of recursive calls
    global t 
    t += 1
    print('DSF called ', t, 'times.')

    # Initialization with empty set
    if visited is None:
        visited = set() 

    # Mark start visited and add it to visited
    visited.add(start)

    # For key in adjancency list set of start but
    # not yet visited visit the key
 
    for key in graph[start] - visited: # Python suports set subtraction       
        dfs(graph, key, visited) # DFS recursive call
    return visited

# Sample graph
graph = {'A': set(['B', 'C', 'D', 'E']),
         'B': set(['A', 'C']),
         'C': set(['A', 'B', 'D', 'E']),
         'D': set(['A', 'C']),
         'E': set(['A', 'C'])}

t = 0
v = dfs(graph, 'A')
print(v)

