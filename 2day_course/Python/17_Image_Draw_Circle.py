from OpenCV_Functions import *

'''
def drawCircle(image, center, radius, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.circle(result, center, radius, color, thickness, lineType)
'''

imagePath = "/home/opencv/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

center_01 = (160, 230)
center_02 = (160, 320)
center_03 = (160, 410) 
radius = 32

circle_01 = drawCircle(image, center_01, radius, (0, 0, 255), 5)
circle_02 = drawCircle(image, center_02, radius, (0, 255, 255), 0)
circle_03 = drawCircle(image, center_03, radius, (0, 255, 0), -1)

imageShow('circle_01', circle_01)
imageShow('circle_02', circle_02)
imageShow('circle_03', circle_03)

cv2.destroyAllWindows()
