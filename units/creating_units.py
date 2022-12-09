#Imports
from PIL import Image
from PIL import ImageDraw


"""
Function Purpose: to obtain the coordinates of the starting territories
Input: name of the territory and the file containing the starting units
Output: the coordinates of the territory
"""
def obtain_start_coord(territory_name, data_file):
    for line in data_file:
        if line[0] == territory_name:
            coord = line[4]
            return coord

"""
Function Purpose: determine color of units
Input: name of country
Output: color of the country
"""
def unit_color(country):
    color = (0, 0, 0, 255)
    if country == "Austria":
        color = (184, 0, 0, 255)
    elif country == "UK":
        color = (245, 93, 214, 255)
    elif country == "Germany":
        color = (46, 31, 31, 255)
    elif country == "Italy":
        color = (2, 115, 17, 255)
    elif country == "France":
        color = (5, 70, 156, 255)
    elif country == "Turkey":
        color = (250, 250, 22, 255)
    elif country == "Russia":
        color = (157, 5, 245, 255)
    else:
        print(country)
        color = (255, 255, 255, 255)
    return color

"""
Function Purpose: Create a unit
Input: 
    - the location of the territory
    - unit type (i.e. army of fleet)
    - the country
    - The map (i.e. map_w_dots.png for now)
Output: an image (png format) that contains the new unit on the image
"""
def create_unit(territory_location, unit_type, country, image_file):
    black = (0, 0, 0, 255)
    color = unit_color(country)
    image = Image.open(image_file)
    territory_location = territory_location.split(" ")
    x_pos = territory_location[0]
    y_pos = territory_location[1]
    x_pos = int(x_pos)
    y_pos = int(y_pos)
    if unit_type == "Army":
        ellipse_dimensions = [(x_pos - 5, y_pos - 5), (x_pos + 5, y_pos + 5)]
        draw = ImageDraw.Draw(image, "RGBA")
        draw.ellipse(ellipse_dimensions, outline = black, fill = color)
    elif unit_type == "Fleet":
        triangle_points = [(x_pos, y_pos + 7), (x_pos - 6, y_pos - 4), (x_pos + 6, y_pos - 4)]
        draw = ImageDraw.Draw(image, "RGBA")
        draw.polygon(triangle_points, outline = black, fill = color)
    return image

"""
Function Purpose: create the starting territories for the game
Input: 
    - file of starting territories => line[0] is country and file[1] is territory
    - image file of map (png format)
    - file of every territory (i.e. map_Data.csv)
Output: an updated map of the starting territories displayed on the map
"""
def create_starting_territories(territory_file, image_file, all_territories_file):
    country_units_dict = {}
    countries = []
    j = 0
    for line in territory_file:
        line[2] = line[2][0]
        country = line[0]
        countries.append(country)
    for country in countries:
        territory_and_type = []
        for line in territory_file:
            if line[0] == country:
                indiv_territory_and_type = (line[1], line[2])
                territory_and_type.append(indiv_territory_and_type)
                j += 1
        country_units_dict[country] = territory_and_type
    for country in countries:
        unit_info = country_units_dict.get(country)
        i = 0
        total_units = len(unit_info)
        while i < total_units:
            unit = unit_info[i][0]
            unit_type = unit_info[i][1]
            territory_loc = obtain_start_coord(unit, all_territories_file)
            if j == 0:
                map_w_new_unit = create_unit(territory_loc, unit_type, country, image_file)
                updated_map = update_map(map_w_new_unit)
            else:
                map_w_new_unit = create_unit(territory_loc, unit_type, country, "data/map_w_units.png")
                updated_map = update_map(map_w_new_unit)
            i += 1
    return updated_map

"""
Function Purpose: update "map_w_units.png" to be the map with all of the units
Input: the map to be saved
Output: the updated map in a png format
"""
def update_map(map_to_save):
    map_to_save.save("data/map_w_units.png", format = "png")
    updated_map = "data/map_w_units.png"
    return updated_map