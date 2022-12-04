import os
import PySimpleGUI as sg
from PIL import Image
from PIL import ImageDraw
import cv2

#Takes in the map_data.csv and returns territory and coordinates in a tuple
def get_territory_and_coord(data):
    territory_and_coord_list = []
    for line in data:
        line = line.split(",")
        name_coord = (line[0], line[-2])
        territory_and_coord_list.append(name_coord)
    return territory_and_coord_list

#Add dot to map
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
                image.resize((600, 400))
                window[file].update()"""
        window.close()

#From https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
#Thank you geeksforgeeks
#Creates an image that, when the mouse clicks on the image, outputs the coordinates of the click
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)

#Get coordinates; from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
#Allows user to click on location and get location in terms of (x, y) coordinates
def run_click_event(image):
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Save image as a png and return the png image
def map_w_dots_png(data_info, file):
    new_map = create_dot(data_info, file)
    new_map.save("data/map_w_dots.png", format = "png")
    new_map = "data/map_w_dots.png"
    return new_map

image_file = "data/kamrans_map.png"
img = cv2.imread(image_file, 1)
