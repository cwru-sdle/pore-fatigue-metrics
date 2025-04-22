import pandas as pd
import cv2
def read_img(inp,column):
    input_df = pd.read_csv(inp.iloc[idx][column])
    path = input_df.iloc[0]['path']
    img = cv2.imread(path) #Read image, is color
    try:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Convert to Greyscale, removing masks if present
    except cv2.error:
        pass #It throws a generic error
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB) #Convert back to color
    print(path)
    print(inp.iloc[idx]['MPa'])
    return img
