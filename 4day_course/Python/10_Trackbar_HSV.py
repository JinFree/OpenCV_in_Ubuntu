from OpenCV_Functions import *


def nothing(x):
    pass


img = np.zeros((10, 10, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('H', 'image', 0, 360, nothing)
cv2.createTrackbar('S', 'image', 0, 255, nothing)
cv2.createTrackbar('V', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    img[:] = [h, s, v]
    img = convertColor(img, cv2.COLOR_HSV2BGR)
cv2.destroyAllWindows()