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

    def successful_move(self, territory):
        #print(territory)
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
                    checking_hold = self.attack_validity(territory, action, occupied, related_moves)
                    print("The result of whether {} holds is {}".format(territory, checking_hold))
                elif action[0] == "S":
                    checking_support = self.support_validity(territory, occupied, action, related_moves, "S")
                    print("{} has support of {}".format(territory, checking_support))
                elif action[0] == "A":
                    checking_attack = self.attack_validity(territory, action, occupied, related_moves)
                    print("1: The result of the possible attack on {} is {}".format(territory, checking_attack))
            #The move is valid if there are no moves attacking/supporting the territory
            else:
                if action[0] == "H":
                    print("{} holds".format(territory))
                elif action[0] == "S":
                    print("{} supports".format(territory))
                #check occupied!!!!!!
                elif action[0] == "A":
                    checking_attack = self.attack_validity(territory, action, occupied, related_moves)
                    if checking_attack:
                        print("The attack {} was successful and {} is now empty".format(checking_attack, territory))
        else:
            if len(related_moves) > 0:
                checking_attack = self.attack_validity(territory, None, occupied, related_moves)
                print("The result of the attack on the empty territory is {}".format(checking_attack))
            else:
                return None

    def attack_validity(self, territory, action, occupied, related_moves):
        print("Territory {} has action {} and related moves {}".format(territory, action, related_moves))
        occupied_support_count = 0
        related_attack_info = []
        support_counts = []
        related_attack = False
        possible_cut_dict = {}
        for related_move in related_moves:
            related_support_count = 0
            possible_cut_territories = self.nodes[related_move]["neighbors"]
            for each_cut in possible_cut_territories:
                if each_cut in self.moves.keys():
                    possible_cut_dict[each_cut] = self.moves[each_cut]["action"]
            #Check if attack is valid
            if related_moves[related_move] == "A {}".format(territory):
                if possible_cut_dict != None:
                    if "A {}".format(related_move) in possible_cut_dict.values():
                        related_attack = False
                    else:
                        related_attack = True
                        attack_support = self.support_validity(related_move, True, related_moves[related_move], possible_cut_dict, "A")
                        if attack_support != None:
                            related_support_count = related_support_count + attack_support
                        related_attack_info.append([related_move, related_support_count])
                        support_counts.append(related_support_count)
                else:
                    #print("checking if this runs for england")
                    related_attack_info.append([related_move, 0])
            #Check if supporting a hold is valid
            elif related_move == "S {} H".format(territory):
                if possible_cut_dict != None:
                    support_hold = self.support_validity(related_move, True, related_moves[related_move], possible_cut_dict, "A")
                    if support_hold != None:
                        occupied_support_count = occupied_support_count + support_hold
                else:
                    occupied_support_count += 1
            else:
                continue  
        if len(support_counts) > 0:
            attacks_w_most_support = []
            #Find the move(s) with the most support
            maximum_support = max(support_counts)
            for each_attack in related_attack_info:
                if each_attack[1] == maximum_support:
                    attacks_w_most_support.append(each_attack[0])
        """if action:
            if related_attack:
                if len(attacks_w_most_support) > 1:
                    winning_move = action
                    if territory == "Tri":
                        print("test1")
                elif len(attacks_w_most_support) == 1:
                    winning_move = attacks_w_most_support[0]
                    if territory == "Tri":
                        print("test2")
                else:
                    winning_move = related_attack_info[0][0]
                    if territory == "Tri":
                        print("test3")
            else:
                if self.moves[territory]["action"] == "H" or "S" in self.moves[territory]["action"]:
                    winning_move = self.moves[territory]["action"]
                    if territory == "Tri":
                        print("test4a")
                else:
                    print(self.moves[territory]["action"])
                    winning_move = action
                    if territory == "Tri":
                        print("test4b")
        else:
            if related_attack:
                if len(attacks_w_most_support) > 1:
                    winning_move = None
                    if territory == "Tri":
                        print("test5")
                elif len(attacks_w_most_support) == 1:
                    winning_move = attacks_w_most_support[0]
                    if territory == "Tri":
                        print("test6")
                else:
                    winning_move = related_attack_info[0][0]
                    if territory == "Tri":
                        print("test7")
            else:
                winning_move = None
                if territory == "Tri":
                        print("test8")"""
        if occupied:
            if related_attack:
                if len(attacks_w_most_support) > 1:
                    winning_move = action
                    if territory == "Tri":
                        print("test1")
                elif len(attacks_w_most_support) == 1:
                    winning_move = attacks_w_most_support[0]
                    if territory == "Tri":
                        print("test2")
                else:
                    winning_move = related_attack_info[0][0]
                    if territory == "Tri":
                        print("test3")
            else:
                winning_move = self.moves[territory]["action"]

                if territory == "Tri":
                    print("test 4", territory, winning_move)

                """if self.moves[territory]["action"] == "H" or "S" in self.moves[territory]["action"]:
                    winning_move = self.moves[territory]["action"]
                    if territory == "Tri":
                        print("test4a")
                else:
                    print(self.moves[territory]["action"])
                    winning_move = action
                    if territory == "Tri":
                        print("test4b")"""
        else:
            if related_attack:
                if len(attacks_w_most_support) > 1:
                    winning_move = None
                    if territory == "Tri":
                        print("test5")
                elif len(attacks_w_most_support) == 1:
                    winning_move = attacks_w_most_support[0]
                    if territory == "Tri":
                        print("test6")
                else:
                    winning_move = related_attack_info[0][0]
                    if territory == "Tri":
                        print("test7")
            else:
                winning_move = None
                if territory == "Tri":
                        print("test8")
        return winning_move

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
