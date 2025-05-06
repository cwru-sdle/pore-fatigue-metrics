from poremetrics import convex_perimeter, perimeter
from . import shapes
from . import parameters

def test_convex_less_than_actual_perimeter_star():
    star = shapes.make_star()
    convex = convex_perimeter(star)
    actual = perimeter(star)
    assert actual > convex
