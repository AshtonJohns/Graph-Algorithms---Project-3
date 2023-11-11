import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
import networkx as nx



# list_test = ["A","B"]
# list_test_1 = ["B","A"]
# list_test_1.sort()
# list_without_brackets = ','.join(list_test)
# dfs = []
# dfs.append(list_test)
# dfs.append(list_test_1)

# print(list_without_brackets)
# print(len(list_test))
# building_list = []
# if len(list_without_brackets) == 3:
#     print("True")
#     print(list_without_brackets)
#     test = "("+list_without_brackets+")"
#     building_list.append([list_without_brackets])
#     print(building_list)

# test = "("+list_without_brackets+")"

# # if len(list_test) % 2 == 0:
# #     list_without_brackets = ','.join(list_test)
# #     test = "("+list_without_brackets+")"

# message = "Test my list concatenate: " + str(list_test)

# print(message)
# size = len(dfs)

# # dfs.insert(size-1,[dfs.index()])
# # print(dfs)

# test_2d_list = [["A","B"],["B","A"]]

# dfs.clear()
# dfs = []

# dfs.append("a")
# dfs.append("b")
# # dfs.append("c")
# #dfs.extend(["e","f"])
# # dfs.extend(["g","h"])
# # dfs.extend(["i","j"])

# # dfs.insert(dfs.index(dfs[-2]),dfs[-3])
# # dfs.insert(dfs.index(dfs[-2]),dfs[-2])

# print(dfs)
# #last_index_to_size = dfs.index(dfs[-1])
# size = len(dfs)


# print(size)

# dfs_to_2d = np.array(dfs).reshape(size//2,2)

# print(dfs_to_2d)

# Create a 2D NumPy array


G=nx.DiGraph()
    
task2graphedges = [(1,3),
                    (3,2),
                    (3,5),
                    (2,1),
                    (4,1),
                    (4,2),
                    (4,12),
                    (5,6),
                    (5,8),
                    (6,8),
                    (6,7),
                    (8,9),
                    (9,5),
                    (9,11),
                    (8,10),
                    (10,9),
                    (6,10),
                    (7,10),
                    (10,11),
                    (11,12)]
    #add edges

G.add_edges_from(task2graphedges)

# # scc = max(nx.strongly_connected_components(G), key=len)

# # print(scc)

# scc = nx.strongly_connected_components(G)

# # #list comprehension 
# # temp_list = list(scc)
# # conn_comp = []
# # for connected_components_list in temp_list:
# #     conn_comp.append(list(connected_components_list))

# # message1 = "Strongly Connected Components for the digraph: "
# # for scc_group in conn_comp:
# #     message1 += "\n"+ str(scc_group)

# # print(message1)
# # #print(conn_comp)


# testter = nx.condensation(G)

# # nx.draw_networkx(testter,node_size=1000,width=3)
# # plt.margins(0.2)
# #plt.show()

# node_data = testter.nodes.data()
# map = {}
# for node_data_stuff in node_data:
#     test_str = str(node_data_stuff[1]['members'])
#     test_str = test_str[1:]
#     test_str = test_str[:-1]
#     print(test_str)
#     map[node_data_stuff[0]] = test_str
#     # print(node_data_stuff[0])
#     # print(node_data_stuff[1]['members']) 
#     #print(node_data_stuff)
# print(map)
# testter = nx.relabel_nodes(testter,map)
# #print(list(node_data))
# #edge_data = G.edges
# #print(edge_data)

# # nx.draw_networkx(testter,node_size=1000,width=3)
# # plt.margins(0.2)
# #plt.show()

# # edge_data = testter.edges
# # print(edge_data)
# #nx.spring_layout(testter)

# if nx.is_directed_acyclic_graph(testter):
#     print("true")

# testter = nx.dag_to_branching(testter)

# if nx.is_directed_acyclic_graph(testter):
#     print("true")


# node_data = testter.nodes.data()
# map = {}
# print(node_data)
# for node_data_stuff in node_data:
#     test_str = str(node_data_stuff[1]['source'])
#     # test_str = test_str[1:]
#     # test_str = test_str[:-1]
#     print(test_str)
#     map[node_data_stuff[0]] = test_str
#     # print(node_data_stuff[0])
#     # print(node_data_stuff[1]['members']) 
#     #print(node_data_stuff)
# print(map)
# testter = nx.relabel_nodes(testter,map)

