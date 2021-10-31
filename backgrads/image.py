import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np

def render_image(backWidth, backDepth, filename, colours='full'):
    if colours == 'dark':
        startColour = list(np.random.choice(range(192), size=3))
        endColour = list(np.random.choice(range(192), size=3))
    elif colours == 'light':
        startColour = list(np.random.choice(range(128) + 127, size=3))
        endColour = list(np.random.choice(range(128) + 127, size=3))
    else:
        startColour = list(np.random.choice(range(256), size=3))
        endColour = list(np.random.choice(range(256), size=3))


    colourArray = get_gradient_3d(backWidth, backDepth, startColour, endColour, (True, False, False))

    im = Image.fromarray(np.uint8(colourArray))
    draw = ImageDraw.Draw(im)

    im.save(filename)


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result