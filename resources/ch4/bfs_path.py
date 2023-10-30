''' The modified script is contributed by Maarten Fabre available at
https://codereview.stackexchange.com/questions/193410/breadth-first-search-implementation-in-python-3-to-find-path-between-two-given-n
'''

def bfs_path(graph, start, goal):
    """
    finds a shortest path in undirected `graph` between `start` and `goal`. 
    If no path is found, returns `None`
    """
    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0) 
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None 

def main():
    graph = {
        'A': set(['B', 'C']),  
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),   
        'D': set(['B']),     
        'E': set(['B', 'F']),
        'F': set(['C', 'E']),
    }
    path = bfs_path(graph, 'D', 'F')
    if path:
        print(path)
    else:
        print('no path found')
        
if __name__ == '__main__':
    main()

