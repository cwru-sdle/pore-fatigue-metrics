import numpy as np
import cv2
from .validate_data import validate
from .convex_hull_perimeter import convex_perimeter
from .perimeter import get_perimeter

def convexity(binary_image:np.array)->float:
    if not validate(binary_image):
        raise ValueError("not valid iamge")
    return convex_perimeter(binary_image) / get_perimeter(binary_image)
