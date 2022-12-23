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
                if territory in self.moves[neighbor]["action"]:
                    related_moves[neighbor] = self.moves[neighbor]["action"]
        if occupied:
            if len(related_moves) > 0:
                if action[0] == "H":
                    print("{} might hold".format(territory))
                elif action[0] == "S":
                    checking_support = self.support_validity(territory, occupied, action, related_moves, "S")
                    print("Territory is {} and support is {}".format(territory, checking_support))
                elif action[0] == "A":
                    checking_attack = self.attack_validity(territory, action, related_moves)
            #The move is valid if there are no moves attacking/supporting the territory
            else:
                if action[0] == "H":
                    print("{} holds".format(territory))
                elif action[0] == "S":
                    print("{} supports".format(territory))
                elif action[0] == "A":
                    checking_attack = self.attack_validity(territory, action, related_moves)
                    print("{} might attack; it is not being attacked".format(territory))
        else:
            if len(related_moves) > 0:
                print("{} is attacked".format(territory))
            else:
                return None



    def attack_validity(self, territory, move, related_moves):
        #If the unit is occupied
        occupied_support_count = 0
        related_attack_info = []
        print("checkkkkkk", territory, move, "related moves", related_moves)
        """if move == "H" or "S" in move:
            for related_move in related_moves:
                related_attack_count = 0
                related_attack = False
                possible_support_cuts = self.nodes[related_move]["neighbors"]
                possible_support = self.support_validity(related_move.values(), True, related_move, possible_support_cuts, "A")
                print("possible support", possible_support)
                if possible_support:
                    if related_move == "S {} H".format(territory):
                        occupied_support_count += 1
                    elif related_move == "A {}".format(territory):
                        related_attack = True
                if related_attack:
                    related_attack_info.append(related_move, possible_support)
                    print("{} attacks {} w support of {}".format(related_move, territory, possible_support))
            print("support count for {}".format(territory), occupied_support_count)
        elif move == None:
            if related_moves > 0:
                for related_move in related_moves:"""
        if len(related_moves) > 0:
            for related_move in related_moves:
                related_attack_count = 0
                related_attack = False
                pos_support_cut_dict = {}
                possible_support_cuts = self.nodes[related_move]["neighbors"]
                if territory in possible_support_cuts:
                    possible_support_cuts = possible_support_cuts.remove(territory)
                if possible_support_cuts:
                    #print("POSSIBLE SUPPORT CUTS", possible_support_cuts)
                    for each_pos_cut in possible_support_cuts:
                        if each_pos_cut in self.moves.keys():
                            pos_support_cut_dict[each_pos_cut] = self.moves[each_pos_cut]
                    print("POSSIBLE SUPPORT CUTS for {}".format(related_move), pos_support_cut_dict)
                    possible_support = self.support_validity(related_moves[related_move], True, related_move, pos_support_cut_dict, "A")
                    if possible_support:
                        if related_move == "S {} H".format(territory) and (move == "H" or "S" in move):
                            occupied_support_count += 1
                        elif related_move == "A {}".format(territory):
                            related_attack = True
                            related_attack_count = related_attack_count + possible_support
                    
                if related_attack:
                    related_attack_info.append(related_move, possible_support)
                    print("{} attacks {} w support of {}".format(related_move, territory, possible_support))



    """
        def check_attack_validity(self, territory, occupied, related_moves):
                attacking_info = []
                supports_for_each_move = []
                num_of_related_moves = len(related_moves)
                i = 0
                print("related moves", related_moves)
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
                #Determine the winning move if there are multiple moves/attacks involving a territory
                if len(supports_for_each_move) > 0:
                    attacks_w_most_support = []
                    #Find the move(s) with the most support
                    maximum_support = max(supports_for_each_move)
                    for each_attack in attacking_info:
                        if each_attack[1] == maximum_support:
                            attacks_w_most_support.append(each_attack[0])
                    #Determine what to do if there's multiple moves with the most support
                    if len(attacks_w_most_support) > 1:
                        #If there are multiple attacks on a unit, the occupied unit wins
                        #If a holding unit is attacked (with the same support), the occupied unit wins
                        if occupied == True:
                            winning_move = self.find_move_from_territory(territory)
                            print(winning_move, "occupied")
                            return winning_move
                        else:
                            print("hello, no winning move")
                            return None
                    else:
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
            
    """





    def support_validity(self, territory, occupied, move, related_moves, support_type):
        related_attack_info = []
        related_support_count = []
        territory_supports = 0
        #SECTION I: determine if the territory is attacked
        if len(related_moves) > 1:
            if "A {}".format(territory) in related_moves.values():
                for related_move in related_moves:
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
                    related_attack_info.append([related_move, related_territory, related_support_count])
                    related_support_count.append(related_support_count)
        else:
            if "A {}".format(territory) in related_moves.values():
                related_attack_info.append([related_moves.keys(),related_moves.values(), 0])
        #Determine supports for territory
        if occupied:
            if "S {} H".format(territory) in related_moves.values():
                for related_move in related_moves:
                    if related_move == "S {} H".format(territory):
                        territory_supports += 1
        #SECTION II: determine winning move/winning support
        #Determine winning move/winning support for multiple attacks
        if len(related_attack_info) > 1:
            maximum_support = max(related_support_count)
            winning_attack = []
            for each_attack in related_attack_info:
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
        elif len(related_attack_info) == 1:
            if territory_supports >= related_attack_info[0][2]:
                winning_move = "H"
                winning_support = territory_supports
            else:
                winning_move = related_move[0][0]
                winning_support = related_attack_info[0][2]
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
        


def check_cut_support_for_attack(self, territory, related_territory, potential_supports):          
    if "S {} A {}".format(related_territory, territory) in potential_supports.values():
        supporting_territory = potential_supports["starting territory"]
        if "A {}".format(supporting_territory) in self.moves.keys():
            return False
        else:
            return True
