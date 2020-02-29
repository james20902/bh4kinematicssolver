import numpy as np
import cv2
from modules import blur, HSVmagicwand

#cappin
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    hsvarray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.setMouseCallback("HSV", pick_color(array=hsvarray))

    modifiedFrame = blur.getSquareBlur(frame, 5)

    # Display the resulting frame
    cv2.imshow('frame', modifiedFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#no cap
cap.release()
cv2.destroyAllWindows()