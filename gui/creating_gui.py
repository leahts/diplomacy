#Imports
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

#Add dot to map; takes in the territories and coordinates and outputs the image file as a png
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
    image.save("data/map_w_dots.png", format = "png")
    updated_map = "data/map_w_dots.png"
    return updated_map

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

#Creates an arrow between two points and returns the map with the arrow as a png file
def create_arrow(image_file, p1, p2):
    black = (0, 0, 0)
    x1 = int(p1[0])
    y1 = int(p1[1])
    x2 = int(p2[0])
    y2 = int(p2[1])
    p1 = (x1, y1)
    p2 = (x2, y2)
    slope = (y2 - y1)/(x2 - x1)
    inverse_slope = (-1)/slope
    if x2 > x1:
        x3 = x2 - 10
    else:
        x3 = x2 + 10
    y3 = slope*(x3 - x1) + y1
    arrow_point1 = (x3 - 5, inverse_slope*(-5) + y3)
    arrow_point2 = (x3 + 5, inverse_slope*(5) + y3)
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)
    draw.line([p1, p2], fill = black, width = 2)
    draw.line([arrow_point1, p2], fill = black, width = 2)
    draw.line([arrow_point2, p2], fill = black, width = 2)
    image.save("data/map_w_arrow.png", format = "png")
    updated_map = "data/map_w_arrow.png"
    return updated_map


image_file = "data/kamrans_map.png"
img = cv2.imread(image_file, 1)
