#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:55:17 2022

@author: katherinesweeney
"""
#Imports
import networkx as nx
import matplotlib.pyplot as plt


#Class Nodes creates the nodes of the graph (i.e. the territories)
class Node():
    
    def __init__(self, territory_name, land_type, dot_status, neighbors):
        self.name = territory_name
        self.land_type = land_type
        self.dot_status = dot_status
        self.neighbors = neighbors
    
    def printing(self):
        print("The territory {} has neighbors {} and a dot status of {}".format(self.name, self.neighbors, self.dot_status))
        
        
# Code is taken from geeksforgeeks.org/visualize-graphs-in-python/
#Code for __init__ and add_initial_edge is not modified
#Thank you for your service geeksforgeekss
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


#Main Body
            
#initialize
graph_file = open("map_data.csv", "r")
graph_file = graph_file.readlines()[1:]
territory_names = []
i = 0
node_graph = nx.Graph()
"""visual = []"""

for line in graph_file:
    #parse data
    line = line.replace("\n", "")
    line = line.split(",")
    line[-1] = line[-1].split(" ")
    territory_names.append(line[0])
    #create nodes and graph
    node = Node(line[0], line[1], line[2], line[3])
    creating_graph = GraphVisualization()
    if i == 0:
        for neighbor in line[-1]:
            """initial_connection = [line[0], neighbor]
            visual.append(initial_connection)
            node_graph.add_edges_from(initial_connection)"""
            initial_graph = creating_graph.add_initial_edge(line[0], neighbor)
            node_graph.add_edges_from(initial_graph)
    else:
        for neighbor in line[-1]:
            """if neighbor not in node_graph:
                connection = [line[0], neighbor]
                visual.append(connection)
                node_graph.add_edges_from(visual)"""
            graph_connections = creating_graph.graph_additions(line[0], neighbor)
            node_graph.add_edges_from(graph_connections)
    node_print = node.printing()
    i += 1
    """info = creating_graph.get_nodes_and_edges()
    print(info)"""

"""plot graph"""
nx.draw_networkx(node_graph)
plt.show()
    



