from OpenCV_Functions import *

'''
def drawLine(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.line(result, point1, point2, color, thickness, lineType)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

pt1 = (130, 197)
pt2 = (130, 259)
pt3 = (190, 259)
pt4 = (190, 197)

line = drawLine(image, pt1, pt2, (0, 0, 255), 5)
line = drawLine(line, pt2, pt3, (0, 0, 255), 5)
line = drawLine(line, pt3, pt4, (0, 0, 255), 5)
line = drawLine(line, pt4, pt1, (0, 0, 255), 5)

imageShow('line', line)

cv2.destroyAllWindows()
