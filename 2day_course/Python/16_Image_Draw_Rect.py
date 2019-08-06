from OpenCV_Functions import *

'''
def drawRect(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.rectangle(result, point1, point2, color, thickness, lineType)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

pt1 = (130, 197)
pt2 = (190, 259)

rect_01 = drawRect(image, pt1, pt2, (0, 0, 255), 5)
rect_02 = drawRect(image, pt1, pt2, (0, 0, 255), 0)
rect_03 = drawRect(image, pt1, pt2, (0, 0, 255), -1)

imageShow('rect_01', rect_01)
imageShow('rect_02', rect_02)
imageShow('rect_03', rect_03)

cv2.destroyAllWindows()