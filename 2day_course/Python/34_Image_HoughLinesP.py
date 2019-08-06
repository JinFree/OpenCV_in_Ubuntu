from OpenCV_Functions import *

'''
def houghLinesP(image, rho=1.0, theta=np.pi/180, threshold=100, minLineLength=10, maxLineGap=100):
    return cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)
def drawHoughLinesP(image, lines):
    result = imageCopy(image)
    if len(image.shape) == 2:
        result = convertColor(image, cv2.COLOR_GRAY2BGR)
    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 3)
    return result
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow("image", image)

image_edge = cannyEdge(image, 100, 200)
lines = houghLinesP(image_edge, 1, np.pi/180, 100, 10, 50)
image_lines = drawHoughLinesP(image, lines)
imageShow("image_edge", image_edge)
imageShow("image_lines", image_lines)

cv2.destroyAllWindows()
