from OpenCV_Functions import *

'''
def addWeightedImage(image1, w1, imagw2, w2=None):
    if w2 is None:
        return cv2.addWeighted(image1, float(w1) * 0.01, imagw2, float(100 - w1) * 0.01, 0)
    else:
        return cv2.addWeighted(image1, w1 * 0.01, imagw2, w2 * 0.01, 0)
'''

def nothing(x):
    pass

imagePath_1 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
imagePath_2 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowLeft.jpg"
image_1 = imageRead(imagePath_1) 
image_2 = imageRead(imagePath_2) 

cv2.namedWindow('dst', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('W1', 'dst', 0, 100, nothing)
cv2.createTrackbar('W2', 'dst', 0, 100, nothing)

switch = '0:W2 OFF\n1:W2 On'
cv2.createTrackbar(switch, 'dst', 1, 1, nothing)
dst = imageCopy(image_1)

while True:
    cv2.imshow('dst', dst)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    w1 = cv2.getTrackbarPos('W1', 'dst')
    w2 = cv2.getTrackbarPos('W2', 'dst')
    s = cv2.getTrackbarPos(switch, 'dst')
    
    if s==0:
        dst = addWeightedImage(image_1, w1, image_2)
    else:
        dst = addWeightedImage(image_1, w1, image_2, w2)

cv2.destroyAllWindows()
