from utils.helper import GiveImage, NumberOctaves
from lowesalg import LowesKernelPyramid, LowesImagePyramid, LowesDOGPyramid
from extrama import AllOctaveExtrema, FinalExtremaLocations, LocatingExtremaPoints

def FirstStepSIFT(path_or_image, sigma_int, restrict_octave = 2, num_intervals=3):

    """This functions take all the parts implemented above to give the extrema points on image"""
    
    if type(path_or_image) == str :
        image = GiveImage(path_or_image)
    else:
        image = path_or_image
    num_octave = NumberOctaves(image.size, restrict_octave)
    kernel_pyramid = LowesKernelPyramid(sigma_int, num_octave, num_intervals)
    gaussian_pyramid = LowesImagePyramid(image, kernel_pyramid)
    DOG_pyramid = LowesDOGPyramid(gaussian_pyramid)
    total_extrema_locations = AllOctaveExtrema(DOG_pyramid)
    image_extrema_locations = FinalExtremaLocations(total_extrema_locations)
    print("The total no of scale-space extrema points are = ",len(image_extrema_locations))
    detected_extrema_on_image = LocatingExtremaPoints(image,image_extrema_locations)
    return detected_extrema_on_image