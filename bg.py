# from .image import render_image
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np


width = 1024
depth = 1024
colourRange = 'full' # ('dark', 'light', 'full')
filename = 'output.png'

def render_image(backWidth, backDepth, filename, colours='full'):
    if colourRange == 'dark':
        startColour = list(np.random.choice(range(128), size=3))
        endColour = list(np.random.choice(range(128), size=3))
    elif colourRange == 'light':
        startColourTemp = list(np.random.choice(range(128), size=3))
        endColourTemp = list(np.random.choice(range(128), size=3))
        startColour = [x+127 for x in startColourTemp]
        endColour = [x+127 for x in endColourTemp]
    else:
        startColour = list(np.random.choice(range(256), size=3))
        endColour = list(np.random.choice(range(256), size=3))

    hlist = list(np.random.choice([True, False], size=3))
    colourArray = get_gradient_3d(backWidth, backDepth, startColour, endColour, hlist)

    im = Image.fromarray(np.uint8(colourArray))
    draw = ImageDraw.Draw(im)

    im.save(filename)

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float64)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

render_image(width, depth, filename, 'full')