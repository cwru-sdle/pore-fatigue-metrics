import numpy as np
import math
from .perimeter import get_perimeter
from .validate_data import validate

def circularity_area(binary_image: np.array) -> float:
    if not validate(binary_image):
        raise ValueError("This is not a valid image")
    shape_area = np.sum(binary_image)/255
    perimeter = get_perimeter(binary_image)
    circular_area = (perimeter**2)/(4*math.pi)
    return shape_area / circular_area
