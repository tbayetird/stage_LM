import numpy as np
import cv2

def open_image(image_path):
    return cv2.imread(image_path)

def save_image(image,name):
    cv2.imwrite(name,image)
    
img = open_image('C:/Users/mouli/stage_LM/opencv.png')
img = cv2.flip(img,0)
save_image(img,'C:/Users/mouli/stage_LM/test1.jpg')

