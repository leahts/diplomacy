# image_viewer.py
import io
import os
import PySimpleGUI as sg
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import sys

#do fancy import from another directory (not sure if I'm using "directory" correctly)
sys.path.append("graph")
import open_file


def create_dot(coord_info_list, image_file):
    image = Image.open(image_file)
    for coord_info in coord_info_list:
        pos = coord_info[1]
        pos = pos.split(" ")
        x_pos = pos[0]
        y_pos = pos[1]
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        territory = coord_info[0]
        color_of_dot = image.getpixel((x_pos, y_pos))
        ellipse_dimensions = [(x_pos - 5, y_pos - 5), (x_pos + 5, y_pos + 5)]
        draw = ImageDraw.Draw(image, "RGBA")
        draw.ellipse(ellipse_dimensions, outline = (0, 0, 0, 255), fill = color_of_dot)
    return image

#Display image function: inputs a .png file and outputs the image
def display_image(file, coordinate_info):
    map_layout = [
        [sg.Image(file, size =(600, 400))],
        [sg.Text("Imperial Diplomacy")]
    ]
    window = sg.Window("Imperial Diplomacy: Spring 1900", map_layout)
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            break
        """if os.path.exists(file):
                image = Image.open(file)
                print("yes")
                image.resize((200, 200))
                window[file].update()"""
        window.close()
  
#From https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
#Thank you geeksforgeeks
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates on the Shell
        print(x, ' ', y)
        # displaying the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    
#Main Body

#Initialize
map_raw = open("data/map_data.csv", "r")
image_file = "data/kamrans_map.png"
territory_and_coord = []

#Read map_data and add dots to map
map_raw = map_raw.readlines()[1:]
map_data = open_file.open_file(map_raw)
for line in map_data:
    line = line.split(",")
    name_coord = (line[0], line[-2])
    territory_and_coord.append(name_coord)

#Create map with dots
map_w_dots = create_dot(territory_and_coord, image_file)
map_w_dots.save("data/map_w_dots.png", format = "png")
map_w_dots = "data/map_w_dots.png"

#Display Map - thank you Kamran for the map
display_image(map_w_dots, territory_and_coord)

#Get coordinates; from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
img = cv2.imread(image_file, 1)
"""
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

