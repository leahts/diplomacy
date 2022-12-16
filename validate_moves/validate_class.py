#Imports



"""
Class Purpose: to validate the moves and determine which moves succeed
Input: moves that will be analyzed, nodes, and units on the map
Output:
- filter_move => returns the move that are "filtered" and follow the basic diplomacy moves
- successful_move => returns the move that is "successful" for a territory
"""

class Validate_move():

    def __init__(self, moves, nodes, units):
        self.moves = moves
        self.nodes = nodes
        self.units = units
    
    def filter_move(self, move):
        country = move["Country"]
        unit_moving = move["Unit"]
        unit_action = move["Action"]
        player_owns_unit = False
        #Check if the unit moving is a territory on the map, and if it is get territory information
        for node in self.nodes:
            if unit_moving == node.name:
                neighbors = node.neighbors
                territory_type = node.land_type
                break
        #check if the unit moving is owned by the player, and if it is get the unit_type
        for unit in self.units:
            if unit_moving == unit.territory and country == unit.country:
                player_owns_unit = True
                unit_type = unit.unit_type
                break
        #if attacking, get the destination and destination land_type
        if "A" in unit_action:
            destination = unit_action[-3:]
            for node in self.nodes:
                if node.name == destination:
                    destination_type = node.land_type
                    break
        #determine if the move follows basic diplomacy rules for an attack
        if player_owns_unit == True and "A" in unit_action:
            if destination in neighbors:
                neighbor_check = True
            else:
                neighbor_check = False
            if unit_type == "Army":
                if destination_type == "Land" or destination_type == "Coast":
                    land_type_check = True
                else:
                    land_type_check = False
            elif unit_type == "Fleet":
                if destination_type == "Sea" or destination_type == "Coast":
                    land_type_check = True
                else:
                    land_type_check = False
            #determine what to return based on if it follows diplomacy rules
            if land_type_check == True and neighbor_check == True:
                return move
            elif land_type_check == True and neighbor_check == False:
                return "maybe convoy"
            else:
                return False
        #return non-attack moves
        elif player_owns_unit == True and unit_action == "H":
            return move
        elif player_owns_unit == True and "S" in unit_action:
            return move
        else:
            return False

    def successful_move(self, territory):
        occupation_status = False
        relevant_moves = self.find_related_moves(territory)
        for unit in self.units:
            if territory == unit.territory:
                occupation_status = True
                break
        for move in relevant_moves:
            print(" ")
            print("Territory looked at:", territory)
            print("Move looked at:", move)

            action = move["Action"]
            if action[0] == "A":
                attack_validity = self.check_attack_validity(territory, occupation_status, relevant_moves)
                #print("attack valididty", move, attack_validity)
                #print(attack_validity)
            elif action[0] == "S":
                support_validity = self.check_support_validity(territory, relevant_moves)
                print("support validity", move, support_validity)
            elif action[0] == "C":
                print(move, "Convoy") 
            elif action[0] == "H":
                print(move, "Hold")
            else:
                print("SOL", move)

    def find_related_moves(self, indiv_territory):
        related_moves = []
        i = 0
        num_of_moves = len(self.moves)
        while i < num_of_moves:
            if indiv_territory in self.moves[i]["Action"]:
                related_moves.append(self.moves[i])
        return related_moves

    def check_attack_validity(self, territory, occupied, related_moves):
        attacking_info = []
        occupied_support_count = 0
        num_of_related_moves = len(related_moves)
        i = 0
        j = 0
        if occupied == True:
            occupied_supports = 0
            while i < num_of_related_moves:
                if related_moves[i]["Action"][0] == "S":
                    possible_support_cuts = self.find_related_moves(related_moves[i]["Unit"])
                    support_validity = self.check_support_validity(related_moves[i]["Unit"], possible_support_cuts)
                    if support_validity == True:
                        occupied_supports += 1
            attacking_info.append(territory, occupied_supports)
        for each_move in related_moves:
            if "A {}".format(territory) in each_move["Action"][0:5]:
                attack_supports = 0
                possible_support_cuts = self.find_related_moves(each_move["Unit"])
                possible_support_validity = self.check_support_validity(each_move["Unit"], possible_support_cuts)
                if possible_support_validity == True:
                    attack_supports += 1
                attacking_info.append([each_move["Unit"], attack_supports])
        #print(attacking_info)
        
    def check_support_validity(self, territory, related_moves):
        is_support_valid = True
        for related_move in related_moves:
            if related_move["Action"] == "S {} A {}".format(related_move, territory):
                is_support_valid = False
                break
        return is_support_valid
            