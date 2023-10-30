# Reference code from
# http://stackoverflow.com/questions/15038876/topological-sort-python

def dfs_tpl_order(graph,start,path):
    path = path + [start]
    global n
    for edge in graph[start]: 
        if edge not in path:
            path = dfs_tpl_order(graph, edge,path)
    print (n, start)
    n -= 1
    return path
    
# Sample graph
graph = {'A': set(['C', 'D']),
         'B': set(['D', 'E']),
         'C': set(['D', 'F', 'H']),
         'D': set(['E']),
         'E': set(['G', 'I']),
         'F': set(['G']),
         'G': set(['I']),
         'H': set(['I']),
         'I': set()}

n = len(graph)
print('Topological order starting from \'A\'')
u = dfs_tpl_order(graph, 'A', [])
print(u)


