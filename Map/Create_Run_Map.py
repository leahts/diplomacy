from PIL import Image
from PIL import ImageDraw
import urllib.request
from io import StringIO

def display_image(image_link, image_file_path):

    data = findImage(image_link, image_file_path)
    # <type 'str'>
    img = Image.open(StringIO(data))
    img.show()
    return img
    #print('Image downloaded from url: {} and saved to: {}.'.format(url, image_file_path))



"""
def display_image (image_link):
    print(image_link)
    urllib.request.urlretrieve(image_link, "github_map.png")
    print(type("github_map.png"))
    open_image = Image.open("github_map.png")
    #open_image.thumbnail((5000, 1000))
    #open_image.save("resized_map.jpg")
    open_image.show()
    return open_image
"""