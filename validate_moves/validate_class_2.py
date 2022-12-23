"""
Class to validate the moves
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
        neighbors = self.nodes[starting_territory]["neighbors"]
        if starting_territory in self.units[unit_id]["starting territory"] and country in self.units[unit_id]["country"]:
            player_owns_unit = True
            unit_type = self.units[unit_id]["unit type"]
        else:
            player_owns_unit = False
        if action[0] == "A":
            destination = action[-3:]
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
        elif action == "H":
            return move
        elif "S" in action:
            return move
        elif "C" in action:
            print("fuck maybe we got a convoying unit")
        else:
            return None

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
    def successful_move(self, territory):
        related_moves = {}
        neighbors = self.nodes[territory]["neighbors"]
        all_moves = self.moves.values()
        
        
        
        
        #Determine if the territory is occupied
        """for each_move in self.moves:
            if territory in self.moves[each_move]["starting territory"]:
                occupied = True
                action = self.moves[each_move]["action"]
            if territory in self.moves[each_move]["action"]:
                related_moves[self.moves[each_move]["starting territory"]] = self.moves[each_move]["action"]
        #If the territory is occupied, check if the move's action is to hold or support
        for related_move in related_moves:
            if "A {}".format(territory) in related_moves[related_move]:
                related_attack = True
                break
        if occupied:
            if related_attack:
                if action[0] == "H":
                    print("{} might hold".format(territory))
                elif action[0] == "S":
                    print("{} might support".format(territory))
            else:
                if action[0] == "H":
                   print("{} holds".format(territory))
                elif action[0] == "S":
                    print("{} supports".format(territory)) 
        #If the territory is not occupied, check if there are attacks on the territory
        else:
            if related_attack == True:
                print("{} is attacked".format(territory))
            #If the territory is not occupied and there are no attacks on the territory, return None
            else:
                return None"""