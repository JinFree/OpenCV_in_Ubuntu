from OpenCV_Functions import *

'''
def cannyEdge(image, threshold1=100, threshold2=200):
    return cv2.Canny(image, threshold1, threshold2) 
'''

def nothing(x):
    pass


imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
backup = imageCopy(image)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('threshold1', 'image', 0, 200, nothing)
cv2.createTrackbar('threshold2', 'image', 100, 400, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    threshold1 = cv2.getTrackbarPos('threshold1', 'image')
    threshold2 = cv2.getTrackbarPos('threshold2', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 1:
        image = cannyEdge(backup, threshold1, threshold2)
    else:
        image = backup

cv2.destroyAllWindows()
