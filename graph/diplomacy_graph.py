#Imports
import networkx as nx
import matplotlib.pyplot as plt
import visualizing_graph as visualizing_graph
import parse_file

#Create a node of the graph (i.e. the territories)
class Node():

    def __init__(self, territory_name, land_type, dot_status, neighbors):
        self.name = territory_name
        self.land_type = land_type
        self.dot_status = dot_status
        self.neighbors = neighbors

    def printing(self):
        print("The territory {} has neighbors {} and a dot status of {}".format(
            self.name, self.neighbors, self.dot_status))


#Main Body
#Open the graph file and parse data
graph_raw = open("data/map_data.csv", "r")
graph_raw = graph_raw.readlines()[1:]
graph_file = parse_file.parse_file(graph_raw)

#Create nodes
for line in graph_file:
    line = line.split(",")
    node = Node(line[0], line[2], line[3], line[4])
    print_statement = node.printing()

#Visualize the graph
visualizing_graph.create_graph(graph_file)
