from poremetrics import unfilled_ratio
import cv2
import numpy as np
import pathlib

DATA_DIR = pathlib.Path(__file__).parent / "data"
filled_img = cv2.imread(str(DATA_DIR / "filled.png"),cv2.IMREAD_GRAYSCALE)
unfilled_img = cv2.imread(str(DATA_DIR / "unfilled.png"),cv2.IMREAD_GRAYSCALE)
mostly_filled = cv2.imread(str(DATA_DIR / "mostly_filled_donut.png"),cv2.IMREAD_GRAYSCALE)
mostly_unfilled = cv2.imread(str(DATA_DIR / "mostly_unfilled_donut.png"),cv2.IMREAD_GRAYSCALE)

def test_filled():
    assert unfilled_ratio(filled_img)==0
def test_unfilled():
    assert .98<=unfilled_ratio(unfilled_img)<=1
def test_compare():
    assert unfilled_ratio(mostly_unfilled)>unfilled_ratio(mostly_filled)
