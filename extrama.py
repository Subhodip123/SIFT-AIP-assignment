import numpy as np
from PIL import ImageDraw

def OneOctaveExtrema(per_octave_DOG_array):

    """This is function will run on one octave images to find the scale space extrema
    A kernel size of 3x3x3 is chosen to compare each pixel extrema with the neighbouring one"""

    ##zero pad the image in 3 dimensions to take account of the edges in scale and space both
    per_octave_DOG_zero_padded = np.pad(
        per_octave_DOG_array, ((1, 1), (1, 1), (1, 1)), mode="constant"
    )
    run_on_scale, run_on_rows, run_on_columns = per_octave_DOG_array.shape
    per_octave_extrema_locations = []
    for scale in range(run_on_scale):
        sliced_in_scale_space = per_octave_DOG_zero_padded[scale : scale + 3, :, :]
        for row in range(run_on_rows):
            sliced_in_row_space = sliced_in_scale_space[:, row : row + 3, :]
            for column in range(run_on_columns):
                sliced_in_column_space = sliced_in_row_space[:, :, column : column + 3]
                kernel_space_max = np.max(sliced_in_column_space)
                kernel_space_min = np.min(sliced_in_column_space)
                center_kernel_pixel_val = sliced_in_column_space[1, 1, 1]
                if (center_kernel_pixel_val == kernel_space_max) or (
                    center_kernel_pixel_val == kernel_space_min
                ):
                    per_octave_extrema_locations.append(
                        (
                            scale,
                            row,
                            column,
                        )  # here this cordinates are in actual octave arrays not on the zero padded images. zero padding is only done to take account of the edge parts.
                    )
                else:
                    continue
    return per_octave_extrema_locations


def AllOctaveExtrema(total_DOG_pyramid):

    """This function is used for computing all the scale space extrema accross all the
    octaves"""

    total_extrema_locations = []
    for octave_idx in range(len(total_DOG_pyramid)):
        per_octave_DOG_array = total_DOG_pyramid[octave_idx]
        per_octave_extrema_locations = OneOctaveExtrema(per_octave_DOG_array)
        total_extrema_locations.append(per_octave_extrema_locations)
    return total_extrema_locations


def FinalExtremaLocations(total_extrema_locations):

    """This function gives all the list of points that are detected in all the octaves"""

    final_extrema_points = []
    for octave_idx in range(len(total_extrema_locations)):
        for _, loc_height, loc_width in total_extrema_locations[octave_idx]:
            final_extrema_points.append(
                (loc_width, loc_height)
            )  # the x,y is interchanged as per the image cordinates convention
    return final_extrema_points

def LocatingExtremaPoints(image, final_extrema_locations):

    """This function will draw the rectangle around the extrema points"""

    image_copied_for_highlight = image.copy()
    image_with_extrema_detected = ImageDraw.Draw(image_copied_for_highlight)
    for loc_width, loc_height in final_extrema_locations:
        image_with_extrema_detected.point((loc_width , loc_height ))

    return image_copied_for_highlight