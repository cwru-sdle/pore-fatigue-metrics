from poremetrics import aspect_ratio
import numpy as np

array_size = 100

# Create a binary array filled with zeros (background)
binary_array = np.zeros((1,array_size, array_size), dtype=int)

# Define the size of the colored block and its position (center)
block_size = 40
center_start = (array_size - block_size) // 2
center_end = center_start + block_size

# Set the values in the center block to 1 (colored)
binary_array[center_start:center_end, center_start:center_end] = 1

assert aspect_ratio(binary_array)==1
