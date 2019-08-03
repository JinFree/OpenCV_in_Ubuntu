from OpenCV_Functions import *

road_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"

# cv2.IMREAD_COLOR
# Blue - Green - Red 순서의 3채널 이미지로 열림
image_color = imageRead(road_image_01, cv2.IMREAD_COLOR)

# cv2.IMREAD_GRAYSCALE
# 회색조 1채널로 열림
image_gray = imageRead(road_image_01, cv2.IMREAD_GRAYSCALE)

# cv2.IMREAD_UNCHANGED
# 1채널 회색조 이미지는 1채널로 열리고, 3채널 컬러 이미지는 3채널 BGR로 열림
image_origin = imageRead(road_image_01, cv2.IMREAD_COLOR)


# cv2.WINDOW_NORMAL: 좌표와 좌표의 RGB 값 확인 가능, 화면 크기 전환 가능 및 비율 유지
imageShow("image_color, cv2.WINDOW_NORMAL", image_color, cv2.WINDOW_NORMAL)

# cv2.WINDOW_AUTOSIZE : 좌표와 좌표의 RGB 값 확인 가능, 화면 크기 전환 불가능 및 비율 유지
imageShow("image_color, cv2.WINDOW_AUTOSIZE", image_color, cv2.WINDOW_AUTOSIZE)

# cv2.WINDOW_FREERATIO : 좌표와 좌표의 RGB 값 확인 가능, 화면 크기 전환 가능 및 비율 유지 안됨
imageShow("image_color, cv2.WINDOW_FREERATIO", image_color, cv2.WINDOW_FREERATIO)

# cv2.WINDOW_GUI_NORMAL : 좌표와 좌표의 RGB 값 확인 불가능, 화면 크기 전환 가능 및 비율 유지
imageShow("image_color, cv2.WINDOW_GUI_NORMAL", image_color, cv2.rWINDOW_GUI_NORMAL)

# cv2.WINDOW_GUI_EXPANDED : 좌표와 좌표의 RGB 값 확인 가능, 화면 크기 전환 가능 및 비율 유지
imageShow("image_color, cv2.WINDOW_GUI_EXPANDED", image_color, cv2.WINDOW_GUI_EXPANDED)

imageWrite("gray.jpg", image_gray)