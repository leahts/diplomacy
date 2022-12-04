
#Imports
import cv2
import sys
from creating_gui import get_territory_and_coord
from creating_gui import create_dot
from creating_gui import display_image
from creating_gui import click_event
from creating_gui import run_click_event
from creating_gui import map_w_dots_png

#do fancy import from another directory (not sure if I'm using "directory" correctly)
sys.path.append("graph")
import parse_file

#Initialize data
map_raw = open("data/map_data.csv", "r")
image_file = "data/kamrans_map.png"

#Read map_data and add dots to map
map_raw = map_raw.readlines()[1:]
map_data = parse_file.parse_file(map_raw)

#Isolate the territory and coordinate data from map_data.csv
territory_and_coord = get_territory_and_coord(map_data)

#Create map with dots
map_w_dots = map_w_dots_png(territory_and_coord, image_file)

#Display map - thank you Kamran for the map
display_image(map_w_dots, territory_and_coord)

#Run image that allows user to click on location and get location in terms of (x, y) coordinates
run_click_event(image_file)