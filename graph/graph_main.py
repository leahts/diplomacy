#Imports
import networkx as nx
import matplotlib.pyplot as plt
import visualizing_graph as visualizing_graph
import parse_file
import node_class

#Create a node of the graph (i.e. the territories)


#Main Body
#Open the graph file and parse data
graph_raw = open("data/map_data.csv", "r")
graph_file = parse_file.parse_file(graph_raw)

#Create nodes
for line in graph_file:
    node = node_class.Node(line[0], line[2], line[3], line[4])
    print_statement = node.printing()

#Visualize the graph
visualizing_graph.create_graph(graph_file)
