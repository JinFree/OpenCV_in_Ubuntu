from OpenCV_Functions import *

'''
def splitImage(image):
    return cv2.split(image)
def mergeImage(channel1, channel2, channel3):
    return cv2.merge((channel1, channel2, channel3))
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

b, g, r = splitImage(image)
imageShow("image_b", b)
imageShow("image_g", g)
imageShow("image_r", r)

image2 = mergeImage(b, g, r)
imageShow("image2", image2)

cv2.destroyAllWindows()
