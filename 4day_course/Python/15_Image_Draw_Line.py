from OpenCV_Functions import *

'''
def drawLine(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.line(result, point1, point2, color, thickness, lineType)
'''

imagePath = "~/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow('image', image)

height = image.shape[0]
width = image.shape[1]
pt1 = (int(width * 0.4), int(height * 0.6))
pt2 = (int(width * 0.6), int(height * 0.6))
pt3 = (int(width), height)
pt4 = (0, height)

line = drawLine(image, pt1, pt2, (0, 0, 255), 5)
line = drawLine(line, pt2, pt3, (0, 0, 255), 5)
line = drawLine(line, pt3, pt4, (0, 0, 255), 5)
line = drawLine(line, pt4, pt1, (0, 0, 255), 5)

imageShow('line', line)

cv2.destroyAllWindows()
