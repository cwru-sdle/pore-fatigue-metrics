import numpy as np
from . import shapes
from . import parameters
from poremetrics import convexity

def test_circle():
    circle = shapes.make_circle()
    value = convexity(circle)
    assert value>parameters.LOWER_BOUND_SCALE
    assert value < parameters.UPPER_BOUND_SCALE
def test_oval():
    oval = shapes.make_oval()
    value = convexity(oval)
    assert value>parameters.LOWER_BOUND_SCALE
    assert value<parameters.UPPER_BOUND_SCALE
def test_star():
    star = shapes.make_star()
    value = convexity(star)
    assert value<parameters.LOWER_BOUND_SCALE
def test_star_comparison():
    more_points_star = shapes.make_star(num_points=10)
    fewer_points_star = shapes.make_star(num_points=4)
    more_points_value = convexity(more_points_star)
    fewer_points_value = convexity(fewer_points_star)
    assert more_points_value < fewer_points_value
