import numpy as np
import cv2

def open_image(image_path):
    return cv2.imread(image_path)

def save_image(image,name):
    cv2.imwrite(name,image)

r=np.sqrt(2)
a=(r-1)/(2*r)
b=(r+1)/(2*r)
img = open_image('C:/Users/mouli/stage_LM/opencv.png')
lg,clm,ch = img.shape
img2 = img[int(a*lg):int(b*lg),int(a*clm):int(b*clm),:]
save_image(img2,'C:/Users/mouli/stage_LM/test5.jpg')
