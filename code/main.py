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

def generateGraph(G,pos,tmpFile,document,task,pressAnyKey,mainIllustration=False,wouldLikeToViewGraphs=True): #genereate all kinds of graphs
    if mainIllustration:
        nx.draw(G,pos=pos,with_labels=True,node_color="red",node_size=3000,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=5,edge_color="black")
        plt.margins(0.2)
        #add image to docx file
        plt.savefig(tmpFile)
        # add figure to document
        addToDoc(document,task=task,tmpFile=tmpFile,addFigure=True)
    else: # compare 
        nx.draw(G,pos=pos,with_labels=True,node_color="green",node_size=1000,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=3,edge_color="black")
        plt.margins(0.2)
        #save to figure
        figure = plt.gcf()
        figure.set_size_inches(3,3)
        #add image to docx file
        plt.savefig(tmpFile)
        # add figure to document
        addToDoc(document,task=task,tmpFile=tmpFile,addFigure=True)

    if wouldLikeToViewGraphs: # if the user wants to compare the figures
        plt.show(block=False) # display graph
        # inform user to press any key to move on
        print(pressAnyKey)
        plt.waitforbuttonpress()
        plt.clf()
        plt.close()

def generateGraphSideBySideForComparison(G_dfs,G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=True):
    #dfs
    nx.draw(G_dfs,pos=pos,with_labels=True,node_color="green",node_size=1000,font_color="white",font_size=20,font_family="Times New Roman", font_weight="bold",width=3,edge_color="black")
    plt.margins(0.2)
    #save to figure
    figure = plt.gcf()
    figure.set_size_inches(3,3)
    #add image to docx file
    plt.savefig(tmpFile)
    # add figure to document
    addToDoc(document,task=task,tmpFile=tmpFile,addFigure=True)

    if wouldLikeToViewGraphs: # if the user wants to compare the figures
        plt.show(block=False) # display graph
        # inform user to press any key to move on
        print(pressAnyKey)
        plt.waitforbuttonpress()
        plt.clf()
        plt.close()

def viewGraphs():
    cont = True
    viewFile = False
    while cont:
        print("\n\nWould you like to see the graphs for comparison? (If not, SAVE THE FILE to view later)\n1. Yes\n2. No\n")
        choice = input("Choice: ")
        if choice.__eq__("1"):
            viewFile = True
            cont = False
        elif choice.__eq__("2"):
            print("\n\nOkay, you will not see the comparisons\n\n")
            cont = False
        else:
            print("Please select a valid option")
    return viewFile
    

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
    #list for storing results for DFS & BFS
    dfs = []
    bfs = []

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

    # generate undirected graph 
    generateGraph(G,pos,tmpFile,document,task,pressAnyKey,mainIllustration=True,wouldLikeToViewGraphs=True)

    #
    # ######################### --------------- QUESTION 1 ---------------#########################  #
    # 
    print(question1)
    # add question to document
    addToDoc(document,text=question1,addparagraph=True)

    # can DFS & BFS find all components of undirected graph?
    #ask if the user wants to compare the graphs, or just view it later in the file
    view = viewGraphs()     

    for node in G.nodes():
        #generate temp graph
        temp_G_dfs = nx.Graph()
        temp_G_bfs = nx.Graph()
        previous_node = '' #stores previous node while doing dfs or bfs
        for current_node in nx.dfs_tree(G,node):
            dfs.append(current_node)
            if previous_node != current_node and previous_node != '': #create the temp graph
                temp_G_dfs.add_edge(previous_node,current_node)
            # assign the previous node
            previous_node = current_node
        previous_node = '' #reset for bfs
        for current_node in nx.bfs_tree(G,node):
            bfs.append(current_node)
            if previous_node != current_node and previous_node != '': #create the temp graph for bfs
                temp_G_bfs.add_edge(previous_node,current_node)
            previous_node = current_node
        #display both dfs & bfs figures for the user to see if they chose to view
        # generateGraph(temp_G_dfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view)
        # generateGraph(temp_G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view)
        generateGraphSideBySideForComparison(temp_G_dfs,temp_G_bfs,pos,tmpFile,document,task,pressAnyKey,wouldLikeToViewGraphs=view)
    
    

    


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
        print("Please select the task to be viewed:\n1. DFS & BFS on undirected graph\n2. \n3. \n4. Quit/Save Results")
        opt1 = input("\nChoice: ")
        if opt1.__eq__("1"): 
            task1(document=document)
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
        document.save(filename)
        print("\n\nDocument can be found in the directory:\n\n" + cwd + "\\" + filename)

    print("\n\nThank you! Take care.")


if __name__ == '__main__':
    main()