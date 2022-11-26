#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:55:17 2022

@author: katherinesweeney
"""


 #Class Nodes creates the nodes of the graph (i.e. the territories)
class Node():
    
    def __init__(self, territory_name, land_type, dot_status, neighbors):
        self.name = territory_name
        self.land_type = land_type
        self.dot_status = dot_status
        self.neighbors = neighbors
    
    def printing(self):
        print("The territory {} has neighbors {} and a dot status of {}".format(self.name, self.neighbors, self.dot_status))
        
       #Main Body
            
#initialize
graph_file = open("map_data.csv", "r")
graph_file = graph_file.readlines()[1:]

#parsing data and calling node function 
for line in graph_file:
    line = line.replace("\n", "")
    line = line.split(",")
    line[-1] = line[-1].split(" ")
    node = Node(line[0], line[1], line[2], line[3])
    node_print = node.printing()

