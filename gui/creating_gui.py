# image_viewer.py
import io
import os
import PySimpleGUI as sg
from PIL import Image

#Functions
#Display image function: inputs a .png file and outputs the image
def display_image(file):
    map_layout = [
        [sg.Image(file, size =(700, 700))],
        [sg.Text("Imperial Diplomacy")]
    ]
    window = sg.Window("Imperial Diplomacy: Spring 1900", map_layout)
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED:
            break
        """elif 
            print("YES")
            if os.path.exists(file):
                image = Image.open(file)
                print("yes")
                image.resize((200, 200))
                window[file].update()"""
        window.close()

#Main Body
image_file = "data/kamrans_map.png"
display_image(image_file)