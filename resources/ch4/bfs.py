
def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

#bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}
def main():
    g = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
     }

    v = bfs(g, 'A')
    print(v)

if __name__ == '__main__':
    main()

