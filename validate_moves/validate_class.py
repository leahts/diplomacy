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
        hold_validity = False
        for unit in self.units:
            if territory == unit.territory:
                occupation_status = True
                break
        for move in self.moves:
            action = move["Action"]
            if move["Unit"] == territory:
                if action == "H":
                    occupation_status = True
                    print(" ")
                    print("territory", territory)
                    print("Occupation status:", occupation_status)
                    print("move", move)
                    hold_validity = self.check_attack_validity(territory, move, occupation_status, relevant_moves)
                    print("hold validity", hold_validity)
                    return hold_validity
                elif action[0] == "A":
                    attack_validity = self.check_attack_validity(territory, move, occupation_status, relevant_moves)
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

    def check_attack_validity(self, territory, move, occupied, related_moves):
        attacking_info = []
        supports_for_each_move = []
        num_of_related_moves = len(related_moves)
        i = 0
        j = 0
        print("related moves", related_moves)
        #account for if the territory is occupied and potential units supporting occupied territory
        if occupied == True:
            occupied_support_count = 0
            while i < num_of_related_moves:
                if related_moves[i]["Action"][0] == "S":
                    possible_support_cuts = self.find_related_moves(related_moves[i]["Unit"])
                    print("Possible cuts", possible_support_cuts)
                    print("Input to possible support cuts", related_moves[i]["Unit"])
                    if len(possible_support_cuts) > 0:
                        support_validity = self.check_support_validity(related_moves[i]["Unit"], "A", occupied, possible_support_cuts)
                        print("Support validity check", support_validity)
                        if support_validity == True:
                            occupied_support_count += 1
                    else:
                        occupied_support_count += 1
                    attacking_info.append([territory, occupied_support_count])
                    supports_for_each_move.append(occupied_support_count)
                i += 1
        #look for units attacking territory
        for each_move in related_moves:
            if "A {}".format(territory) in each_move["Action"][0:5]:
                attack_supports = 0
                possible_support_cuts = self.find_related_moves(each_move["Unit"])
                if len(possible_support_cuts) > 0:
                    possible_support_validity = self.check_support_validity(each_move["Unit"], "A", occupied, possible_support_cuts)
                    if possible_support_validity == True:
                        attack_supports += 1
                attacking_info.append([each_move, attack_supports])
                supports_for_each_move.append(attack_supports)
        #WORK ON THIS AREA
        #determine the winning move if there are multiple moves/attacks involving a territory
        if len(supports_for_each_move) > 0:
            attacks_w_most_support = []
            #find the move(s) with the most support
            maximum_support = max(supports_for_each_move)
            for each_attack in attacking_info:
                if each_attack[1] == maximum_support:
                    attacks_w_most_support.append(each_attack[0])
            #determine what to do if there's multiple moves with the most support
            if len(attacks_w_most_support) > 1:
                #if there are multiple attacks on a unit, the occupied unit wins
                #if a holding unit is attacked (with the same support), the occupied unit wins
                if occupied == True:
                    winning_move = self.find_move_from_territory(territory)
                    print(winning_move, "occupied")
                    return winning_move
                else:
                    print("hello, no winning move")
                    return None
            else:
                #print("attack unit that won", attacking_info[0][0])
                winning_move = self.find_move_from_territory(attacking_info[0][0])
                return winning_move
        #determine and return move if there are no supports for the attack/hold
        else:
            if occupied == True:
                winning_move = self.find_move_from_territory(territory)
                return winning_move
            else:
                print("attack unit that won", attacking_info[0][0])
                winning_move = self.find_move_from_territory(attacking_info[0][0])
                #return winning_move
                return winning_move
    
    #if support_type = "A" => return support count
    #if support_type = "S" => return winning_move 
    #"Support hold" is for territories that are occupied and support so the winning move is returned
    def check_support_validity(self, territory, support_type, occupied, related_moves):
        is_support_valid = 0
        attacks_count = []
        attacks_on_territory_info = []
        biggest_attack = []
        #Determine if the move that is cutting support is being attacked
        #related move = a move that is potentially cutting support
        for related_move in related_moves:
            attack_on_territory_count = 0
            pot_related_attacks = self.find_related_moves(related_move["Unit"])
            num_of_pot_related_attacks = len(pot_related_attacks)
            #If there are potential attacks on the related move, determine if the related move's cut support is valid
            if num_of_pot_related_attacks > 0:
                for pot_related_attack in pot_related_attacks:
                    #if the related is attacked, then the related move does not count against the unit supporting
                    #unit supporting => the unit occupying the territory in question
                    if pot_related_attack["Action"] == "A {}".format(related_move["Unit"]):
                        related_attack = False
                        break
                    else:
                        related_attack = True
                #if the related move is not attacked and support is cut, then increase the cut support's count
                if related_move["Action"] == "A {}".format(territory) and related_attack == False:
                    attack_on_territory_count += 1
            #If there are no potential attacks on the related move, determine if it is a cut support
            else:
                #If the related move attacks the territory, increase the attack count by one
                #DO I NEED TO FIND SUPPORT FOR ATTACK
                if related_move["Action"] == "A {}".format(territory):
                    attack_on_territory_count += 1
                #If the related move does not attack the territory, increase the support count by one
                else:
                    is_support_valid += 1
            #append the supports of the attack to attacks_count if attacks_count > 0
            if attack_on_territory_count > 0:
                attacks_count.append(attack_on_territory_count)
            #append the information on the attack on the supporting unit
            attacks_on_territory_info.append([related_move, attack_on_territory_count])
        #Determe the move to return
        #If there are multiple attacks on the unit, determine the biggest attack on the unit
        if len(attacks_count) > 1:
            maximum_attack_support = max(attacks_count)
            for each_attack in attacks_on_territory_info:
                if each_attack[1] == maximum_attack_support:
                    biggest_attack.append(each_attack[0])
            #Start returning shit
            #if there are multiple "biggest" attacks with the same support, determine what to return
            if len(biggest_attack) > 1:
                #if occupied, the multiple attacks bounce out and the occupied unit holds
                if occupied == True:
                    winning_move = self.support_return_function(territory, support_type, is_support_valid)
                    if support_type == "S":
                        winning_move["Action"] = "H"
                    elif support_type == "A":
                        winning_move = 0
                    return winning_move
                #if not occupied, the multiple attacks bounce out and the territory is not occupied
                else:
                    return None
            #if there is one biggest attack, determine what to return
            elif len(biggest_attack) == 1:
                #if the support is greater than the attack's support, the unit holds
                if is_support_valid > maximum_attack_support:
                    winning_move = self.support_return_function(territory, support_type, is_support_valid)
                    if support_type == "S":
                        winning_move["Action"] == "H"
                    elif support_type == "A":
                        winning_move = 0
                    return winning_move
                #if the support and attack's support are equal, the unit holds
                elif is_support_valid == maximum_attack_support:
                    winning_move = self.find_move_from_territory(territory, support_type, is_support_valid)
                    if support_type == "S":
                        winning_move["Action"] = "H"
                    elif support_type == "A":
                        winning_move = 0
                    return winning_move
            #gives info if something is wrong
            else:
                return "FUCKKKK THE BIGGEST ATTACK THING DIDN'T WORK"
        #if there is one attack on the supporting unit, determine what to return
        elif len(attacks_count) == 1:
            attack_count = attacks_on_territory_info[0][1]
            attack_territory = attacks_on_territory_info[0][0]
            #if the support is greater than the attack's support, return the support
            #QUESTION: if there's any cut support on support_type "S", isn't support cut?
            if is_support_valid > attack_count:
                winning_move = self.support_return_function(territory, support_type, is_support_valid)
                if support_type == "S":
                    winning_move["Action"] = "H"
                elif support_type == "A":
                    winning_move = 0
                return winning_move
            #if the support is equal to the attack's support, the unit holds
            elif is_support_valid == attack_count:
                winning_move = self.support_return_function(territory, support_type, is_support_valid)
                if support_type == "S":
                    winning_move["Action"] = "H"
                elif support_type == "A":
                    winning_move = 0
                return winning_move
            #if the attacking_move has greater support, the attacking_unit occupies the territory
            else:
                winning_move = self.support_return_function(attack_territory, support_type, is_support_valid)
                return winning_move
        #if there are no attacks on the supporting unit, return the move of the supporting unit
        else:
            winning_move = self.support_return_function(territory, support_type, is_support_valid)
            return winning_move

    def find_move_from_territory(self, territory):
        for move in self.moves:
            if move["Unit"] == territory:
                return move

    def support_return_function(self, og_territory, support_type, support_validity_count):
        if support_type == "S":
            winning_move = self.find_move_from_territory(og_territory)
            return winning_move
        elif support_type == "A":
            return support_validity_count

    def find_related_moves(self, indiv_territory):
        related_moves = []
        for move in self.moves:
            if indiv_territory in move["Action"]:
                related_moves.append(move)
        return related_moves