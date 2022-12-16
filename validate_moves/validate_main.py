#Imports
import sys
from validate_class import Validate_move

#Fancy Imports
sys.path.append("graph")
import node_class
import parse_file
sys.path.append("units")
import run_create_units

#Initialize
starting_units_raw = open("data/starting_territories.csv", "r")
territories_raw = open("data/map_data.csv", "r")
territories_parsed = parse_file.parse_file(territories_raw)
starting_units_parsed = parse_file.parse_file(starting_units_raw)
image_file = "data/map_w_dots.png"
nodes = []
filtered_moves = []

moves = [
    #{"Country": "UK", "Unit": "Edi", "Action": "H"},
    #{"Country": "UK", "Unit": "Lon", "Action": "A Eng"},
    #{"Country": "UK", "Unit": "Lvp", "Action": "S Edi H"},
   # {"Country": "France", "Unit": "Bre", "Action": "S Par A Gas"},
    #{"Country": "France", "Unit": "Par", "Action": "A Gas"},
    {"Country": "Austria", "Unit": "Tri", "Action": "A Ven"},
    {"Country": "Italy", "Unit": "Ven", "Action": "S Rom H"},
    {"Country": "Italy", "Unit": "Rom", "Action": "H"}
]


#Main
"""
Properties of Imported Classes:
- Node properties: name, land_type, dot_status, neighbors
- Unit properties: country, territory, unit_type, image, map_file
"""
for line in territories_parsed:
    node = node_class.Node(line[0], line[2], line[3], line[5])
    nodes.append(node)

units = run_create_units.run_create_units(starting_units_parsed, territories_parsed, image_file, "units")


filtering_moves = Validate_move(moves, nodes, units)

for move in moves:
    filtered_move = filtering_moves.filter_move(move)
    if filtered_move != False:
        filtered_moves.append(filtered_move)
print(filtered_moves)
print(" ")
#print(filtered_moves)
validating_moves = Validate_move(filtered_moves, nodes, units)
for territory in territories_parsed:
    det_successful_move = validating_moves.successful_move(territory[0])