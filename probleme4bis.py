import numpy as np
import cv2
import glob

rond = np.zeros((200, 200),np.uint8)
rond = cv2.circle(rond,(100,100),80,(255,255,255), -1)

def open_image(image):
    img = cv2.imread(image)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return imgray,img
    
def traitement(imgray):
    ret,thresh = cv2.threshold(imgray,160,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((10,10),np.uint8)
    opg = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    trt = cv2.morphologyEx(opg, cv2.MORPH_CLOSE, kernel)
    return trt
                
def mean_val(cnt,imgray,img):
    mask = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    return cv2.mean(img,mask = mask)

def est_rond(cnt):
    contours, hierarchy = cv2.findContours(rond,2,1)
    cnt2 = contours[0]
    ret = cv2.matchShapes(cnt,cnt2,1,0.0)
    return (ret < 0.1) 
    
    
def detecte_boutons(image):  
    imgray,img = open_image(image)
    trt = traitement(imgray)      
    contours, hierarchy = cv2.findContours(trt,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:    
        mv = mean_val(cnt,imgray,img)
        if mv[2] > 180 and mv[0]<110 and mv[1]<110:
            x,y,w,h = cv2.boundingRect(cnt)
            if w*h > 500 and est_rond(cnt):
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
#%%
files = glob.glob('C:/Users/mouli/stage_LM/images en pagaille/*')
for image in files:
    detecte_boutons(image)
