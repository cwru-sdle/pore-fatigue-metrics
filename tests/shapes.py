# %%
import numpy as np
import cv2
import skimage.draw
import os

def get_file_path(filename:str) -> str:
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    img_path = os.path.join(data_dir, filename)
    return img_path

def make_rectangle(array_size: int=1024,x_length:int=100,y_length:int=100) -> np.ndarray:
    if array_size<x_length:
        raise ValueError(f"The box x axis ({x_length}) is larger than the surrounding array ({array_size}).")
    if array_size<y_length:
        raise ValueError(f"The box y axis ({y_length}) is larger than the surrounding array ({array_size}).")
    array = np.zeros((array_size,array_size),dtype=np.uint8)
    x_start = (array_size-x_length) // 2
    x_end = x_start+x_length
    y_start = (array_size-y_length) // 2
    y_end = y_start + y_length
    array[x_start:x_end,y_start:y_end]=255
    return array

def make_circle(array_size:int=1024,radius:int=100) -> np.ndarray:
    if array_size<radius:
        raise ValueError(f"The circle radius ({radius}) is larger than the surrounding array ({array_size}).")
    center = (array_size // 2, array_size // 2)
    Y, X = np.ogrid[:array_size, :array_size] # Makes a column and row matrix where the element = the index
    dist_from_center = np.sqrt((Y - center[0])**2 + (X - center[1])**2) # For every x and y coordinate combination (ie: every element in the matrix), the distance from the center is found 
    return np.astype(np.where(dist_from_center <=radius, 255,0),np.uint8) # Where the distance is less than the radius, the array is set to positive (255, since its an unsigned interger)

def make_oval(array_size:int=1024,x_axis:int=100,y_axis:int=200):
    if array_size<x_axis:
        raise ValueError(f"The circle radius ({x_axis}) is larger than the surrounding array ({array_size}).")
    if array_size<y_axis:
        raise ValueError(f"The circle radius ({y_axis}) is larger than the surrounding array ({array_size}).")
    center = (array_size // 2, array_size // 2)
    Y, X = np.ogrid[:array_size, :array_size] # Makes a column and row matrix where the element = the index
    dist_from_center = ((Y - center[0])/y_axis)**2 + ((X - center[1])/x_axis)**2 # For every x and y coordinate combination (ie: every element in the matrix), the distance from the center is found 
    mask = dist_from_center <= 1 # Where the distance is less than the radius, the array is set to positive (255, since its an unsigned interger)
    return np.astype(np.where(dist_from_center<=1,255,0),np.uint8)

def make_star(array_size:int=1024,outer_radius:int=300, inner_radius:int=100,num_points:int=5) -> np.ndarray:
    img = np.zeros((array_size, array_size), dtype=np.uint8)
    pts = []
    angle = -np.pi / 2  # Start pointing up
    for i in range(num_points * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        x = int(array_size//2 + r * np.cos(angle))
        y = int(array_size//2 + r * np.sin(angle))
        pts.append([x, y])
        angle += np.pi / num_points
    pts = np.array(pts)
    return cv2.fillPoly(img, [pts], [255])

def make_equilateral_triangle(array_size:int=1024,base:int=300,height:int=400):
    p1 = np.array([array_size//2-base//2,array_size//2-height//2])
    p2 = p1 + np.array([0,base])
    p3 = p1 + np.array([height,base//2])
    polygon = np.array([p1,p2,p3])
    mask = skimage.draw.polygon2mask(polygon=polygon,image_shape=(array_size,array_size))
    return mask.astype(np.uint8)*255
