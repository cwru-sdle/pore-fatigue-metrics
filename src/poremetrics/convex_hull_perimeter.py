import cv2
import numpy as np

def convex_perimeter(binary_image:np.array) -> float:
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    convex_contour =  cv2.convexHull(contours[0])
    return cv2.arcLength(convex_contour, True)
