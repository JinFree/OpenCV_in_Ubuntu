from OpenCV_Functions import *

'''
def houghCircles(image, method=cv2.HOUGH_GRADIENT, dp = 1, minDist = 10, canny = 50, threshold = 30, minRadius = 0, maxRadius = 0):
    circles = cv2.HoughCircles(image, method, dp, minDist, param1=canny, param2=threshold, minRadius=minRadius, maxRadius=maxRadius)
    return circles
def drawHoughCircles(image, circles):
    result = imageCopy(image)
    if circles is None:
        return result
    for i in circles[0,:]:
        cv2.circle(result, (i[0],i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(result, (i[0],i[1]), 2, (0, 0, 255), -1)
    return result
'''

def nothing(x):
    pass


imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath)
backup_bgr = imageCopy(image)
backup = convertColor(backup_bgr, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('minDist', 'image', 0, 100, nothing)
cv2.createTrackbar('canny', 'image', 0, 100, nothing)
cv2.createTrackbar('threshold', 'image', 80, 100, nothing)
cv2.createTrackbar('minRadius', 'image', 0, 100, nothing)
cv2.createTrackbar('maxRadius', 'image', 0, 100, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    minDist = cv2.getTrackbarPos('minDist', 'image')
    canny = cv2.getTrackbarPos('canny', 'image')
    threshold = cv2.getTrackbarPos('threshold', 'image')
    minRadius = cv2.getTrackbarPos('minRadius', 'image')
    maxRadius = cv2.getTrackbarPos('maxRadius', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 1:
        circles = houghCircles(backup, cv2.HOUGH_GRADIENT, 1, minDist+1, canny+1, threshold+1, minRadius, maxRadius)
        image = drawHoughCircles(backup_bgr, circles)
    else:
        image = backup_bgr
    

cv2.destroyAllWindows()