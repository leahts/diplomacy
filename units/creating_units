from PIL import Image
from PIL import ImageDraw

def unit_color(country):
    if country == "Austria":
        color = (255, 0, 0)

def create_unit(territory, country, image_file):
    color = unit_color(country)
    image = Image.open(image_file)
    x_pos = territory[0]
    y_pos = territory[1]
    x_pos = int(x_pos)
    y_pos = int(y_pos)
    ellipse_dimensions = [(x_pos - 5, y_pos - 5), (x_pos + 5, y_pos + 5)]
    draw = ImageDraw.Draw(image, "RGBA")
    draw.ellipse(ellipse_dimensions, outline = (0, 0, 0, 255), fill = color)
    image.save("data/map_w_units.png", format = "png")
    updated_map = "data/map_w_units.png"
    return updated_map