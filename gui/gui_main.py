#Imports
import cv2
import sys
from creating_gui import get_territory_and_coord #takes map_data.csv and returns (territory, coordinates)
from creating_gui import create_dot #create dot for each territory on map
from creating_gui import display_image #gui to display image
from creating_gui import click_event #image in which a mouse click gives the location of the mouse
from creating_gui import run_click_event #runs click_event function
from creating_gui import map_w_dots_png #saves map (that has the dots on it) as a png and returns that map

#Fancy import from another directory (not sure if I'm using "directory" correctly)
sys.path.append("graph")
import parse_file

#Initialize data and read the map_data.csv file
map_raw = open("data/map_data.csv", "r")
map_raw = map_raw.readlines()[1:]
image_file = "data/kamrans_map.png"

#Call Functions
map_data = parse_file.parse_file(map_raw)
territory_and_coord = get_territory_and_coord(map_data)
map_w_dots = map_w_dots_png(territory_and_coord, image_file)
display_image(map_w_dots, territory_and_coord)
#run_click_event(image_file)
