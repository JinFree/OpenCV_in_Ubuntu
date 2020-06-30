from OpenCV_Functions import *

'''
def imageTranslation(image, size=None, dx=0.0, dy=0.0, flags=cv2.INTER_LINEAR):
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    if size is None:
        rows, cols = image.shape[:2]
        size = (cols, rows)
    return cv2.warpAffine(image, M, size, flags=flags)
'''

imagePath = "~/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
height, width = image.shape[:2]
print(height, width)

dx, dy = 100, 200
size = (width+dx, height+dy)
image_Translation_01 = imageTranslation(image, size=size, dx=dx, dy=dy)
image_Translation_02 = imageTranslation(image_Translation_01, size=(width, height), dx=dx, dy=dy, flags=cv2.WARP_INVERSE_MAP)
image_Translation_03 = imageTranslation(image_Translation_01, size=(width, height), dx=-dx, dy=-dy)

imageShow("image", image)
imageShow("image_Translation_01", image_Translation_01)
imageShow("image_Translation_02", image_Translation_02)
imageShow("image_Translation_03", image_Translation_03)

cv2.destroyAllWindows()