# node_data = testter.nodes.data()
# pos = {}
# print(node_data)
# i = 0
# for node_data_stuff in node_data:
#     #test_str = str(node_data_stuff[1]['source'])
#     # test_str = test_str[1:]
#     # test_str = test_str[:-1]
#     pos[node_data_stuff[0]] = (i,5)
#     i += 2.5


G_weighted_undirected = nx.Graph()

G_weighted_undirected.add_edge("A","B",weight=22,color='black')
G_weighted_undirected.add_edge("A","C",weight=9,color='black')
G_weighted_undirected.add_edge("A","D",weight=12,color='black')
G_weighted_undirected.add_edge("B","F",weight=36,color='black')
G_weighted_undirected.add_edge("C","B",weight=35,color='black')
G_weighted_undirected.add_edge("C","D",weight=4,color='black')
G_weighted_undirected.add_edge("C","E",weight=65,color='black')
G_weighted_undirected.add_edge("C","F",weight=42,color='black')
G_weighted_undirected.add_edge("D","E",weight=33,color='black')
G_weighted_undirected.add_edge("E","G",weight=23,color='black')
G_weighted_undirected.add_edge("E","F",weight=18,color='black')
G_weighted_undirected.add_edge("F","G",weight=39,color='black')
G_weighted_undirected.add_edge("B","H",weight=34,color='black')
G_weighted_undirected.add_edge("D","I",weight=30,color='black')
G_weighted_undirected.add_edge("H","I",weight=19,color='black')
G_weighted_undirected.add_edge("F","H",weight=24,color='black')
G_weighted_undirected.add_edge("G","I",weight=21,color='black')
G_weighted_undirected.add_edge("G","H",weight=25,color='black')

pos={ # positions for nodes
    
    "A":(0,7.5),
    "B":(2.5,10),
    "C":(2.5,7.5),
    "D":(2.5,2.5),
    "E":(5,5),
    "F":(5,7.5),
    "G":(7.5,5),
    "H":(10,10),
    "I":(10,2.5),
}
# start_node = "A"
# nodes = G_weighted_undirected.nodes()
# spt = nx.single_source_dijkstra_path(G_weighted_undirected,start_node,weight='weight')
# message = "Nodes: \n" + str(nodes) + "\nDijkstra's algorithm found the shortest path tree:\n"
# for x,value in spt.items():
#     message += "Shortest path from " + start_node + " to " + x + ":\n"
#     message += str(value) + "\n"

# print(message)

G_error_prone = G_weighted_undirected.copy()

G_error_prone.add_edge("G","I",weight=-21,color='black')

start_node = "A"

try:
    spt = nx.single_source_dijkstra_path(G_error_prone,start_node,weight='weight')
    nx.draw(spt,pos=pos,node_size=700,with_labels=True,width=3)
except ValueError as e:
    # print(e.with_traceback())
    message = e
    print()

print(str(message))
exit()

mst = nx.minimum_spanning_tree(G_weighted_undirected,weight='weight',algorithm="kruskal")

mstPath = nx.minimum_spanning_edges(G_weighted_undirected, algorithm="kruskal",)

# mstPath = nx.minimum_branching(G_weighted_undirected,attr='weight')
# edgelist = list(mstPath)


fig, ax = plt.subplots()

# Decrease the margins
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

plt.show()


exit()

# start_node = "A"

# spt = nx.single_source_dijkstra_path(G_weighted_undirected,start_node,weight='weight')

# G_copy = G_weighted_undirected.copy()

test_list = mst.edges()
path_edge_color = 'red'

real_list = []
for x in test_list:
    real_list.append([x[0],x[1]])

print(real_list)

G_s = G_weighted_undirected.copy()

for x in range(len(real_list)):
    edges_data = G_s.get_edge_data(real_list[x][0],real_list[x][1])
    G_s.add_edge(real_list[x][0],real_list[x][1],color=path_edge_color,weight=edges_data.get('weight'))
    message = "\nTo get to node " + str(real_list[x][1]) + ", the closest node with least weight is " + str(real_list[x][0])
    message += "\nGraphically represented:\n"
    if x == len(real_list) - 1:
        message += "\n!---ALL NODES AND PATHS HAVE BEEN MADE WITH THE LEAST WEIGHT USING KRUSKAL'S ALGORITHM---!:\n"
    print(message)
