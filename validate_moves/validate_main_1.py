import sys
from validate_class_1 import Validate_move

#Fancy Imports
sys.path.append("graph")
import node_class
import parse_file
from graph_main import *
sys.path.append("units")
from run_create_units import run_create_units

#Initialize
starting_units_raw = open("data/starting_territories.csv", "r")
territories_raw = open("data/map_data.csv", "r")
territories_parsed = parse_file.parse_file(territories_raw)
starting_units_parsed = parse_file.parse_file(starting_units_raw)
image_file = "data/map_w_dots.png"
filtered_moves = []
successful_moves = []
node_dict = {}
unit_dict = {}
moves = {}

#Call functions
"""
Properties of Imported Classes:
- Node properties: name, land_type, dot_status, neighbors
- Unit properties: id, country, starting_territory, unit_type, image, map_file
"""
for node in nodes:
    node_dict[node.name] = {"land type": node.land_type, "dot status": node.dot_status, "neighbors": node.neighbors}

#print(node_dict)


units = run_create_units(starting_units_parsed, territories_parsed, image_file, "units")
for unit in units:
    unit_dict[unit.id] = {
        "starting territory": unit.starting_territory, 
        "country": unit.country, 
        "unit type": unit.unit_type}
    #write actions
    if unit.starting_territory == "Lon":
        action = "A Eng"
    elif unit.starting_territory == "Lvp":
        action = "S Edi H"
    elif unit.starting_territory == "Bre":
        action = "S Par A Gas"
    elif unit.starting_territory == "Par":
        action = "A Gas"
    elif unit.starting_territory == "Tri":
        action = "A Ven"
    elif unit.starting_territory == "Ven":
        action = "S Rom H"
    else:
        action = "H"
    moves[unit.id] = {
        "country": unit.country,
        "starting territory": unit.starting_territory,
        "action": action
    }
#print(unit_dict)
#print(moves)


filtering_moves = Validate_move(moves, node_dict, unit_dict)
filtered_moves = {}
for each_move in moves:
    #print(moves[each_move])
    filtered_move = filtering_moves.filter_move(each_move, moves[each_move])
    if filtered_move != None:
        filtered_moves[each_move] = moves[each_move]



validating_moves = Validate_move(filtered_moves, node_dict, unit_dict)
for territory in territories_parsed:
    det_successful_move = validating_moves.successful_move(territory[0])
    if det_successful_move != None:
        print(det_successful_move)
    #successful_moves.append(det_successful_move)

#print("Successful moves", successful_moves)
