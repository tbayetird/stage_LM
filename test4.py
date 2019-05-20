import numpy as np
import cv2

def open_video(video_path):
    return cv2.VideoCapture(video_path)

vid = open_video('C:/Users/mouli/stage_LM/survol_kayak.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('C:/Users/mouli/stage_LM/test4.mp4',fourcc, 20.0, (1920,1080))

while (vid.isOpened()):
    a, frame = vid.read()
    if a==True:
        lg,clm,ch = frame.shape
        frame = frame[:, :(clm//2),:]
        out.write(frame)
    else:
        break

vid.release
out.release