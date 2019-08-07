from OpenCV_Functions import *

'''
def imageDilation(image, kernel, iterations):
    return cv2.dilate(image, kernel=kernel, iterations=iterations)
def imageErosion(image, kernel, iterations):
    return cv2.erode(image, kernel=kernel, iterations=iterations)
def imageMorphologicalGradient(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    dilation = imageDilation(image, kernel, iterations)
    erosion = imageErosion(image, kernel, iterations)
    return dilation-erosion
def imageOpening(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    erosion = imageErosion(image, kernel, iterations)
    return imageDilation(erosion, kernel, iterations)
def imageClosing(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    dilation = imageDilation(image, kernel, iterations)
    return imageErosion(dilation, kernel, iterations)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath, cv2.IMREAD_GRAYSCALE) 
imageShow("image", image)

image_threshold = imageThreshold(image, 128, 255, cv2.THRESH_BINARY)
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], np.uint8)
image_Dilation = imageDilation(image_threshold, kernel, 1)
image_Erosion = imageErosion(image_threshold, kernel, 1)
image_Opening = imageOpening(image_threshold, 1)
image_Closing = imageClosing(image_threshold, 1)
image_Gradient = imageMorphologicalGradient(image_threshold)

imageShow("image_threshold", image_threshold)
imageShow("image_Dilation", image_Dilation)
imageShow("image_Erosion", image_Erosion)
imageShow("image_Opening", image_Opening)
imageShow("image_Closing", image_Closing)
imageShow("image_Gradient", image_Gradient)

cv2.destroyAllWindows()