# for x in range(len(real_list)):
    edges = G_s.edges()
    colors = [G_s[u][v]['color'] for u,v in edges]
    weights = [G_s[u][v]['weight'] for u,v in edges]
    nx.draw(G_s, pos, edge_color=colors, width=2,with_labels=True)
    nx.draw_networkx_edge_labels(G_s,pos=pos,edge_labels=nx.get_edge_attributes(G_s, 'weight'))
    plt.show()

exit()

for key,value in spt.items():
    do_changes = False
    G_s = G_weighted_undirected.copy()
    
    if len(value) == 2:
        edges_data = G_s.get_edge_data(value[0],value[1])
        G_s.add_edge(value[0],value[1],color=path_edge_color,weight=edges_data.get('weight'))

    elif len(value) > 2:
        for x in range(len(value)):
            if not value[-2].__eq__(value[-3]):
                index = value.index(value[x+x+1])
                value.insert(index+1,value[x+x+1])
        #convert to 2d
        dfs_to_2d = np.array(value).reshape((len(value))//2,2)
        for x in range(len(dfs_to_2d)):
            edges_data = G_s.get_edge_data(dfs_to_2d[x][0],dfs_to_2d[x][1])
            G_s.add_edge(dfs_to_2d[x][0],dfs_to_2d[x][1],color=path_edge_color,weight=edges_data.get('weight'))
          
    edges = G_s.edges()
    colors = [G_s[u][v]['color'] for u,v in edges]
    weights = [G_s[u][v]['weight'] for u,v in edges]
    nx.draw(G_s, pos, edge_color=colors, width=2,with_labels=True)
    nx.draw_networkx_edge_labels(G_s,pos=pos,edge_labels=nx.get_edge_attributes(G_s, 'weight'))
    plt.show()

exit()




path_edge_color = 'red'

for key,value in spt.items():
    do_changes = False
    G_s = G_weighted_undirected.copy()
    
    if len(value) == 2:
        edges_data = G_s.get_edge_data(value[0],value[1])
        G_s.add_edge(value[0],value[1],color=path_edge_color,weight=edges_data.get('weight'))

    elif len(value) > 2:
        for x in range(len(value)):
            if not value[-2].__eq__(value[-3]):
                index = value.index(value[x+x+1])
                value.insert(index+1,value[x+x+1])
        #convert to 2d
        dfs_to_2d = np.array(value).reshape((len(value))//2,2)
        for x in range(len(dfs_to_2d)):
            edges_data = G_s.get_edge_data(dfs_to_2d[x][0],dfs_to_2d[x][1])
            G_s.add_edge(dfs_to_2d[x][0],dfs_to_2d[x][1],color=path_edge_color,weight=edges_data.get('weight'))
          
    edges = G_s.edges()
    colors = [G_s[u][v]['color'] for u,v in edges]
    weights = [G_s[u][v]['weight'] for u,v in edges]
    nx.draw(G_s, pos, edge_color=colors, width=2,with_labels=True)
    nx.draw_networkx_edge_labels(G_s,pos=pos,edge_labels=nx.get_edge_attributes(G_s, 'weight'))
    plt.show()
#     # elif len(value) % 2 ==0:


# edges_data = G_copy.get_edge_data("A","B")

# print(nodes)
# print(edges_data)

# G_copy.add_edge("A","B",color='red',weight=100)

# edges = G_copy.edges()
# colors = [G_copy[u][v]['color'] for u,v in edges]
# weights = [G_copy[u][v]['weight'] for u,v in edges]


# for key,value in spt.items():
#     G_a_lot = G.copy()
#     G.add_edge()


# nx.draw(G_copy, pos, edge_color=colors, width=2,with_labels=True)

# nx.draw_networkx_edge_labels(G_copy,pos=pos,edge_labels=nx.get_edge_attributes(G_copy, 'weight'))
# plt.show()







# # nx.spreadout(G)
# # plt.margins(1,1)
# # figure = plt.gcf()
# # figure.set_size_inches(5,5)
# plt.savefig("testter.png")

# nx.draw(spt,pos=pos,node_size=700,with_labels=True,width=3)
# plt.show()

neg_number = -12
number = 10

if neg_number < 10:
    print("-12 is less than 10")

print(neg_number)
