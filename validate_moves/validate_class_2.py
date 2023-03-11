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
            if "-SC" in action or "-NC" in action:
                #print("yes", action)
                destination = action[-6:]
            else:
                destination = action[-3:]
            #print(destination)
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
                print(starting_territory, destination, "maybe a unit is trying to convoy")
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
        #print("TERRITORY TESTED", territory)
        related_moves = {}
        occupied = False
        action = None
        neighbors = self.nodes[territory]["neighbors"]
        if territory in self.moves.keys():
            occupied = True
            action = self.moves[territory]["action"]
        for neighbor in neighbors:
            if neighbor in self.moves.keys():
                if self.moves[neighbor]["action"] != None:
                    if territory in self.moves[neighbor]["action"]:
                        related_moves[neighbor] = self.moves[neighbor]["action"]
        #print("territory {} has related moves".format(territory), related_moves)
        if occupied:
            if len(related_moves) > 0:
                if action[0] == "H":
                    outcome = self.attack_validity(territory, action, occupied, related_moves)
                    self.moves[territory]["action"] = outcome
                elif action[0] == "S":
                    outcome = self.support_validity(territory, occupied, related_moves, "S")
                    self.moves[territory]["action"] = outcome
                elif action[0] == "A":
                    #print("TESTING", territory, related_moves, action)
                    outcome = self.attack_validity(territory, action, occupied, related_moves)
            #The move is valid if there are no moves attacking/supporting the territory
            else:
                if action[0] == "H":
                    outcome = "H"
                elif action[0] == "S":
                    outcome = "S"
                #check occupied!!!!!!
                elif action[0] == "A":
                    outcome = self.attack_validity(territory, action, occupied, related_moves)
        else:
            if len(related_moves) > 0:
                outcome = self.attack_validity(territory, None, occupied, related_moves)
            else:
                outcome = None
        return outcome

    def attack_validity(self, territory, action, occupied, related_moves):
        occupied_support_count = 0
        related_attack_info = []
        support_counts = []
        related_attack = False
        attacks_w_most_support = []
        #Find the move(s) with the most support
        if "A {}".format(territory) in related_moves.values():
            related_attack = True
            for related_move in related_moves:
                related_support_count = 0
                print("check 1")
                attack_support = self.support_validity(territory, True, related_moves, "A")
                #print("attack support for ", territory, attack_support)
                if attack_support != None:
                    related_support_count = related_support_count + attack_support
                related_attack_info.append([related_move, related_support_count])
                support_counts.append(related_support_count)
        elif "S {} H".format(territory) in related_moves:
            for related_move in related_moves:
                print("check 2")
                support_hold = self.support_validity(territory, True, related_moves, "A")
                if support_hold != None:
                    occupied_support_count = occupied_support_count + support_hold
        #Determine attack with most support
        if len(support_counts) > 0:
            maximum_support = max(support_counts)
            for each_attack in related_attack_info:
                if each_attack[1] == maximum_support:
                    attacks_w_most_support.append(each_attack[0])
        #check winning move if unit occupies the territory
        if action != None:
            #Check winning move if there is a unit on the territory that is attacking
            if action[0] == "A":
               # print("the territory {} is attacking".format(territory))
                if "-NC" in action or "-SC" in action:
                        unit_on_territory_destination = action[-6:]
                else:
                    unit_on_territory_destination = action[-3:]
                unit_on_territory_attack = self.successful_move(unit_on_territory_destination)
                #check what happens if the attack from the unit on the territory was successful
                if unit_on_territory_attack != None:
                    if related_attack:
                        winning_move = self.check_which_attack_wins(action, related_attack_info, attacks_w_most_support)
                    else:
                        winning_move = "H"
                #checks what happens if the attack from the unit on the territory was not successful
                else:
                    if len(support_counts) > 0:
                        if len(attacks_w_most_support) == 1:
                            winning_attacker = attacks_w_most_support[0]
                            winning_move = self.moves[winning_attacker]["action"]
                        else:
                            winning_move = None
                    else:
                        winning_move = None
            elif action == "H":
                if related_attack:
                    if len(support_counts) > 0:
                        if len(attacks_w_most_support) == 1:
                            if maximum_support > 0:
                                winning_attacker = attacks_w_most_support[0]
                                winning_move = self.moves[winning_attacker]["action"]
                            else:
                                winning_move = action
                        else:
                            winning_move = action
                    else:
                        winning_move = action
                else:
                    winning_move = action
        #Check what to do if the unit moves to an occupied unit
        else:
            if related_attack:
                winning_move = self.check_which_attack_wins(action, related_attack_info, attacks_w_most_support)
            else:
                winning_move = None
        return winning_move

    def check_which_attack_wins(self, action, related_attack_info, attacks_w_most_support):
        if len(related_attack_info) > 0:
            if len(attacks_w_most_support) > 1:
                winning_move = action
            elif len(attacks_w_most_support) == 1:
                winning_attacker = attacks_w_most_support[0]
                winning_move = self.moves[winning_attacker]["action"]
            else:
                winning_move = related_attack_info[0][0]
        else:
            winning_move = None
        return winning_move

    def support_validity(self, territory, occupied, related_moves, support_type):
        print("tettiroy checking support for is ", territory)
        related_attack_info = []
        related_support_counts = []
        territory_supports = 0
        if territory in self.moves:
            if self.moves[territory]["action"] == "H":
            #check for units supporting the hold
                if "S {} H".format(territory) in related_moves.values():
                    for related_move in related_moves:
                        if related_move == "S {} H".format(territory):
                            pot_support = self.check_cut_support_for_attack(territory, related_moves, related_move)
                            if pot_support == True:
                                territory_supports += 1
            elif self.moves[territory]["action"][0] == "A":
                #print("TEST")
                if "S {} A".format(territory) in related_moves.values():
                    for related_move in related_moves:
                        if related_move == "S {} H".format(territory):
                            pot_support = self.check_cut_support_for_attack(territory, related_moves, related_move)
                            if pot_support == True:
                                territory_supports += 1
        print("the territory {} has related moves".format(territory), related_moves)
        if len(related_moves) > 1:
            if "A {}".format(territory) in related_moves.values():
                print("FUCK TEST {}".format(territory))
                for related_territory in related_moves:
                    print("idek at this point")
                    if related_moves[related_territory] == "A {}".format(territory):
                        print("HELL YEAHHHH")
                        related_support_count = 0
                        potential_supports = related_moves.copy()
                        potential_supports = potential_supports.pop(related_territory)
                        #Determine support for multiple potential supports for related attack
                        if len(potential_supports) > 1:
                            for potential_support in potential_supports:
                                #print("SUPPORT VALIDITY IS ", potential_support_validity)
                                potential_support_validity = self.check_cut_support_for_attack(territory, related_territory, potential_supports[0])
                                print("SUPPORT VALIDITY IS ", potential_support_validity)
                                if potential_support_validity == True:
                                    related_support_count += 1
                        #Determine support for one potential support for related attack
                        elif len(potential_supports) == 1:
                           # print("SUPPORT VALIDITY IS ", potential_support_validity)
                            potential_support_validity = self.check_cut_support_for_attack(territory, related_territory, potential_supports[0])
                            print("SUPPORT VALIDITY IS ", potential_support_validity)
                            if potential_support_validity == True:  
                                related_support_count += 1
                    #append the attack and support count
                        print("the territory {} is being attacked by {} with {} supports".format(territory, related_territory, related_support_count))
                        related_attack_info.append(["A {}".format(territory), related_territory, related_support_count])
                        related_support_counts.append(related_support_count)
            else:
                print("SHEEEEEEEEEE")
        else:
            print("FUCKKKKK  for {}".format(territory))
            if "A {}".format(territory) in related_moves.values():
                neighbors_of_unit_attacking = self.nodes[territory]["neighbors"]
                for neighbor_of_unit in neighbors_of_unit_attacking:
                    related_support_count = 0
                    print("related moves for {} is".format(territory), related_moves)
                    if neighbor_of_unit in related_moves.keys():
                        potential_supports = neighbors_of_unit_attacking.remove(neighbor_of_unit)
                        #Determine support for multiple potential supports for related attack
                        if potential_supports != None:
                            if len(potential_supports) > 1:
                                for potential_support in potential_supports:
                                    potential_support_validity = self.check_cut_support_for_attack(territory, neighbor_of_unit, potential_support)
                                    #print("SUPPORT VALIDITY IS ", potential_support_validity)
                                    if potential_support_validity == True:
                                        related_support_count += 1
                            #Determine support for one potential support for related attack
                            elif len(potential_supports) == 1:
                                potential_support_validity = self.check_cut_support_for_attack(territory, neighbor_of_unit, potential_supports[0])
                                #print("SUPPORT VALIDITY IS ", potential_support_validity)
                                if potential_support_validity == True:  
                                    related_support_count +1
                    related_attack_info.append(["A {}".format(territory), neighbor_of_unit, related_support_count])
                    related_support_counts.append(related_support_count)
            #print("attack info for {} is".format(territory), related_attack_info)
        #SECTION II: determine winning move/winning support
        #Determine winning move/winning support for multiple attacks
        print("territory supports for {} is".format(territory), territory_supports)
        if territory in self.moves:
            if len(related_attack_info) > 1:
                print("TEST 1")
                maximum_support = max(related_support_counts)
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
                print("TEST 2")
                if territory_supports >= related_attack_info[0][2]:
                    winning_move = "H"
                    winning_support = territory_supports
                else:
                    winning_move = related_move[0][0]
                    winning_support = related_attack_info[0][2]
            else:
                print("TEST 3")
                if "-NC" in self.moves[territory]["action"] or "-SC" in self.moves[territory]["action"]:
                    destination = self.moves[territory]["action"][-6:]
                else:
                    destination = self.moves[territory]["action"][-3:]
                if destination in self.moves:
                    if self.moves[destination]["action"] == "H" or self.moves[destination]["action"][0] == "S":
                        winning_move = "H"
                        winning_support = territory_supports
                    else:
                        checking_occupied_destination_attack = self.successful_move(destination)
                        if checking_occupied_destination_attack == "H" or checking_occupied_destination_attack == "S":
                            winning_move = "H"
                            winning_support = territory_supports
                        elif checking_occupied_destination_attack[0] == "A":
                            winning_move = self.moves[territory]["action"]
                            winning_support = territory_supports
                        else:
                            print("HELP")
                else:
                    winning_move = self.moves[territory]["action"]
                    winning_support = territory_supports
        else:
            winning_move = None
            winning_support = territory_supports
           # winning_move = self.moves[territory]["action"]
           # winning_support = territory_supports
        #SECTION III: Determine what to return
        #Return winning move (if it's run in support validity) or support count (if it's run in attack validity)
        if support_type == "S":
            return winning_move
        elif support_type == "A":
            return winning_support
        
    def check_cut_support_for_attack(self, origin, destination, potential_supports):          
        if potential_supports == "S {} A {}".format(destination, origin):
            supporting_territory = potential_supports["starting territory"]
            if "A {}".format(supporting_territory) in self.moves.keys():
                return True
            else:
                return False
