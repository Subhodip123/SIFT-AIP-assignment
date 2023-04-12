##import some libraries for the implementation

import numpy as np
from PIL import Image, ImageFilter, ImageDraw
import matplotlib.pyplot as plt
from IPython.display import display


def GiveImage(path):

    """This takes the input path to read the image in the environment"""

    image = Image.open(path)
    return image

def DisplayImages(list_of_tuples, list_of_images):

    "This displays some images from the total image pyramid"

    for idx1, idx2 in list_of_tuples:
        display(list_of_images[idx1][idx2])

    return None

def NumberOctaves(image_size, restrict_octave):

    """Compute number of octaves in image pyramid. restrict_octave is hyper parameter that
    stops the octave according to the user so that the last image has enough size"""

    return int(round(np.log(min(image_size)) / np.log(2) - restrict_octave))

