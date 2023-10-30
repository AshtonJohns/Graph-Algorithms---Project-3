# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Sample 1
'''graph = {'A': set(['B', 'C', 'D', 'E']),
         'B': set(['A', 'C']),
         'C': set(['A', 'B', 'D', 'E']),
         'D': set(['A', 'C']),
         'E': set(['A', 'C'])}

u = list(dfs_paths(graph, 'A', 'E'))
print(u)
'''

def main():
    # Sample 2
    graph1 = {'A': set(['B', 'E']),
         'B': set(['A', 'C']),
         'C': set(['B', 'D', 'E']),
         'D': set(['C']),
         'E': set(['A', 'C'])}

    v = list(dfs_paths(graph1, 'A', 'D'))
    print(v)

if __name__ == '__main__':
    main()
