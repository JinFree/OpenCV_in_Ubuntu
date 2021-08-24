from OpenCV_Functions import *


def nothing(x):
    pass


img = np.zeros((10, 10, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('R', 'image', 128, 255, nothing)
cv2.createTrackbar('G', 'image', 128, 255, nothing)
cv2.createTrackbar('B', 'image', 128, 255, nothing)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(100) & 0xFF == 27:
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    img[:] = [b, g, r]
cv2.destroyAllWindows()
