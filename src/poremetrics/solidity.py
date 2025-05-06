import numpy as np
import cv2
from .validate_data import validate

def solidity(binary_image:np.array) -> float:
    if not validate(binary_image):
        raise ValueError("Not a valid image.")
    area = np.sum(binary_image)/255
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    convex_contour = cv2.convexHull(contours[0])
    convex_area = cv2.contourArea(convex_contour)
    return area / convex_area
