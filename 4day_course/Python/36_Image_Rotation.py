from OpenCV_Functions import *

'''
def imageRotation(image, center=None, angle=0.0, scale=1.0, size=None, flags=cv2.INTER_LINEAR):
    if center is None:
        rows, cols = image.shape[:2]
        center = (cols/2, rows/2)
    if size is None:
        rows, cols = image.shape[:2]
        size = (cols, rows)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, size, flags=flags)
'''

def nothing(x):
    pass


imagePath = "~/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
backup = np.copy(image)

height, width = image.shape[:2]
center_x = int(width * 0.5)
center_y = int(height * 0.5)

cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('Center_x', 'image', center_x, width, nothing)
cv2.createTrackbar('Center_y', 'image', center_y, height, nothing)
cv2.createTrackbar('angle: value-180', 'image', 180, 360, nothing)
cv2.createTrackbar('scale: value[\%]', 'image', 100, 200, nothing)
cv2.createTrackbar('size: value[\%]', 'image', 100, 200, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    x = cv2.getTrackbarPos('Center_x', 'image')
    y = cv2.getTrackbarPos('Center_y', 'image')
    angle = cv2.getTrackbarPos('angle: value-180', 'image')
    scale = cv2.getTrackbarPos('scale: value[\%]', 'image')
    size = cv2.getTrackbarPos('size: value[\%]', 'image')
    sw = cv2.getTrackbarPos(switch, 'image')
    modified_size = (int(width*size*0.01),int(height*size*0.01))
    if sw == 0:
        image = backup
    else:
        image = backup
        image = imageRotation(image, (x, y), angle-180, scale*0.01, modified_size)

cv2.destroyAllWindows()