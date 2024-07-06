import sys
import Create_Run_Map as create_map
import Map_Functions as funcs
#import urllib.request

#urllib.request.urlretrieve('https://github.com/leahts/diplomacy/blob/gui/data/kamrans_map.png', "map_from_github.png")

#map_link = "https://github.com/leahts/diplomacy/blob/1852164f98b9b5215cd13c77538a32267b095aff/data/kamrans_map.png"

#sys.path.append("data")
#import kamrans_map
#print(type("map_from_github.png"))
#create_map.display_image(map_link, "data")


create_database = funcs.create_sql_db("katherine", "P4$$word")
print(create_database)






