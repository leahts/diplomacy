"""
Class: Nodes_Class 

Purpose: create a territory object (node).

Input: name, full_name, node_type, nbrs, country, dot, hsc (home supply center)

Output: Node (object)
"""

class Node ():
    
    def __init__ (self, name, full_name, node_type, neighbors, country, 
            dot_status, hsc_status):
        self.name = name
        self.full_name = full_name
        self.node_type = node_type
        self.nbrs = neighbors
        self.country = country
        self.dot = dot_status
        self.hsc = hsc_status

    def print_node_info (self):
        print("Territory {} / {} is owned by {} with neighbors {}"
              .format(self.name, self.full_name, self.country, self.nbrs))
        print("Territory {} has dot status {} and hsc status {}"
              .format(self.name, self.dot, self.hsc))
        print("   ")




    
    