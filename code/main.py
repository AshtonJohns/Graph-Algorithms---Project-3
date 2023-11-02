import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

## produce graph without variation of node positions (when position is NOT defined)
# seed = 0
# random.seed(seed)
# np.random.seed(seed)

G=nx.Graph()

# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")
# G.add_node("E")
# G.add_node("F")
# G.add_node("G")
# G.add_node("H")
# G.add_node("I")
# G.add_node("J")
# G.add_node("K")
# G.add_node("L")
# G.add_node("M")
# G.add_node("N")
# G.add_node("O")
# G.add_node("P")

# G.add_edges_from()
# G.add

# undirected graph 1
G.add_edge("A","B")
G.add_edge("A","F")
G.add_edge("A","E")
G.add_edge("B","F")
G.add_edge("E","F")
G.add_edge("E","I")
G.add_edge("I","J")
G.add_edge("I","M")
G.add_edge("M","N")
G.add_edge("B","C")
G.add_edge("J","G")
G.add_edge("C","D")
G.add_edge("C","G")
G.add_edge("G","D")
G.add_edge("H","K")
G.add_edge("H","L")
G.add_edge("K","L")
G.add_edge("K","O")
G.add_edge("L","P")

G.nodes()

pos={
    
    "A":(0,10),
    "B":(2.5,10),
    "C":(5,10),
    "D":(7.5,10),
    "E":(0,7.5),
    "F":(2.5,7.5),
    "G":(5,7.5),
    "H":(7.5,7.5),
    "I":(0,5),
    "J":(2.5,5),
    "K":(5,5),
    "L":(7.5,5),
    "M":(0,2.5),
    "N":(2.5,2.5),
    "O":(5,2.5),
    "P":(7.5,2.5),
}

# generate undirected graph 
nx.draw(G,pos=pos,with_labels=True,node_color="red",node_size=3000,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=5,edge_color="black")
plt.margins(0.2)
plt.show()


# main driver
def main():
    #get task 1 undirected graph
    
    choice = True
    showInvalidinput = False
    createResults = False
    while choice:
        #get input and ask which task to view
        print("Please select the task to be viewed:\n1. DFS & BFS on undirected graph\n2. \n3. \n4. Quit/Save Results")
        opt1 = input("\nChoice: ")
        if opt1.__eq__("1"):
            print("\n\n___QUESTION___:\nStarting from any vertex, can DFS and BFS find all connected components of an undirected graph? ")
        elif opt1.__eq__("4"):
            print("Would you like to save these results?\n1. Yes\n2. No")
            opt2 = input("\nChoice: ")
            if opt2.__eq__("1"):
                choice = False
                createResults = True
            elif opt2.__eq__("2"):
                choice = False
            else:
                showInvalidinput = True
        else:
            showInvalidinput = True
        # show when invalid input
        if showInvalidinput:
            print("\n\nPlease select a valid option\n\n")
            choice = True
            showInvalidinput = False
            createResults = False

    if createResults:
        print("not implemnted ")
        # do stuff here

    print("\n\nThank you! Take care.")


if __name__ == '__main__':
    main()