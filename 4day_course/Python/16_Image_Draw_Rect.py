from OpenCV_Functions import *

'''
def drawRect(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.rectangle(result, point1, point2, color, thickness, lineType)
'''

imagePath = "~/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow('image', image)


height = image.shape[0]
width = image.shape[1]
pt1 = (0, int(height * 0.6))
pt2 = (width, height) 


rect_01 = drawRect(image, pt1, pt2, (0, 0, 255), 5)
rect_02 = drawRect(image, pt1, pt2, (0, 255, 0), 0)
rect_03 = drawRect(image, pt1, pt2, (255, 0, 0), -1)

imageShow('rect_01', rect_01)
imageShow('rect_02', rect_02)
imageShow('rect_03', rect_03)

cv2.destroyAllWindows()
