import cv2
import numpy as np
def extract_largest_object(img,points_list):
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    for points in points_list:
        cv2.fillPoly(
            mask,
            [np.array(points, dtype=np.int32)],
            255
        )
    img_object, largest_object_mask = process_mask(mask)
    return largest_object_mask