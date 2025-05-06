from . import shapes
from . import parameters
from poremetrics import circularity_area

def test_circle():
    circle = shapes.make_circle()
    circularity = circularity_area(circle)
    assert circularity > parameters.LOWER_BOUND_SCALE
    assert circularity < parameters.UPPER_BOUND_SCALE
def test_oval_more_than_rectangle():
    oval = shapes.make_oval(x_axis = 100, y_axis = 200)
    rectangle = shapes.make_rectangle(x_length = 100,y_length=200)
    assert circularity_area(oval)>circularity_area(rectangle)
