import cv2

def getBlobFrames():
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = 1
    params.blobColor = (255)
    params.minThreshold = 10
    params.maxThreshold = 220
    params.filterByArea = True
    params.minArea = min_area
    params.maxArea = max_area
    params.filterByCircularity = True
    params.minCircularity = circularity[0]
    params.maxCircularity = circularity[1]
    params.filterByConvexity = False
    params.filterByInertia = False
    detector = cv2.SimpleBlobDetector_create(params)
    return detector.detect(input)