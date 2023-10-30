# A Vertex class object is a vertex of a graph
class Vertex:
    # Constructor
    def __init__(self, n):
        self.name = n # Name of a vertex
        self.neighbor_set = set()
        
    # The add_neighbor method adds a vertex v in neighbor list
    def add_neighbor(self, v): 
        if v not in self.neighbor_set: #list:
            self.neighbor_set = self.neighbor_set | {v}
        
# A Graph object is a dictionary, which is constructed
# through adding graph and edges
class Graph:
    graph = dict() # Instanciate graph as an empty dictionary

    # The add_vertex method adds a vertex in the graph if not in.
    # Using the vertex.name as key, the vertex as value.
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and \
           vertex.name not in self.graph:
            self.graph[vertex.name] = vertex

    # The add_edge method adds an edge (ends with U and V) to the graph
    # by expanding their vertex.neighbor_list.
    def add_edge(self, u, v):
        if u in self.graph and v in self.graph: # Check both keys in graph
            for key, value in self.graph.items(): # Assume undirect graph
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    # The print_graph method prints each vetex and adjacent list
    def print_graph(self):
        for key in sorted(list(self.graph.keys())):
            print(str(key) + ': ',self.graph[key].neighbor_set)
        
def main():
    g = Graph()

    for i in range(1, 9):
        g.add_vertex(Vertex(str(i)))
                     
    edges = ['12', '13', '23', '24', '25', '35', '37', '38', \
             '45', '56', '78']
    
    # for i in range(ord('A'), ord('K')):
    #     g.add_vertex(Vertex(chr(i)))

    # edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', \
    #          'FG', 'FI', 'FJ', 'GJ', 'HI']
    


    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.print_graph()

if __name__ == '__main__':
    main()
