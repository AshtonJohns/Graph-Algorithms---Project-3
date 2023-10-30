def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                print(path + [next])
                yield path + [next]               
            else:
                queue.append((next, path + [next]))

def main():
    g = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
     }

    

    paths = tuple(bfs_paths(g, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
    print('The paths are:')
    print(paths)

if __name__ == '__main__':
    main()


