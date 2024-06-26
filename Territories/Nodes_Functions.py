"""
Functions used to create the nodes and visualize the nodes

Functions to Create Nodes
        
    parse_file: parses CSV file and returns a list of the lines

    create_node: calls the node_class to make a node based on one line of the 
            parsed csv file and returns a node object

    run_create_node: takes the csv file, runs the parse_file function, and runs
            the lines of the parse_file output into the create_node function. 
            The node objects are entered into a dictionary.
            Key => name (e.g. "Mun")
            Value => node object

Functions to Visualize Nodes

    create_graph: create the nodes and edges for the territories graph

    run_create_graph: run the create_graph function and return the visual graph
"""

import networkx as nx
from Nodes_Class import Node
from Node_Visualize_Class import GraphVisualization

def parse_file (file_name):
    open_file = open(file_name)
    i = 0
    csv_lines = []
    for line in open_file.readlines():
        line = line.replace("\n", "")
        line = line.split(sep = ",")
        if i > 0:
            csv_lines.append(line)
        i += 1
    return csv_lines

"""
CVS File Line List - Elements:
    0 => Abbreviated name (e.g. Mun, Sev)
    1 => Full name (e.g. Munich, Sevestapol)
    2 => Type (land, sea, or coast)
    3 => Neighbors (terrritory abbreviations separated by spaces)
    4 => Country (e.g. Neutral, Fra, Aus)
    5 => Dot (True or False)
    6 => Home SupCenter (True or False)
"""
def create_node (line):
    indiv_node = Node(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    indiv_node.parse_nbrs()
    return indiv_node

def run_create_nodes (csv_file):
    node_dict = {}
    parsed_csv = parse_file(csv_file)
    for indiv_line in parsed_csv:
        indiv_create_node = create_node(indiv_line)
        node_dict[indiv_line[0]] = indiv_create_node
        indiv_create_node.print_node_info()
    print(node_dict)
    create_graph(node_dict)
    return node_dict

def create_graph (node_dict):
    territory_graph = GraphVisualization()
    for territory in node_dict:
        for each_nbr in node_dict[territory].nbrs:
            territory_graph.addEdge(territory, each_nbr)
    return territory_graph

def run_create_graph (node_dict):
    visual_graph = create_graph(node_dict)
    visual_graph.visualize()
    return visual_graph
