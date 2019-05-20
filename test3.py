import numpy as np
import cv2

def open_image(image_path):
    return cv2.imread(image_path)

def save_image(image,name):
    cv2.imwrite(name,image)
    
img = open_image('C:/Users/mouli/stage_LM/opencv.png')
lg,clm,ch = img.shape
img = cv2.line(img,(0,clm//2),(lg,clm//2),(0,255,0),3)
save_image(img,'C:/Users/mouli/stage_LM/test3.jpg')