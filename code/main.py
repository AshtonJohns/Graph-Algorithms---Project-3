import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import networkx as nx
import numpy as np
import random
from docx import Document
from docx.shared import Inches
import os

## produce graph without variation of node positions (when position is NOT defined)
# seed = 0
# random.seed(seed)
# np.random.seed(seed)
def addToDoc(document,task="",text="",tmpFile="",addparagraph=False,addFigure=False):
    if addparagraph: #adding bolded paragraph
        p = document.add_paragraph()
        p.add_run(text).bold = True
    if addFigure:
        document.add_heading(task + "graph",level=1)
        document.add_picture(tmpFile)

def generateGraph(G,pos,tmpFile,document,task,pressAnyKey,mainIllustration=False,wouldLikeToViewGraphs=True,node_size=1000,x=3,y=3,is_directed=False): #genereate all kinds of graphs
    if mainIllustration:
        if not is_directed:
            nx.draw(G,pos=pos,with_labels=True,node_color="red",node_size=3000,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=5,edge_color="black")
        else:
            nx.draw_networkx(G,pos=pos,with_labels=True)
        plt.margins(0.2)
        #add image to docx file
        plt.savefig(tmpFile)
        # add figure to document
        addToDoc(document,task=task,tmpFile=tmpFile,addFigure=True)
    else: # compare 
        nx.draw(G,pos=pos,with_labels=True,node_color="green",node_size=node_size,font_color="white",font_size=10,font_family="Times New Roman", font_weight="bold",width=2,edge_color="black")
        plt.margins(0.2)
        #save to figure
        figure = plt.gcf()
        figure.set_size_inches(x,y)
        #add image to docx file
        plt.savefig(tmpFile)
        # add figure to document
        addToDoc(document,task=task,tmpFile=tmpFile,addFigure=True)

    if wouldLikeToViewGraphs: # if the user wants to compare the figures
        plt.show(block=False) # display graph
        # inform user to press any key to move on
        #print(pressAnyKey)
        input("\n---Press Enter to continue---")
        plt.clf()
        plt.close()
    else:
        plt.clf()
        plt.close()

def generateGraphSideBySideForComparison(G_dfs,G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=True):
    #dfs
    tmpFile_dfs = "dfs" + tmpFile
    nx.draw(G_dfs,pos=pos,with_labels=True,node_color="green",node_size=400,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=3,edge_color="black")
    plt.margins(0.2)
    #save to figure
    figure = plt.gcf()
    figure.set_size_inches(2.5,2.5)
    #add image to docx file
    plt.savefig(tmpFile_dfs)
    # add figure to document
    addToDoc(document,task=task,tmpFile=tmpFile_dfs,addFigure=True)
    plt.clf()
    plt.close()

    #bfs
    tmpFile_bfs = "bfs" + tmpFile
    nx.draw(G_bfs,pos=pos,with_labels=True,node_color="green",node_size=400,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=3,edge_color="black")
    plt.margins(0.2)
    #save to figure
    figure = plt.gcf()
    figure.set_size_inches(2.5,2.5)
    #add image to docx file
    plt.savefig(tmpFile_bfs)
    # add figure to document
    addToDoc(document,task=task,tmpFile=tmpFile_bfs,addFigure=True)
    plt.clf()
    plt.close()


    if wouldLikeToViewGraphs:
        # Load the images
        plt.clf()
        plt.close()
        image1 = plt.imread(tmpFile_dfs)
        image2 = plt.imread(tmpFile_bfs)

        # Create a figure and axes
        fig, axes = plt.subplots(1, 2)

        # Plot the images
        axes[0].imshow(image1)
        axes[1].imshow(image2)

        # Show the figure
        plt.show(block=False) # display graph
        # inform user to press any key to move on
        #print(pressAnyKey)
        input("\n---Press Enter to continue---")
        plt.clf()
        plt.close()
    


