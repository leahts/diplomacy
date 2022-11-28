#imports 
import networkx as nx
import matplotlib.pyplot as plt

# Code is taken from geeksforgeeks.org/visualize-graphs-in-python/
#Code for __init__ and add_initial_edge is not modified
#thank you geeksforgeeks I appreciate it
class GraphVisualization:
   
    def __init__(self):
        self.visual = []
        
    def add_initial_edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
        return self.visual
    
    def graph_additions(self, starting_node, possible_node):
        if possible_node not in self.visual:
            connection = [starting_node, possible_node]
            self.visual.append(connection)
            return self.visual
        
    def get_nodes_and_edges(self):
        return self.visual




def create_graph(graph_file):
    node_graph = nx.Graph()
    i = 0
    for line in graph_file:
        line = line.replace("\n", "")
        line = line.split(",")
        line[-1] = line[-1].split(" ")
        creating_graph = GraphVisualization()
        if i == 0:
            for neighbor in line[-1]:
                initial_graph = creating_graph.add_initial_edge(line[0], neighbor)
                node_graph.add_edges_from(initial_graph)
        else:
            for neighbor in line[-1]:
                graph_connections = creating_graph.graph_additions(line[0], neighbor)
                node_graph.add_edges_from(graph_connections)
        i += 1 
    nx.draw_networkx(node_graph)
    plt.show()
