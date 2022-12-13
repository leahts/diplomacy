#Imports
import cv2
import sys
from creating_gui import get_territory_and_coord #takes map_data.csv and returns (territory, coordinates)
from creating_gui import create_dot #create dot for each territory on map
from creating_gui import display_image #gui to display image
from creating_gui import click_event #image in which a mouse click gives the location of the mouse
from creating_gui import run_click_event #runs click_event function
from creating_gui import create_arrow #create arrow between two points

#Fancy import from another directory (not sure if I'm using "directory" correctly)
sys.path.append("graph")
import parse_file

#Initialize data
map_raw = open("data/map_data.csv", "r")
image_file = "data/kamrans_map.png"

spot1 = (65, 100)
spot2 = (250, 310)

#Call functions
map_data = parse_file.parse_file(map_raw)
territory_and_coord = get_territory_and_coord(map_data)
map_w_dots = create_dot(territory_and_coord, image_file)
display_image(map_w_dots)
#map_w_arrow = create_arrow(map_w_dots, spot1, spot2)
#display_image(map_w_arrow, territory_and_coord)
#run_click_event(image_file)

print(map_data)
