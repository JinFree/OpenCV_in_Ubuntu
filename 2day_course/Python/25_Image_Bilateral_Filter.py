from OpenCV_Functions import *

'''
def imageBilateralFilter(image, size, sigmaColor, sigmaSpace):
    d = (size+1) * 2 - 1
    return cv2.bilateralFilter(image, d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
'''

def nothing(x):
    pass


imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
backup = imageCopy(image)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('BlurSize', 'image', 0, 10, nothing)
cv2.createTrackbar('sigmaColor', 'image', 0, 100, nothing)
cv2.createTrackbar('sigmaSpace', 'image', 0, 100, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    sigmaColor = cv2.getTrackbarPos('sigmaColor', 'image')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'image')
    size = cv2.getTrackbarPos('BlurSize', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 1:
        image = imageBilateralFilter(backup, size, sigmaColor, sigmaSpace)
    else:
        image = backup
    

cv2.destroyAllWindows()
