from OpenCV_Functions import *

'''
def imageBlur(image, ksize):
    size = ((ksize+1) * 2 - 1, (ksize+1) * 2 - 1)
    return cv2.blur(image, size)
def imageGaussianBlur(image, ksize, sigmaX, sigmaY):
    size = ((ksize+1) * 2 - 1, (ksize+1) * 2 - 1)
    return cv2.GaussianBlur(image, ksize=size, sigmaX=sigmaX, sigmaY=sigmaY)
'''

def nothing(x):
    pass


imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
backup = imageCopy(image)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('BlurSize', 'image', 0, 10, nothing)
cv2.createTrackbar('sigmaX', 'image', 0, 50, nothing)
cv2.createTrackbar('sigmaY', 'image', 0, 50, nothing)

switch = '0:Mean\n1:Gaussian'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    size = cv2.getTrackbarPos('BlurSize', 'image')
    sigmaX = cv2.getTrackbarPos('sigmaX', 'image')
    sigmaY = cv2.getTrackbarPos('sigmaY', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        image = imageBlur(backup, size)
    else:
        image = imageGaussianBlur(backup, size, sigmaX, sigmaY)
    

cv2.destroyAllWindows()
