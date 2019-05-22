import numpy as np
import cv2

imgray = cv2.imread('C:/Users/mouli/stage_LM/boutons_rouges.jpg',0)
img = cv2.imread('C:/Users/mouli/stage_LM/boutons_rouges.jpg')
ret,thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
opg = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(opg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    mask = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    mean_val = cv2.mean(img,mask = mask)
    if mean_val[0] < 120:
        x,y,w,h = cv2.boundingRect(cnt)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()