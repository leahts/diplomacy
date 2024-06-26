"""
Functions used to create the nodes
"""

import networkx as nx
from Nodes_Class import Node

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
    return indiv_node

"""
run_create_nodes creates nodes from territories

Input: CSV file of territories
Output: Dictionary of Nodes
        Key => Territory abbreviations
        Value => node objects
"""
def run_create_nodes (csv_file):
    node_dict = {}
    parsed_csv = parse_file(csv_file)
    for indiv_line in parsed_csv:
        indiv_create_node = create_node(indiv_line)
        node_dict[indiv_line[0]] = indiv_create_node
        indiv_create_node.print_node_info()
    return node_dict