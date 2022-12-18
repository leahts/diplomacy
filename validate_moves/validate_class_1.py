
"""
node_dict entires: name: 
    {"land type": node.land_type, 
    "dot status": node.dot_status, 
    "neighbors": node.neighbors}

unit_dict entries: unit.id: 
    {starting territory: unit.starting_territory, 
    country: unit.country, 
    unit type: unit.unit_type}

moves entires: unit.id:
    {country: unit.country,
    starting_territory: unit.starting_territory,
    "action": action}
"""

class Validate_move():

    def __init__(self, moves, nodes, units):
        self.moves = moves
        self.nodes = nodes
        self.units = units
    
    def filter_move(self, unit_id, move):
        country = move["country"]
        starting_territory = move["starting territory"]
        action = move["action"]
        #check if move selected is owned by the country and is in the territory
        if unit_id in self.units.keys():
            if starting_territory in self.units[unit_id]["starting territory"] and country in self.units[unit_id]["country"]:
                player_owns_unit = True
                unit_type = self.units[unit_id]["unit type"]
            else:
                player_owns_unit = False
        else:
            player_owns_unit = False
        #get neighbors of the territory for the move
        if starting_territory in self.nodes.keys():
            neighbors = self.nodes[starting_territory]["neighbors"]
        if "A" in action:
            destination = action[-3:]
            if destination in self.nodes.keys():
                land_type = self.nodes[destination]["land type"]
            if player_owns_unit == True:
                if destination in neighbors:
                    neighbor_check = True
                else:
                    neighbor_check = False
            if unit_type == "Army":
                if land_type == "Land" or land_type == "Coast":
                    land_type_check = True
                else:
                    land_type_check = False
            elif unit_type == "Fleet":
                if land_type == "Sea" or land_type == "Coast":
                    land_type_check = True
                else:
                    land_type_check = False
            if land_type_check == True and neighbor_check == True:
                return move
            elif land_type_check == True and neighbor_check == False :
                print("maybe a unit is trying to convoy")
            else:
                return None
        elif player_owns_unit == True and action == "H":
            return move
        elif player_owns_unit == True and "S" in action:
            return move
        elif player_owns_unit == True and "C" in action:
            print("fuck maybe we got a convoying unit")
        else:
            return None



    def successful_move(self, territory):
        for unit in self.units:
            if territory in self.units[unit]["starting territory"]:
                occupied = True
                break
            else:
                occupied = False
        return occupied

"""
    def successful_move(self, territory):
        occupation_status = False
        relevant_moves = self.find_related_moves(territory)
        hold_validity = False
        for unit in self.units:
            if territory == unit.territory:
                occupation_status = True
                break


        for move in self.moves:
            action = move["Action"]
            if move["Unit"] == territory:
                if action == "H":
                    print(" ")
                    print("territory", territory)
                    print("Occupation status:", occupation_status)
                    print("move", move)
                    hold_validity = self.check_attack_validity(territory, occupation_status, relevant_moves)
                    print("hold validity", hold_validity)
                    return hold_validity
                elif action[0] == "A":
                    attack_validity = self.check_attack_validity(territory, occupation_status, relevant_moves)
                    print(attack_validity)
                    return attack_validity
                elif action[0] == "S":
                    if len(relevant_moves) > 0:
                        support_validity = self.check_support_validity(territory, "S", occupation_status, relevant_moves)
                        print("support validity for {}".format(territory), support_validity)
                    else:
                        winning_move = self.find_move_from_territory(territory)
                        return winning_move
                elif action == "C":
                    return "FUCK ITS A CONVOY"
                else:
                    return "SOL"
"""