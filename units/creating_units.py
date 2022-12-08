from PIL import Image
from PIL import ImageDraw

def unit_color(country):
    if country == "Austria":
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)
    return color

def create_unit(territory_location, unit_type, country, image_file):
    black = (0, 0, 0, 255)
    color = unit_color(country)
    image = Image.open(image_file)
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
    image.save("data/map_w_units.png", format = "png")
    updated_map = "data/map_w_units.png"
    return updated_map

def obtain_coord(territory_name, data_file):
    for line in data_file:
        if line[0] == territory_name:
            coord = line[4]
            return coord

def create_starting_territories(territory_file, image_file, all_territories_file):
    country_units_dict = {}
    countries = []
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
        country_units_dict[country] = territory_and_type
    for country in countries:
        unit_info = country_units_dict.get(country)
        i = 0
        total_units = len(unit_info)
        while i < total_units:
            unit = unit_info[i][0]
            unit_type = unit_info[i][1]
            territory_loc = obtain_coord(unit, all_territories_file)
            print(territory_loc)
            new_unit = create_unit(territory_loc, unit_type, country, image_file)
            i += 1
