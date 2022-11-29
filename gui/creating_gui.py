# image_viewer.py
import io
import os
import PySimpleGUI as sg
from PIL import Image



image_file = "data/diplomacy_map_image.jpg"

map_layout = [
        [sg.Image(filename = image_file)], 
        [sg.Text("Imperial Diplomacy")]
    ]
window = sg.Window("Imperial Diplomacy: Spring 1900", map_layout)
while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    else:
        if os.path.exists(image_file):
            image = Image.open(image_file)
            image.thumbnail((1000, 1000))
            window[image_file].update()
    window.close()