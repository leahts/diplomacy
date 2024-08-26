
The current step is to create a graph that represents the diplomacy map. An adjacency list will be created and stored in a csv. 

The nodes represent the map's territories, the edges represent the map's connections (i.e. if two countries are neighbors), and the weights indicate what type of moves are legal. The types of legal moves can be only armies allowed, only fleets allowed, or both armies and fleets allowed.  Nodes that have no edge represent territories that are not neighbors. 




create adjacency list of edges with their weights.
- info is in node object's properties
- use dictionary with tuples
- assign weights for type of connection 

store adjacency list as csv

create graph 
- territories as nodes, edges as neighbors, weights as what connection can go through






afterwards for my own memory
- take out neighbor property from nodes
- take out neighbors from nodes csv?
- store nodes in an sql table(?)