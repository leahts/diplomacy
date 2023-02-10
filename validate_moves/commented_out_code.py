
#For attack_validity function
"""possible_cut_dict = {}
        for related_move in related_moves:
            related_support_count = 0
            possible_cut_territories = self.nodes[related_move]["neighbors"]
            for each_cut in possible_cut_territories:
                if each_cut in self.moves.keys():
                    if self.moves[each_cut]["action"][0] == "A {}".format(territory) or (self.moves[each_cut]["action"][0] == "S" and territory in self.moves[each_cut]["action"]):
                        possible_cut_dict[each_cut] = self.moves[each_cut]["action"]
            #Check if attack is valid
            if possible_cut_dict != None:
                if "A {}".format(territory) in possible_cut_dict:

                    related_attack = True
                    attack_support = self.support_validity(related_move, True, possible_cut_dict, "A")
                    if attack_support != None:
                        related_support_count = related_support_count + attack_support
                    related_attack_info.append([related_move, related_support_count])
                    support_counts.append(related_support_count)
            #Check if supporting a hold is valid
                elif "S {} H".format(territory) in possible_cut_dict:
                    #support_hold = self.support_validity(related_move, True, related_moves[related_move], possible_cut_dict, "A")
                    support_hold = self.support_validity(related_move, True, possible_cut_dict, "A")
                    if support_hold != None:
                        occupied_support_count = occupied_support_count + support_hold
                else:
                    occupied_support_count += 1
            print("related attack for {} is {}".format(territory, related_attack))
        if len(support_counts) > 0:
            attacks_w_most_support = []
            #Find the move(s) with the most support
            maximum_support = max(support_counts)
            for each_attack in related_attack_info:
                if each_attack[1] == maximum_support:
                    attacks_w_most_support.append(each_attack[0]
        if occupied:
            if related_attack:
                if len(attacks_w_most_support) > 1:
                    winning_move = action
                elif len(attacks_w_most_support) == 1:
                    winning_attacker = attacks_w_most_support[0]
                    winning_move = self.moves[winning_attacker]["action"]
                else:
                    winning_move = related_attack_info[0][0]
            #Check what to do if the unit moves to an occupied unit
            else:
                potential_winning_move = self.moves[territory]["action"]
                if potential_winning_move[0] == "A":
                    if "-NC" in potential_winning_move or "-SC" in potential_winning_move:
                        potential_territory = potential_winning_move[-6:]
                    else:
                        potential_territory = potential_winning_move[-3:]
                    #If the unit is occupied and tries to attack another occupied territory
                    #then it should hold
                    print("trying to test the territory", territory, potential_territory)
                    if potential_territory in self.moves.keys():
                        print("trying something else", potential_territory)
                        winning_move = self.successful_move(potential_territory)
                        print("WINNNING MOVE", winning_move)
                    else:
                        winning_move = None
                else:
                    winning_move = potential_winning_move"""

"""for related_move in related_moves:
            related_support_count = 0
            #check if the territory is being possibly attacked
            #changed possible_cut_territories to possible_attacking_territories
            #changed each_cut to possible_attack

            possible_attacking_territories = self.nodes[related_move]["neighbors"]
            print("the possible attacking territories on {} are".format(related_move), possible_attacking_territories)
            for possible_attack in possible_attacking_territories:
                if possible_attack in self.moves.keys():
                    print("checking possible attack on {}".format(related_move), possible_attack, self.moves[possible_attack]["action"])
                    if self.moves[possible_attack]["action"] == "A {}".format(related_move):
                        print("TEST")
                        possible_attack_dict[possible_attack] = self.moves[possible_attack]["action"]
                    elif self.moves[possible_attack]["action"][0] == "S" and related_move in self.moves[possible_attack]["action"]:
                        print("test!!!!!!!")
                        possible_attack_dict[possible_attack] = self.moves[possible_attack]["action"]
                    related_attack = True
            #Check if the possible attack on the territory is valid
            if possible_attack_dict != None:
                print("the possible attacks for {} are".format(territory), possible_attack_dict)
                if "A {}".format(territory) in possible_attack_dict:
                    related_attack = True
                    print("YES")
                    #checking support for attacks
                    attack_support = self.support_validity(related_move, True, possible_attack_dict, "A")
                    if attack_support != None:
                        related_support_count = related_support_count + attack_support
                    related_attack_info.append([related_move, related_support_count])
                    support_counts.append(related_support_count)
            #Check if supporting a hold is valid
                elif "S {} H".format(territory) in possible_attack_dict:
                    #support_hold = self.support_validity(related_move, True, related_moves[related_move], possible_cut_dict, "A")
                    support_hold = self.support_validity(related_move, True, possible_attack_dict, "A")
                    if support_hold != None:
                        occupied_support_count = occupied_support_count + support_hold
                else:
                    occupied_support_count += 1"""


#for support_validity function
"""
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
                        territory_supports += 1"""