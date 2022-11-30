# image_viewer.py
import io
import os
import PySimpleGUI as sg
from PIL import Image
import cv2
import sys

#sys.path.append(/Users/katherinesweeney/Documents/diplomacy/graph/diplomacy_graph.py)
#import open_file

#Functions

#Display image function: inputs a .png file and outputs the image
def display_image(file):
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
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
    # checking for right mouse clicks    
 
 
    
#Main Body
#Thank you Kamran for the map
image_file = "data/kamrans_map.png"
#map_file = map_data.csv
display_image(image_file)
img = cv2.imread(image_file, 1)

#map_data = open_file(map_file)
#print(map_data)


"""
#only used to get coordinates; from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""