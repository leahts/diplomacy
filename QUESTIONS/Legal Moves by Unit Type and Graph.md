
Are legal moves by unit type (army/fleet) boiled down to these three if statements?
- If destination is coast, armies and fleets are allowed
- If destination is inland, only armies are allowed
- If destination is sea, only fleets are allowed

Checking this would be three consecutive if statements. This is a lot less convoluted than the previous code I had. I think previously I overcomplicated the legal moves. Since we can assumed the starting location of a unit is legal, we only need to check the destination (I think).

If these three if statements can be used to check legal moves, is there still a benefit to making the graph a weighted graph (over an unweighted graph) and if so what are those benefits?


I thought of this while struggling to think of a good way to implement the adjacency matrix lmao.