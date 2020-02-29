import numpy as np
import cv2

def include_color(event,x,y,flags,param,array,upperoriginal,loweroriginal):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = array[y,x]
        
        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        return upper, lower

def exclude_color(event,x,y,flags,param,array,upperoriginal,loweroriginal):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = array[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        return upper, lower