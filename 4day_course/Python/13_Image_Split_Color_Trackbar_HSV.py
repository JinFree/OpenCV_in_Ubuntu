from OpenCV_Functions import *


def nothing(x):
    pass

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
image = convertColor(image, cv2.COLOR_BGR2HSV)

img = imageCopy(image)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('H_lower', 'image', 0, 360, nothing)
cv2.createTrackbar('S_lower', 'image', 0, 255, nothing)
cv2.createTrackbar('V_lower', 'image', 0, 255, nothing)
cv2.createTrackbar('H_upper', 'image', 0, 360, nothing)
cv2.createTrackbar('S_upper', 'image', 0, 255, nothing)
cv2.createTrackbar('V_upper', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    h_l = cv2.getTrackbarPos('H_lower', 'image')
    s_l = cv2.getTrackbarPos('S_lower', 'image')
    v_l = cv2.getTrackbarPos('V_lower', 'image')
    h_u = cv2.getTrackbarPos('H_upper', 'image')
    s_u = cv2.getTrackbarPos('S_upper', 'image')
    v_u = cv2.getTrackbarPos('V_upper', 'image')
    lower = np.array([h_l, s_l, v_l])
    upper = np.array([h_u, s_u, v_u])

    img = splitColor(image, lower, upper)
    img = convertColor(img, cv2.COLOR_HSV2BGR)
cv2.destroyAllWindows()