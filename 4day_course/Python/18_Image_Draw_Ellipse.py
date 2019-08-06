from OpenCV_Functions import *

'''
def drawEllipse(image, center, axis, angle, startAngle, endAngle, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.ellipse(result, center, axis, angle, startAngle, endAngle, color, thickness, lineType)
'''


def nothing(x):
    pass


imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
backup = np.copy(image)

height = image.shape[0]
width = image.shape[1]

cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('Center_x', 'image', 0, width, nothing)
cv2.createTrackbar('Center_y', 'image', 0, height, nothing)
cv2.createTrackbar('axes_x', 'image', 0, width, nothing)
cv2.createTrackbar('axes_y', 'image', 0, height, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('angle', 'image', 0, 360, nothing)
cv2.createTrackbar('startAngle', 'image', 0, 360, nothing)
cv2.createTrackbar('endAngle', 'image', 0, 360, nothing)
cv2.createTrackbar('Thickness', 'image', 0, 255, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while True:
    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    x = cv2.getTrackbarPos('Center_x', 'image')
    y = cv2.getTrackbarPos('Center_y', 'image')
    axes_x = cv2.getTrackbarPos('axes_x', 'image')
    axes_y = cv2.getTrackbarPos('axes_y', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    angle = cv2.getTrackbarPos('angle', 'image')
    startAngle = cv2.getTrackbarPos('startAngle', 'image')
    endAngle = cv2.getTrackbarPos('endAngle', 'image')
    thickness = cv2.getTrackbarPos('Thickness', 'image')
    thickness = thickness-1
    sw = cv2.getTrackbarPos(switch, 'image')

    if sw == 0:
        image = backup
    else:
        image = backup
        image = drawEllipse(image, (x, y), (axes_x, axes_y), angle, startAngle, endAngle, (b, g, r), thickness)

cv2.destroyAllWindows()