"""
Class: Create a node of the territory, which has information about the territory
Input: 
- Territory name
- Land type (land, coast, or sea)
- Dot status (True or False)
- Neighbors
"""
class Node():
#initialize the node
    def __init__(self, territory_name, land_type, dot_status, neighbors):
        self.name = territory_name
        self.land_type = land_type
        self.dot_status = dot_status
        self.neighbors = neighbors

#printing statement
    def printing(self):
        print("The territory {} has neighbors {} and a dot status of {}".format(
            self.name, self.neighbors, self.dot_status))