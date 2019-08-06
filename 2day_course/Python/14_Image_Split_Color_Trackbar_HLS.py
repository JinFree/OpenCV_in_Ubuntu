from OpenCV_Functions import *


def nothing(x):
    pass

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
image = convertColor(image, cv2.COLOR_BGR2HLS)

img = imageCopy(image)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('H_lower', 'image', 0, 360, nothing)
cv2.createTrackbar('L_lower', 'image', 0, 255, nothing)
cv2.createTrackbar('S_lower', 'image', 0, 255, nothing)
cv2.createTrackbar('H_upper', 'image', 0, 360, nothing)
cv2.createTrackbar('L_upper', 'image', 0, 255, nothing)
cv2.createTrackbar('S_upper', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    h_l = cv2.getTrackbarPos('H_lower', 'image')
    l_l = cv2.getTrackbarPos('L_lower', 'image')
    s_l = cv2.getTrackbarPos('S_lower', 'image')
    h_u = cv2.getTrackbarPos('H_upper', 'image')
    l_u = cv2.getTrackbarPos('L_upper', 'image')
    s_u = cv2.getTrackbarPos('S_upper', 'image')
    lower = np.array([h_l, l_l, s_l])
    upper = np.array([h_u, l_u, s_u])

    img = splitColor(image, lower, upper)
    img = convertColor(img, cv2.COLOR_HLS2BGR)
cv2.destroyAllWindows()