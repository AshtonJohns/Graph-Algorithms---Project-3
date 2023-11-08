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

# scc = max(nx.strongly_connected_components(G), key=len)

# print(scc)

scc = nx.strongly_connected_components(G)

# #list comprehension 
# temp_list = list(scc)
# conn_comp = []
# for connected_components_list in temp_list:
#     conn_comp.append(list(connected_components_list))

# message1 = "Strongly Connected Components for the digraph: "
# for scc_group in conn_comp:
#     message1 += "\n"+ str(scc_group)

# print(message1)
# #print(conn_comp)


testter = nx.condensation(G)

# nx.draw_networkx(testter,node_size=1000,width=3)
# plt.margins(0.2)
#plt.show()

node_data = testter.nodes.data()
map = {}
for node_data_stuff in node_data:
    test_str = str(node_data_stuff[1]['members'])
    test_str = test_str[1:]
    test_str = test_str[:-1]
    print(test_str)
    map[node_data_stuff[0]] = test_str
    # print(node_data_stuff[0])
    # print(node_data_stuff[1]['members']) 
    #print(node_data_stuff)
print(map)
testter = nx.relabel_nodes(testter,map)
#print(list(node_data))
#edge_data = G.edges
#print(edge_data)

# nx.draw_networkx(testter,node_size=1000,width=3)
# plt.margins(0.2)
#plt.show()

# edge_data = testter.edges
# print(edge_data)
#nx.spring_layout(testter)

if nx.is_directed_acyclic_graph(testter):
    print("true")

testter = nx.dag_to_branching(testter)

if nx.is_directed_acyclic_graph(testter):
    print("true")


node_data = testter.nodes.data()
map = {}
print(node_data)
for node_data_stuff in node_data:
    test_str = str(node_data_stuff[1]['source'])
    # test_str = test_str[1:]
    # test_str = test_str[:-1]
    print(test_str)
    map[node_data_stuff[0]] = test_str
    # print(node_data_stuff[0])
    # print(node_data_stuff[1]['members']) 
    #print(node_data_stuff)
print(map)
testter = nx.relabel_nodes(testter,map)

node_data = testter.nodes.data()
pos = {}
print(node_data)
i = 0
for node_data_stuff in node_data:
    #test_str = str(node_data_stuff[1]['source'])
    # test_str = test_str[1:]
    # test_str = test_str[:-1]
    pos[node_data_stuff[0]] = (i,5)
    i += 2.5


nx.draw(testter,pos=pos,node_size=700,with_labels=True,width=3,connectionstyle='arc3, rad=0.5')






#plt.margins(0.2)
plt.show()
# # nx.spreadout(G)
# # plt.margins(1,1)
# # figure = plt.gcf()
# # figure.set_size_inches(5,5)
# plt.savefig("testter.png")

