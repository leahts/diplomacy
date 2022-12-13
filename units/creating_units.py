#Imports
from PIL import Image
from PIL import ImageDraw


"""
Function Purpose: update "map_w_units.png" to be the map with all of the units
Input: the map to be saved
Output: the updated map in a png format
"""
def update_map(map_to_save):
    map_to_save.save("data/map_w_units.png", format = "png")
    updated_map = "data/map_w_units.png"
    return updated_map


"""
Class Purpose: Create a unit
Inputs:
- country
- territory name (in abbreviation form)
- location 
- unit type (army or fleet)
- image file of map 
Output: an image file of the map with the unit
"""
class create_unit():

    def __init__(self, country, territory_name, unit_type, map_file, image_file):
        self.country = country
        self.territory = territory_name
        self.unit_type = unit_type
        self.image = image_file
        self.map_file = map_file
        
    """
    Function Purpose: obtain the coordinates of the territory
    Input: N/A
    Output: coordinate in the form of "x_pos y_pos"
    """
    def obtain_start_coord(self):
        for line in self.map_file:
            if line[0] == self.territory:
                coord = line[4]
                return coord

    """
    Function Purpose: determine color of units
    Input: N/A
    Output: color of the country
    """
    def unit_color(self):
        self.color = (0, 0, 0, 255)
        if self.country == "Austria":
            self.color = (184, 0, 0, 255)
        elif self.country == "UK":
            self.color = (245, 93, 214, 255)
        elif self.country == "Germany":
            self.color = (46, 31, 31, 255)
        elif self.country == "Italy":
            self.color = (2, 115, 17, 255)
        elif self.country == "France":
            self.color = (5, 70, 156, 255)
        elif self.country == "Turkey":
            self.color = (250, 250, 22, 255)
        elif self.country == "Russia":
            self.color = (157, 5, 245, 255)
        return self.color
    
    """
    Function Purpose: create the unit symbol on the map
    Input: N/A
    Output: an image with the unit displayed on the map    
    """
    def create_unit_symbol(self):
        black = (0, 0, 0, 255)
        self.image = Image.open(self.image)
        self.loc = self.obtain_start_coord()
        self.color = self.unit_color()
        self.loc = self.loc.split(" ")
        x_pos = self.loc[0]
        y_pos = self.loc[1]
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        if self.unit_type == "Army":
            ellipse_dimensions = [(x_pos - 5, y_pos - 5), (x_pos + 5, y_pos + 5)]
            draw = ImageDraw.Draw(self.image, "RGBA")
            draw.ellipse(ellipse_dimensions, outline = black, fill = self.color)
        elif self.unit_type == "Fleet":
            triangle_points = [(x_pos, y_pos + 7), (x_pos - 6, y_pos - 4), (x_pos + 6, y_pos - 4)]
            draw = ImageDraw.Draw(self.image, "RGBA")
            draw.polygon(triangle_points, outline = black, fill = self.color)
        self.image_updated = update_map(self.image)
        return self.image_updated