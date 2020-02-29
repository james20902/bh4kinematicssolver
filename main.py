import numpy as np
import cv2
from modules import blur
 
hsvarray = None
upper =  np.array([49, 154, 255])
lower =  np.array([18, 46, 83])
 
variance = 10
 
#cappin
cap = cv2.VideoCapture(0)
 
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsvarray[y,x]
        # return upper, lower
        print([pixel[0], pixel[1], pixel[2]])
 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.setMouseCallback('Step 1: Blur', pick_color)
    hsvarray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    stepOne = blur.getSquareBlur(hsvarray, 5)
    #print("Upper and Lower Ranges:", upper, lower)
    stepTwo = cv2.inRange(stepOne, lower, upper)
    #stepThree = cv2
    # Display the resulting frame
    cv2.imshow('Step 1: Blur', stepOne)
    cv2.imshow('Step 2: inRange', stepTwo)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
#no cap
cap.release()
cv2.destroyAllWindows()
