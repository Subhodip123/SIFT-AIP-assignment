import numpy as np
from PIL import ImageFilter

def LowesKernelPyramid(sigma_init, num_octaves, num_intervals=3):

    """Generate list of list gaussian kernels at which to blur the input image for all the octaves."""

    total_sigma_pyramid = []
    num_filters_per_octave = num_intervals + 3
    for octave_idx in range(num_octaves):
        per_octave_sigma_pyramid = [0]
        for sigma_idx in range(1, num_filters_per_octave):
            current_sigma = (
                (2 ** ((sigma_idx - 1) / num_intervals)) * sigma_init * (octave_idx + 1)
            )
            per_octave_sigma_pyramid.append(current_sigma)
        total_sigma_pyramid.append(per_octave_sigma_pyramid)

    return total_sigma_pyramid


def LowesImagePyramid(img, total_sigma_pyramid):

    """This returns a list of list of gaussian blurred images for each octave"""

    total_image_pyramid = []
    for octave_idx in range(len(total_sigma_pyramid)):
        per_octave_image_pyramid = []
        new_width = int(img.width / (2**octave_idx))
        new_height = int(img.height / (2**octave_idx))
        resized_img = img.resize((new_width, new_height))
        for sigma in total_sigma_pyramid[octave_idx]:
            blurred_img = resized_img.filter(ImageFilter.GaussianBlur(radius=sigma))
            per_octave_image_pyramid.append(blurred_img)
        total_image_pyramid.append(per_octave_image_pyramid)

    return total_image_pyramid


def LowesDOGPyramid(total_image_pyramid):

    """This converts each PIL image as numpy array for each octave level and then perform the DOG
    operation at each level"""

    total_DOG_pyramid = []
    for octave_idx in range(len(total_image_pyramid)):
        per_octave_array_pyramid = []
        for img in total_image_pyramid[octave_idx]:
            img_array = np.asfarray(img)
            per_octave_array_pyramid.append(img_array)
        per_octave_DOG_array = np.diff(np.array(per_octave_array_pyramid), axis=0)
        total_DOG_pyramid.append(per_octave_DOG_array)

    return total_DOG_pyramid
