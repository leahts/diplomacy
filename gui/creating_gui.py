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


#Display image function: inputs a .png file and outputs the image
def display_image(file, coordinate_info):
    map_layout = [
        [sg.Image(file, size =(600, 400))],
        [sg.Text("Imperial Diplomacy")]
    ]
    window = sg.Window("Imperial Diplomacy: Spring 1900", map_layout)
    """
    for coord_info in coordinate_info:
        shape = ImageDraw.Draw.rectangle(coord_info[1][0], coord_info[1][1])
        window["graph"].draw_image()
        window.update()
    """
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

#Retrieve map names and coordinates
map_raw = open("data/map_data.csv", "r")
map_raw = map_raw.readlines()[1:]
map_data = open_file.open_file(map_raw)
territory_coordinates = []
for line in map_data:
    line = line.split(",")
    name_coord = (line[0], line[-2])
    territory_coordinates.append(name_coord)
print(territory_coordinates)

#Display Map - thank you Kamran for the map
image_file = "data/kamrans_map.png"
display_image(image_file, territory_coordinates)
img = cv2.imread(image_file, 1)

#Get coordinates; from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
"""
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
