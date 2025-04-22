import numpy as np
def find_area(mask: np.ndarray):
    total = 1
    for i in mask.shape:
        total = total*i
    active_class = np.max(mask)
    return np.sum(mask) / total*active_class
