import numpy as np
import cv2
from poremetrics import solidity
from . import shapes
from . import parameters

def test_circle():
    circle = shapes.make_circle()
    value = solidity(circle)
    assert value>parameters.LOWER_BOUND_SCALE
    assert value<parameters.UPPER_BOUND_SCALE
