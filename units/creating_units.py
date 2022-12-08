from PIL import Image
from PIL import ImageDraw

def unit_color(country):
    if country == "Austria":
        color = (255, 0, 0)
    return color

def create_unit(territory, unit_type, country, image_file):
    black = (0, 0, 0, 255)
    color = unit_color(country)
    image = Image.open(image_file)
    x_pos = territory[0]
    y_pos = territory[1]
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