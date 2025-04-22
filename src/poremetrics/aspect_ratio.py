import numpy as np
def calculate_aspect_ratio(mask):
    # Find the non-zero mask coordinates
    y_coords, x_coords = np.where(mask > 0)
    
    # Calculate the bounding box dimensions
    height = y_coords.max() - y_coords.min() + 1
    width = x_coords.max() - x_coords.min() + 1
    
    # Calculate the aspect ratio
    aspect_ratio = width / height
    return aspect_ratio