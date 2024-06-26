"""
Class: Node_Visualize

Purpose: Create a graph with the territories as nodes to confirm territories' neighbors are correct.

Input: Node name (e.g. Den)

Output: Node to add to the graph

Source: https://www.geeksforgeeks.org/visualize-graphs-in-python/
"""

import networkx as nx 
import matplotlib.pyplot as plt 

class GraphVisualization: 
    
    # List stores the graph's set of edges
	def __init__(self): 
		self.visual = [] 
		
	# Take vertices for an edge append the edge to the visual list 
	def addEdge(self, a, b): 
		temp = [a, b] 
		self.visual.append(temp) 
		
	# Create a graph with list of edges 
	def visualize(self): 
		G = nx.Graph() 
		G.add_edges_from(self.visual)
		figure = plt.figure(figsize = (16, 12))
		nx.draw_networkx(G, node_size = 100, node_color = "skyblue", width = 0.5) 
		plt.show() 
