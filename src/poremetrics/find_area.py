import numpy as np
def find_area(mask):
    total = 1
    for i in mask.shape:
        total = total*i
    return np.sum(mask) / total