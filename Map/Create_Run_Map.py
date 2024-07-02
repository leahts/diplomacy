from PIL import Image
from PIL import ImageDraw

def display_image (image_file):
    open_image = Image.open(image_file)
    open_image.show()
    return open_image