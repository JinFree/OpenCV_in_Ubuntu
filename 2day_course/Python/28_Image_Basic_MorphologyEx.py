from OpenCV_Functions import *

'''
def imageMorphologyKernel(flag=cv2.MORPH_RECT, size=5):
    return cv2.getStructuringElement(flag, (size, size))    
def imageMorphologyEx(image, op, kernel, iterations=1):
    return cv2.morphologyEx(image, op=op, kernel=kernel, iterations=iterations)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath, cv2.IMREAD_GRAYSCALE) 
imageShow("image", image)


image_Threshold = imageThreshold(image, 128, 255, cv2.THRESH_BINARY)
MORPH_RECT = imageMorphologyKernel(cv2.MORPH_RECT, 5)
MORPH_ELLIPSE = imageMorphologyKernel(cv2.MORPH_ELLIPSE, 5)
MORPH_CROSS = imageMorphologyKernel(cv2.MORPH_CROSS, 5)

image_Open_RECT = imageMorphologyEx(image_Threshold, cv2.MORPH_OPEN, MORPH_RECT)
image_Open_ELLIPSE = imageMorphologyEx(image_Threshold, cv2.MORPH_OPEN, MORPH_ELLIPSE)
image_Open_CROSS = imageMorphologyEx(image_Threshold, cv2.MORPH_OPEN, MORPH_CROSS)

imageShow("image_Threshold", image_Threshold)
imageShow("MORPH_RECT", MORPH_RECT)
imageShow("image_Open_RECT", image_Open_RECT)
imageShow("MORPH_ELLIPSE", MORPH_ELLIPSE)
imageShow("image_Open_ELLIPSE", image_Open_ELLIPSE)
imageShow("MORPH_CROSS", MORPH_CROSS)
imageShow("image_Open_CROSS", image_Open_CROSS)

cv2.destroyAllWindows()

image_Close_RECT = imageMorphologyEx(image_Threshold, cv2.MORPH_CLOSE , MORPH_RECT)
image_Close_ELLIPSE = imageMorphologyEx(image_Threshold, cv2.MORPH_CLOSE, MORPH_ELLIPSE)
image_Close_CROSS = imageMorphologyEx(image_Threshold, cv2.MORPH_CLOSE, MORPH_CROSS)

imageShow("image_Threshold", image_Threshold)
imageShow("MORPH_RECT", MORPH_RECT)
imageShow("image_Close_RECT", image_Close_RECT)
imageShow("MORPH_ELLIPSE", MORPH_ELLIPSE)
imageShow("image_Close_ELLIPSE", image_Close_ELLIPSE)
imageShow("MORPH_CROSS", MORPH_CROSS)
imageShow("image_Close_CROSS", image_Close_CROSS)

cv2.destroyAllWindows()
 
image_Gradient_RECT = imageMorphologyEx(image_Threshold, cv2.MORPH_GRADIENT , MORPH_RECT)
image_Gradient_ELLIPSE = imageMorphologyEx(image_Threshold, cv2.MORPH_GRADIENT , MORPH_ELLIPSE)
image_Gradient_CROSS = imageMorphologyEx(image_Threshold, cv2.MORPH_GRADIENT , MORPH_CROSS)

imageShow("image_Threshold", image_Threshold)
imageShow("MORPH_RECT", MORPH_RECT)
imageShow("image_Gradient_RECT", image_Gradient_RECT)
imageShow("MORPH_ELLIPSE", MORPH_ELLIPSE)
imageShow("image_Gradient_ELLIPSE", image_Gradient_ELLIPSE)
imageShow("MORPH_CROSS", MORPH_CROSS)
imageShow("image_Gradient_CROSS", image_Gradient_CROSS)

cv2.destroyAllWindows()

