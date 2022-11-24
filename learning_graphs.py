#insert your code below


class nodes():
    
    def __init__(self, territory, adj_territories):
        self.territory = territory
        self.nbrs = adj_territories
        
    def check_dot(self, has_dot):
        print(self.territory, self.nbrs)
        if has_dot == "dot":
            print("{} has a dot".format(self.territory))
        else:
            print("{} does not have a dot".format(self.territory))
            
imperial_map = {
    "Tyr": ["Vie", "Tri", "Boh"],
    "Vie": ["Tyr", "Boh", "Tri", "Gal"],
    "Mun": ["Boh", "Tyr", "Bur", "Sil"]
}

imperial_dots = {
"Tyr": "no dot",
"Vie": "dot",
"Mun": "dot"
}

for (key1, key2) in zip(imperial_map, imperial_dots):
    indiv_node = nodes(key1, imperial_map[key1])
    dot_status = indiv_node.check_dot(imperial_dots[key2])
