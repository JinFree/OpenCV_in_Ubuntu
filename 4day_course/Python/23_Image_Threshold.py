from OpenCV_Functions import *

'''
def imageThreshold(image, thresh=128, maxval=255, type=cv2.THRESH_BINARY):
    _, res = cv2.threshold(image, thresh=thresh, maxval=maxval, type=type)
    return res
'''

image = np.zeros((512, 512), np.uint8)
for i in range(0, 512):
    for j in range(0, 256):
        roadColor = setPixel(image, i, j, j)
    for j in range(256, 512):
        roadColor = setPixel(image, i, j, 256-j)
imageShow("image", image)

image_THRESH_BINARY = imageThreshold(image, 128, 255, cv2.THRESH_BINARY)
imageShow("image_THRESH_BINARY", image_THRESH_BINARY)

image_THRESH_BINARY_INV = imageThreshold(image, 128, 255, cv2.THRESH_BINARY_INV)
imageShow("image_THRESH_BINARY_INV", image_THRESH_BINARY_INV)

image_THRESH_TRUNC = imageThreshold(image, 128, 255, cv2.THRESH_TRUNC)
imageShow("image_THRESH_TRUNC", image_THRESH_TRUNC)

image_THRESH_TOZERO = imageThreshold(image, 128, 255, cv2.THRESH_TOZERO)
imageShow("image_THRESH_TOZERO", image_THRESH_TOZERO)

image_THRESH_TOZERO_INV = imageThreshold(image, 128, 255, cv2.THRESH_TOZERO_INV)
imageShow("image_THRESH_TOZERO_INV", image_THRESH_TOZERO_INV)

cv2.destroyAllWindows()
