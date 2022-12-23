
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
        neighbors = self.nodes[starting_territory]["neighbors"]
        if starting_territory in self.units[unit_id]["starting territory"] and country in self.units[unit_id]["country"]:
            player_owns_unit = True
            unit_type = self.units[unit_id]["unit type"]
        else:
            player_owns_unit = False
        if "A" in action:
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
    """def successful_move(self, territory):
        occupied = False
        related_attack = False"""
        



    def successful_move(self, territory):
        related_moves = {}
        occupied = False
        related_attack = False
        #Determine if the territory is occupied
        for each_move in self.moves:
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
                return None


#related moves format: nested dictionary
#dictionary entries: action: {"unit id": unit_id, "starting territory": starting territory}

def check_attack_validity(self, territory, move, related_moves):
    #If the unit is occupKied
    what_to_do = None
    occupied_support_count = 0
    if move != None:
        #Check for related supports if there are related moves
        if len(related_moves) > 0:
            for related_move in related_moves:
                if related_move == "S":
                    #check for possible cut supports
                    possible_cut_support = "check for possible cut support?"
                    support_validity = "run support validity function"
            if support_validity > 0:
                occupied_support_count += 1
        else:
            print("yay")

#This is all programmed under the assumption that the moves were the keys
def support_validity(self, territory, occupied, move, related_moves, support_type):
    related_attacks_info = []
    territory_supports = 0
    related_supports_counts = []
    #SECTION I: Determine if there are attacks on the unit
    #Determine related attacks if there are multiple related moves
    if len(related_moves) > 1:
        if "A {}".format(territory) in related_moves.keys():
            for related_move in related_moves:
                #Determine if a related move attacks
                if related_move == "A {}".format(territory):
                    related_support_count = 0
                    related_territory = related_move["starting territory"]
                    potential_supports = related_moves.pop(related_move)
                    #Determine support for multiple potential supports for related attack
                    if len(potential_supports) > 1:
                        for potential_support in potential_supports:
                            potential_support_validity = check_cut_support_for_attack(territory, related_territory, potential_support)
                            if potential_support_validity == True:
                                related_support_count += 1
                    #Determine support for one potential support for related attack
                    elif len(potential_supports) == 1:
                        potential_support_validity = check_cut_support_for_attack(territory, related_territory, potential_supports[0])
                        if potential_support_validity == True:
                            related_support_count += 1
                    #append the attack and support count
                    related_attacks_info.append([related_move, related_territory, related_support_count])
                    related_supports_counts.append(related_support_count)
    #Determine related attack if there is one related move
    elif len(related_moves) == 1:
        if "A {}".format(territory) in related_moves.keys():
            related_attacks_info.append([related_territory, 0])
    #Determine supports for territory
    if occupied == True:
        if "S {} H".format(territory) in related_moves.keys():
            for related_move in related_moves:
                if related_move == "S {} H".format(territory):
                    territory_supports += 1
    #SECTION II: determine winning move/winning support
    #Determine winning move/winning support for multiple attacks
    if len(related_attacks_info) > 1:
        maximum_support = max(related_supports_counts)
        winning_attack = []
        for each_attack in related_attacks_info:
            if maximum_support == each_attack[2]:
                winning_attack.append(each_attack)
        #Determine winning move/winning support if there are multiple attacks with the same strength
        if len(winning_attack) > 1:
            if occupied == True:
                winning_move = "H"
                winning_support = territory_supports
            else:
                winning_move = None
                winning_support = 0            
        #Determine winning move/winning support for one attack on unit
        elif len(winning_attack) == 1:
            if territory_supports >= maximum_support:
                winning_move = "H"
                winning_support = territory_supports
            else:
                winning_move = winning_attack[0][0]
                winning_support = winning_attack[0][2]
    #Determine winning move/winning support for one related attack
    elif len(related_attacks_info) == 1:
        if territory_supports >= related_attacks_info[0][2]:
            winning_move = "H"
            winning_support = territory_supports
        else:
            winning_move = related_move[0][0]
            winning_support = related_attacks_info[0][2]
    #Determine winning move for no attacks
    else:
        winning_move = move
        winning_support = territory_supports
    #SECTION III: Determine what to return
    #Return winning move (if it's run in support validity) or support count (if it's run in attack validity)
    if support_type == "S":
        return winning_move
    elif support_type == "A":
        return winning_support

def check_cut_support_for_attack(self, territory, related_territory, potential_support):          
    if potential_support == "S {} A {}".format(related_territory, territory):
        supporting_territory = potential_support["starting territory"]
        if "A {}".format(supporting_territory) in self.moves.keys():
            return False
        else:
            return True



"""
def check_support_validity(self, territory, support_type, occupied, related_moves):
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
            #QUESTION TO ASK MERCY: if there's any cut support on support_type "S", isn't support cut?
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
"""