def viewGraphs():
    cont = True
    viewFile = False
    answerQuestion = False
    while cont:
        print("\n\nWould you like to answer this question? \n1. Yes\n2. No\n")
        answerQChoice = input("Choice: ")
        if answerQChoice.__eq__("1"):
            answerQuestion = True
            cont = False
            # print("\nWould you like to see the graphs for comparison? (If not, SAVE THE FILE to view later)\n1. Yes\n2. No\n")
            # choice = input("Choice: ")
            # if choice.__eq__("1"):
            #     viewFile = True
            #     cont = False
            # elif choice.__eq__("2"):
            #     print("\n\nOkay, you will not see the comparisons\n\n")
            #     cont = False
        elif answerQChoice.__eq__("2"):
            cont = False
        else:
            print("Please select a valid option")
    return viewFile,answerQuestion

def getConnectedComponents(G):
    conn_comp_gen = nx.connected_components(G)
    #list comprehension 
    temp_list = list(conn_comp_gen)
    conn_comp = []
    for connected_components_list in temp_list:
        conn_comp.append(list(connected_components_list))
    return conn_comp
    

def task1(document):
    #current task
    task = "Task 1 "
    #temp file for graphs
    tmpFile = "graph.png"
    # move on message
    pressAnyKey = "\n\n" + task + "graph\n\n" + "\n---PRESS ANY KEY TO MOVE ON!---\n\n"
    # questions
    question1 = "\n\nQUESTION:\nStarting from any vertex, can DFS and BFS find all connected components of an undirected graph?\n\n"
    question2 = "\n\nQUESTION:\nCan both BFS and DFS determine if there is a path between two given nodes?\n\n"
    question3 = "\n\nQUESTION:\nProvided that there is a path between two vertices u and v in the graph. If started from u, do DFS and BFS always find exactly the same path to v?\n\n"
    #create graph
    G=nx.Graph()
    # undirected graph 1
    # G_undirected_edges = [["A","B"],
    #                       ["B","C"],
    #                       ["C","D"],
    #                       ["A","E"],
    #                       ["A","F"],
    #                       ["B","F"],
    #                       ["C","G"],
    #                       ["D","G"],
    #                       ["E","F"],
    #                       ["E","I"],
    #                       ["F","I"],
    #                       ["H","K"],
    #                       ["H","L"],
    #                       ["G","J"],
    #                       ["I","J"],
    #                       ["K","L"],
    #                       ["I","M"],
    #                       ["K","O"],
    #                       ["L","P"],
    #                       ["M","N"]
    #                      ]

    task1graphedges = [("A", "B"),
                       ("A", "F"),
                       ("A", "E"),
                        ("B", "F"),
                        ("B", "C"),
                        ("C", "D"),
                        ("C", "G"),
                        ("D", "G"),
                        ("G", "J"),
                        ("E", "F"),
                        ("E", "I"),
                        ("F", "I"),
                        ("I", "J"),
                        ("I", "M"),
                        ("M", "N"),
                        ("H", "K"),
                        ("K", "O"),
                        ("K", "L"),
                        ("L", "H"),
                        ("L", "P")]
    #add edges
    G.add_edges_from(task1graphedges)
    # G.add_edge("A","B")
    # G.add_edge("B","C")
    # G.add_edge("C","D")
    # G.add_edge("A","E")
    # G.add_edge("A","F")
    # G.add_edge("B","F")
    # G.add_edge("C","G")
    # G.add_edge("D","G")
    # G.add_edge("E","F")
    # G.add_edge("E","I")
    # G.add_edge("F","I")
    # G.add_edge("H","K")
    # G.add_edge("H","L")
    # G.add_edge("G","J")
    # G.add_edge("I","J")
    # G.add_edge("K","L")
    # G.add_edge("I","M")
    # G.add_edge("K","O")
    # G.add_edge("L","P")
    # G.add_edge("M","N")

    G_undirected = G.to_undirected()

    #get connected components
    conn_comp = getConnectedComponents(G)
    
    # list_connected_components_1 = ['A','B','C','D','E','F','G','I','J','M','N']
    # list_connected_components_2 = ['H','K','L','O','P']

    pos={ # positions for nodes
        
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

    #
    # ######################### --------------- QUESTION 1 ---------------#########################  #
    # 
    print(question1)
    # add question to document
    addToDoc(document,text=question1,addparagraph=True)

    # generate undirected graph 
    generateGraph(G_undirected,pos,tmpFile,document,task,pressAnyKey,mainIllustration=True,wouldLikeToViewGraphs=True)

    document.add_page_break()

    # can DFS & BFS find all components of undirected graph?
    #ask if the user wants to compare the graphs, or just view it later in the file
    view,answerQuestion = viewGraphs()     

    if answerQuestion:
        for node in G_undirected.nodes():
            #list for storing results for DFS & BFS
            dfs = []
            bfs = []
            for current_node in nx.dfs_tree(G_undirected,node):
                dfs.append(current_node)
            for current_node in nx.bfs_tree(G_undirected,node):
                bfs.append(current_node)

            #determine which connected components to look at 
            current_conn_comp = []
            for known_conn_comp_part in conn_comp:
                if node in known_conn_comp_part:
                    current_conn_comp = known_conn_comp_part
            # message1
            message1 = "\n\nDFS\nStart node: " + node + "\nConnected Components found by DFS from the start node: \n" + str(dfs) + "\nKnown Connected Components: \n" \
                        + str(conn_comp) + "\nKnown Connected Components in Question: \n" + str(current_conn_comp) \
                        + "\nDid DFS find all connected components from the start node?\n" +"(DFS)" + str(dfs) + "\n=?\n" + str(current_conn_comp) + "\nResult: "
            result = set(current_conn_comp).__eq__(set(dfs))
            message1 += str(result)
            print(message1)
            addToDoc(document,text=message1,addparagraph=True) 
            # message2
            message2 = "\n\nBFS\nStart node: " + node + "\nConnected Components found by BFS from the start node: \n" + str(bfs) + "\nKnown Connected Components: \n" \
                        + str(conn_comp) + "\nKnown Connected Components in Question: \n" + str(current_conn_comp) \
                        + "\nDid BFS find all connected components from the start node?\n" +"(BFS)" + str(dfs) + "\n=?\n" + str(current_conn_comp) + "\nResult: "
            result = set(current_conn_comp).__eq__(set(dfs))
            message2 += str(result)
            print(message2)
            addToDoc(document,text=message2,addparagraph=True)
            document.add_page_break()



            # #list for storing results for DFS & BFS
            # dfs = []
            # bfs = []
            # #generate temp graph
            # temp_G_dfs = nx.Graph()
            # temp_G_bfs = nx.Graph()
            # previous_node = '' #stores previous node while doing dfs or bfs
            # for current_node in nx.dfs_tree(G_undirected,node):
            #     dfs.append(current_node)
            #     if previous_node != current_node and previous_node != '': #create the temp graph
            #         temp_G_dfs.add_edge(previous_node,current_node)
            #     # assign the previous node
            #     previous_node = current_node
            # previous_node = '' #reset for bfs
            # for current_node in nx.bfs_tree(G_undirected,node):
            #     bfs.append(current_node)
            #     if previous_node != current_node and previous_node != '': #create the temp graph for bfs
            #         temp_G_bfs.add_edge(previous_node,current_node)
            #     previous_node = current_node
            # #display both dfs & bfs figures for the user to see if they chose to view
            # generateGraphSideBySideForComparison(temp_G_dfs,temp_G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view)
            # # determine which list of connected components the node belongs within
            # if node in list_connected_components_1:
            #     list_connected_components = list_connected_components_1
            # else:
            #     list_connected_components = list_connected_components_2
            # # print message / doc message
            # message = "\nKnown connected components: " + str(list_connected_components) + \
            #         "\nStarting from node: " + node + "..." + \
            #         "\nConnected components determined with DFS: " + str(dfs) + \
            #         "\nConnected components determined with BFS: " + str(bfs) + \
            #         "\nDid DFS and BFS result in getting all the connected components?" + \
            #         "\n(DFS)" + str(dfs) + "=?" + str(list_connected_components) + ": "
            # # compare with list of connected components
            # dfs.sort()
            # result = list_connected_components.__eq__(dfs)
            # message += str(result)
            # message += "\n(BFS)" + str(bfs) + "=?" + str(list_connected_components) + ": "
            # bfs.sort()
            # result = list_connected_components.__eq__(bfs)
            # message += str(result)
            # print(message)
            # addToDoc(document,text=message,addparagraph=True)
    
    #
    # ######################### --------------- QUESTION 2 ---------------#########################  #
    # 
    print(question2)
    #insert page break
    document.add_page_break()
    # add question to document
    addToDoc(document,text=question2,addparagraph=True)
    message = "\nTo answer this question, we will loop over all nodes, and find all possible paths, using DFS and BFS\n\n"
    print(message)
    addToDoc(document,text=message,addparagraph=True)
    # generate undirected graph 
    generateGraph(G_undirected,pos,tmpFile,document,task,pressAnyKey,mainIllustration=True,wouldLikeToViewGraphs=True)
    document.add_page_break()
    # Can both BFS and DFS determine if there is a path between two given nodes?
    #ask if the user wants to compare the graphs, or just view it later in the file
    view,answerQuestion = viewGraphs() 

    if answerQuestion:
        for node in G_undirected.nodes():
            # message1
            message1 = "\n\nDFS\nStart node: " + node
            print(message1)
            addToDoc(document,text=message1,addparagraph=True)
            
            for current_node in nx.dfs_tree(G_undirected, node):
                if current_node != node: # A == A, B == B, etc (starting nodes)
                    # message2
                    message2 = "\nDFS found a path from start node " + node + " and end node " + current_node  
                    print(message2)
                    addToDoc(document,text=message2,addparagraph=True)
            # message3
            message3 = "\n\nBFS\nStart node: " + node
            print(message3)
            addToDoc(document,text=message3,addparagraph=True)
            for current_node in nx.bfs_tree(G_undirected, node):
                if current_node != node:
                    # message4
                    message4 = "\nBFS found a path from start node " + node + " and end node " + current_node  
                    print(message4)
                    addToDoc(document,text=message4,addparagraph=True)
            document.add_page_break()

    # if answerQuestion:
    #     for node in G_undirected.nodes():
    #         dfs_for_undirected = []
    #         # message1
    #         message1 = "\n\nDFS\nStart node: " + node
    #         print(message1)
    #         addToDoc(document,text=message1,addparagraph=True)
    #         for current_node in nx.dfs_tree(G_undirected,node):
    #             test_list.append(current_node)
    #             dfs_for_undirected.append(current_node)
    #             if current_node != node: # A == A, B == B, etc (starting nodes)
    #                 dfs_for_undirected.append(current_node)
    #         dfs_for_undirected.pop()
    #         dfs_for_undirected_to_path = []
    #         for x in range(len(dfs_for_undirected)-1):
    #             temp_list = []
    #             if x % 2 == 0:
    #                 temp_list.append([dfs_for_undirected[x],dfs_for_undirected[x+1]])
    #                 path = nx.Graph()
    #                 path.add_edges_from(temp_list)

    #                 dfs_for_undirected_to_path.append([dfs_for_undirected[x],dfs_for_undirected[x+1]])
    #                 #convert to 2d
    #                 #dfs_to_2d = np.array(dfs_for_undirected_to_path).reshape((len(dfs_for_undirected_to_path))//2,2)
    #                 temp_G_dfs = nx.Graph()
    #                 temp_G_dfs.add_edges_from(dfs_for_undirected_to_path)

    #                 generateGraph(path,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=300)
    #                 generateGraph(temp_G_dfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=500)
    #                 # message2
    #                 message2 = "\nEnd node: " + dfs_for_undirected[x+1] + "\nDFS found a path from start node " + node + " and end node " + dfs_for_undirected[x+1] + "\nNew Edge: " + str(temp_list) + "\nTotal path: \n" + str(dfs_for_undirected_to_path) 
    #                 print(message2)
    #                 addToDoc(document,text=message2,addparagraph=True)
    #                 document.add_page_break() 

    #
    # ######################### --------------- QUESTION 3 ---------------#########################  #
    # 
    print(question3)
    #insert page break
    document.add_page_break()
    # add question to document
    addToDoc(document,text=question3,addparagraph=True)
    message = "\nTo answer this question, we will loop over all nodes, and find all possible paths, using DFS and BFS\n\n"
    print(message)
    addToDoc(document,text=message,addparagraph=True)
    # generate undirected graph 
    generateGraph(G_undirected,pos,tmpFile,document,task,pressAnyKey,mainIllustration=True,wouldLikeToViewGraphs=True)
    document.add_page_break()
    # Provided that there is a path between two vertices u and v in the graph. If started from u, do DFS and BFS always find exactly the same path to v?
    #ask if the user wants to compare the graphs, or just view it later in the file
    view,answerQuestion = viewGraphs() 

    if answerQuestion:
        #find the known connected component parts
        conn_comp_1 = conn_comp[0]
        conn_comp_2 = conn_comp[1]


        for nodeA in conn_comp_1:
            for nodeB in conn_comp_1:
                if nodeA != nodeB:
                    dfs = []
                    bfs = []
                    #message 1 
                    message1 = "\nKnown Connected Components: \n" + str(conn_comp_1) \
                             + "\nStart node: \n" + nodeA + "\nNode to compare DFS and BFS path: \n" + nodeB
                    for i in nx.dfs_tree(G_undirected, nodeA):
                        dfs.append(i)
                    message1 += "\nConnected Components found by DFS from the start node: \n" + str(dfs)
                    for i in nx.bfs_tree(G_undirected, nodeA):
                        bfs.append(i)
                    message1 += "\nConnected Components found by BFS from the start node: \n" + str(bfs)
                    if nodeB in dfs and nodeB in bfs: #REVISE
                        dfsendnodeindex = dfs.index(nodeB)
                        bfsendnodeindex = bfs.index(nodeB)
                        dfspath = dfs[:dfsendnodeindex]
                        message1 += "\n(DFS)Connected Components from start node to comparable node: \n" + str(dfspath)
                        bfspath = bfs[:bfsendnodeindex]
                        message1 += "\n(BFS)Connected Components from start node to comparable node: \n" + str(bfspath) \
                                + "\nAre the paths exactly the same? \n" + "(DFS)" + str(dfspath) + "\n=?\n" + "(BFS)" + str(bfspath) \
                                + "\nResult: "
                        if dfspath == bfspath:
                            message1 += "True"
                        else: 
                            message1 += "False"
                    else: 
                        message1 += "\nTest"
                        print("Test") #task1file.write("\nNo path exists between " + str(nodeA) + " and " + str(i)) 
                    print(message1)
                    addToDoc(document,text=message1,addparagraph=True)
                    document.add_page_break()

        for nodeA in conn_comp_2:
            for nodeB in conn_comp_2:
                if nodeA != nodeB:
                    dfs = []
                    bfs = []
                    #message 2 
                    message2 = "\nKnown Connected Components: \n" + str(conn_comp_2) \
                             + "\nStart node: \n" + nodeA + "\nNode to compare DFS and BFS path: \n" + nodeB
                    for i in nx.dfs_tree(G_undirected, nodeA):
                        dfs.append(i)
                    message2 += "\nConnected Components found by DFS from the start node: \n" + str(dfs)
                    for i in nx.bfs_tree(G_undirected, nodeA):
                        bfs.append(i)
                    message2 += "\nConnected Components found by BFS from the start node: \n" + str(bfs)
                    if nodeB in dfs and nodeB in bfs: #REVISE
                        dfsendnodeindex = dfs.index(nodeB)
                        bfsendnodeindex = bfs.index(nodeB)
                        dfspath = dfs[:dfsendnodeindex]
                        message2 += "\n(DFS)Connected Components from start node to comparable node: \n" + str(dfspath)
                        bfspath = bfs[:bfsendnodeindex]
                        message2 += "\n(BFS)Connected Components from start node to comparable node: \n" + str(bfspath) \
                                + "\nAre the paths exactly the same? \n" + "(DFS)" + str(dfspath) + "\n=?\n" + "(BFS)" + str(bfspath) \
                                + "\nResult: "
                        if dfspath == bfspath:
                            message2 += "True"
                        else: 
                            message2 += "False"
                    else: 
                        message2 += "\nTest"
                        print("Test") #task1file.write("\nNo path exists between " + str(nodeA) + " and " + str(i)) 
                    print(message2)
                    addToDoc(document,text=message2,addparagraph=True)
                    document.add_page_break()     


    # if answerQuestion:
    #     for node in G_undirected.nodes():
    #         #list for storing results for DFS & BFS
    #         dfs = [] #stores all edges for DFS
    #         bfs = [] #stores all edges for BFS
    #         temp_list = [] #stores an edge
    #         # message1
    #         message1 = "\n\nDFS\nStart node: " + node
    #         print(message1)
    #         addToDoc(document,text=message1,addparagraph=True)
    #         for current_node in nx.dfs_tree(G_undirected,node):
    #             #generate graph containing all discovered edges
    #             temp_G_dfs = nx.Graph()
    #             #generate graph containing newly discovered edge
    #             path = nx.Graph()
    #             #add add nodes to create a new edge
    #             temp_list.append(current_node) 
    #             if len(temp_list) == 2: #once two nodes are connected...
    #                 dfs.extend(temp_list)
    #                 # add path from previous edge end node to start node of newly discovered edge
    #                 if len(dfs) > 2:
    #                     dfs.insert(dfs.index(dfs[-2]),dfs[-3])
    #                     dfs.insert(dfs.index(dfs[-2]),dfs[-2])
    #                 #convert to 2d
    #                 dfs_to_2d = np.array(dfs).reshape((len(dfs))//2,2) 
    #                 # create the total path for DFS
    #                 temp_G_dfs.add_edges_from(dfs_to_2d)
    #                 # create the newly discovered edge 
    #                 path.add_edge(temp_list[0],temp_list[1])
    #                 generateGraph(path,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=500)
    #                 generateGraph(temp_G_dfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=500)
    #                 # message2
    #                 message2 = "\nEnd node: " + current_node + "\nDFS found a path from start node " + node + " and end node " + current_node + "\nNew Edge: " + str(temp_list) + "\nTotal path: \n" + str(dfs_to_2d.flatten()) 
    #                 print(message2)
    #                 addToDoc(document,text=message2,addparagraph=True)
    #                 document.add_page_break()
    #                 temp_list = [] #clean edge
    #         # message3
    #         message3 = "\n\nBFS\nStart node: " + node
    #         print(message3)
    #         addToDoc(document,text=message3,addparagraph=True)
    #         for current_node in nx.bfs_tree(G_undirected,node):
    #             #generate graph containing all discovered edges
    #             temp_G_bfs = nx.Graph()
    #             #generate graph containing newly discovered edge
    #             path = nx.Graph()
    #             #add add nodes to create a new edge
    #             temp_list.append(current_node) 
    #             if len(temp_list) == 2: #once two nodes are connected...
    #                 bfs.extend(temp_list)
    #                 # add path from previous edge end node to start node of newly discovered edge
    #                 if len(bfs) > 2:
    #                     bfs.insert(bfs.index(bfs[-2]),bfs[-3])
    #                     bfs.insert(bfs.index(bfs[-2]),bfs[-2])
    #                 #convert to 2d
    #                 bfs_to_2d = np.array(bfs).reshape((len(bfs))//2,2) 
    #                 # create the total path for bfs
    #                 temp_G_bfs.add_edges_from(bfs_to_2d)
    #                 # create the newly discovered edge 
    #                 path.add_edge(temp_list[0],temp_list[1])
    #                 generateGraph(path,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=500)
    #                 generateGraph(temp_G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view,x=2,y=2,node_size=500)
    #                 # message4
    #                 message4 = "\nEnd node: " + current_node + "\nBFS found a path from start node " + node + " and end node " + current_node + "\nNew Edge: " + str(temp_list) + "\nTotal path: \n" + str(bfs_to_2d.flatten()) 
    #                 print(message4)
    #                 addToDoc(document,text=message4,addparagraph=True)
    #                 document.add_page_break()
    #                 temp_list = []
            
def task2(document):
    #current task
    task = "Task 1 "
    #temp file for graphs
    tmpFile = "graph.png"
    # move on message
    pressAnyKey = "\n\n" + task + "graph\n\n" + "\n---PRESS ANY KEY TO MOVE ON!---\n\n"
    # questions
    question1 = "\n\nQUESTION:\nUse an application to find the strongly connected components of the digraph.\n\n"
    question2 = "\n\nQUESTION:\nDraw the digraph as a 'meta graph' of its strongly connected components in the report.\n\n"
    question3 = "\n\nQUESTION:\nRepresent the 'meta graph' as a DAG and linearize it in its topological order.\n\n"
    #create graph
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
    # digraph 1

    # #get connected components
    # conn_comp = getConnectedComponents(G)

    pos={ # positions for nodes
        
        1:(0,10),
        3:(2.5,10),
        5:(5,10),
        6:(7.5,10),
        4:(0,7.5),
        2:(2.5,7.5),
        9:(5,7.5),
        8:(6.2,7.5),
        7:(9,7.5),
        12:(2.5,5),
        11:(5,5),
        10:(7.5,5),
    }

    #
    # ######################### --------------- QUESTION 1 ---------------#########################  #
    # 
    print(question1)
    # add question to document
    addToDoc(document,text=question1,addparagraph=True)

    # generate undirected graph 
    generateGraph(G,pos,tmpFile,document,task,pressAnyKey,mainIllustration=True,wouldLikeToViewGraphs=True,is_directed=True)

    document.add_page_break()

    # Use an application to find the strongly connected components of the digraph
    #ask if the user wants to compare the graphs, or just view it later in the file
    view,answerQuestion = viewGraphs()
         

    
    

    


# main driver
def main():
    #get task 1 undirected graph
    document = Document()
    document.add_heading('Test Results on Graph Algorithms',level=0)
    document.add_page_break()


    choice = True
    showInvalidinput = False
    createResults = False
    while choice:
        #get input and ask which task to view
        print("\nPlease select the task to be viewed:\n1. DFS & BFS on undirected graph\n2. Connected digraph as a 'meta graph'" \
              + "\n3. \n4. Quit/Save Results")
        opt1 = input("\nChoice: ")
        if opt1.__eq__("1"): 
            task1(document=document)
        elif opt1.__eq__("2"):
            task2(document=document)
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
        # # do stuff here
        cwd = os.getcwd()
        print("Creating document...")
        #document = Document(cwd + "Task Results.docx")
        filename = "Task Results.docx"
        try_again = True
        i = 1
        #in case the file is opened, to prevent loss of runs, create another file
        while try_again:
            try:
                document.save(filename)
                try_again = False
            except:
                filename = "Task Results(" + str(i) +").docx"
                i += 1
        # remove png files
        for file in os.listdir("."):
            if file.endswith(".png"):
                os.remove(file)
        if i>1:
            print("\n\nYou had a similar file name opened, so another is going to be created with (" + str(i-1)+") in the filename.")
        print("\n\nDocument can be found in the directory:\n\n" + cwd + "\\" + filename)

    print("\n\nThank you! Take care.")


if __name__ == '__main__':
    main()