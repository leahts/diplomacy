import sys
from validate_class_2 import Validate_move
from parse_moves import parse_moves

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
moves_file = open("data/starting_moves_trial_1.csv", "r")
moves_parsed = parse_moves(moves_file)
filtered_moves = []
successful_moves = []
node_dict = {}
unit_dict = {}
moves = {}

#Call functions
"""
node_dict entires: name: 
    {"land type": node.land_type, 
    "dot status": node.dot_status, 
     "neighbors": node.neighbors}

unit_dict entries: unit.id: 
    {starting territory: unit.starting_territory, 
    country: unit.country, 
    unit type: unit.unit_type}

moves entires: starting territory:
    {country: unit.country,
    unit id: unit.id,
    "action": action}
"""

for node in nodes:
    node_dict[node.name] = {"land type": node.land_type, "dot status": node.dot_status, "neighbors": node.neighbors}

units = run_create_units(starting_units_parsed, territories_parsed, image_file, "units")
for unit in units:
    unit_dict[unit.id] = {
        "starting territory": unit.starting_territory, 
        "country": unit.country, 
        "unit type": unit.unit_type}
    #write actions
    for line in moves_parsed:
        if unit.starting_territory == line[0]:
            action = line[1]
            break
        else:
            action = "H"
    moves[unit.starting_territory] = {
        "country": unit.country,
        "action": action,
        "unit id": unit.id
    }

#print("MOVES", moves)

#print(node_dict.keys())

filtering_moves = Validate_move(moves, node_dict, unit_dict)
filtered_moves = {}

for each_move in moves:
    filtered_move = filtering_moves.filter_move(each_move, moves[each_move])
    if filtered_move != None:
        filtered_moves[each_move] = moves[each_move]


validating_moves = Validate_move(filtered_moves, node_dict, unit_dict)
for territory in territories_parsed:
    det_successful_move = validating_moves.successful_move(territory[0])
    if det_successful_move == "S" or det_successful_move == "H":
        print(territory[0], det_successful_move)
    elif det_successful_move != None:
        print(det_successful_move)
    #if det_successful_move != None:
        #print(det_successful_move)
    #successful_moves.append(det_successful_move)

#print("Successful moves", successful_moves)
