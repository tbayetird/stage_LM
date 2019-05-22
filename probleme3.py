import numpy as np
import cv2

def open_image(image):
    img = cv2.imread(image)
    img2 = cv2.imread(image)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return imgray,img,img2
    
def traitement(imgray):
    ret,thresh = cv2.threshold(imgray,160,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((10,10),np.uint8)
    opg = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    trt = cv2.morphologyEx(opg, cv2.MORPH_CLOSE, kernel)
    return trt

def rempli_contours(trt,img):
    contours, hierarchy = cv2.findContours(trt,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        mask = np.zeros(trt.shape,np.uint8)
        cv2.drawContours(mask,[cnt],0,255,-1)
        pixelpoints = np.transpose(np.nonzero(mask))
        for pxl in pixelpoints:
            x=pxl[0]
            y=pxl[1]
            if (trt[x,y] < 50):
                trt[x,y] = 255
                img[x,y] = [0,0,255]
                
def mean_val(cnt,imgray,img):
    mask = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    return cv2.mean(img,mask = mask)

def compte_boutons(image):  
    imgray,img,img2 = open_image(image)
    trt = traitement(imgray) 
    rempli_contours(trt,img)      
    contours, hierarchy = cv2.findContours(trt,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    s=0
    for cnt in contours:    
        mv = mean_val(cnt,imgray,img)
        if mv[0] < 75 and mv[0] > 10:
            s+=1
            x,y,w,h = cv2.boundingRect(cnt)
            img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',trt)
    cv2.waitKey()
    cv2.imshow('image',img2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return s