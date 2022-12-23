"""
Class to validate the moves
"""

class Validate_move():

    def __init__(self, moves, nodes, units):
        self.moves = moves
        self.nodes = nodes
        self.units = units
    
    def filter_move(self, starting_territory, move):
        country = move["country"]
        unit_id = move["unit id"]
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

    moves entires: starting territory:
        {country: unit.country,
        unit id: unit.id,
        "action": action}
    """
    def successful_move(self, territory):
        related_moves = {}
        occupied = False
        action = None
        neighbors = self.nodes[territory]["neighbors"]
        if territory in self.moves.keys():
            occupied = True
            action = self.moves[territory]["action"]
        for neighbor in neighbors:
            if neighbor in self.moves.keys():
                if " A {}".format(territory) in self.moves[neighbor]["action"]:
                    related_moves[neighbor] = self.moves[neighbor]["action"]
        if occupied:
            if len(related_moves) > 0:
                if action[0] == "H":
                    print("{} might hold".format(territory))
                elif action[0] == "S":
                    print("{} might support".format(territory))
                elif action[0] == "A":
                    print("{} might attack".format(territory))
            else:
                if action[0] == "H":
                    print("{} holds".format(territory))
                elif action[0] == "S":
                    print("{} supports".format(territory))
                elif action[0] == "A":
                    print("{} might attack; it is not being attacked".format(territory))
        else:
            if len(related_moves) > 0:
                print("{} is attacked".format(territory))
            else:
                return None
        

                
        
        
        
        #Determine if the territory is occupied
        """
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