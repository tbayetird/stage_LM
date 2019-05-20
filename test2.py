import numpy as np
import cv2

def open_image(image_path):
    return cv2.imread(image_path)

def save_image(image,name):
    cv2.imwrite(name,image)
    
img = open_image('C:/Users/mouli/stage_LM/opencv.png')
blue = img[:,:,0]
img[:,:,0] = img [:,:,2]
img [:,:,2] = blue
save_image(img,'C:/Users/mouli/stage_LM/test2.jpg')

