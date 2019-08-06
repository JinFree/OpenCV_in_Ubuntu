from OpenCV_Functions import *

'''
def convertColor(image, flag=cv2.COLOR_BGR2GRAY):
    return cv2.cvtColor(image, flag)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

b, g, r = splitImage(image)
imageShow("b", b)
imageShow("g", g)
imageShow("r", r)

imageHSV = convertColor(image, cv2.COLOR_BGR2HSV)
imageShow("image.HSV", imageHSV)
h, s, v = splitImage(imageHSV)
imageShow("h", h)
imageShow("s", s)
imageShow("v", v)

imageHLS = convertColor(image, cv2.COLOR_BGR2HLS)
imageShow("imageHLS", imageHLS)
h2, l2, s2 = splitImage(imageHLS)
imageShow("h2", h2)
imageShow("l2", l2)
imageShow("s2", s2)

imageGray = convertColor(image, cv2.COLOR_BGR2GRAY)
imageShow("imageGray", imageGray)

cv2.destroyAllWindows()
