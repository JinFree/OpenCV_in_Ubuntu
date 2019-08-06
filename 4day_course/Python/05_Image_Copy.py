from OpenCV_Functions import *

'''
def imageCopy(src):
    return np.copy(src)
'''
imagePath = path_to_images()
image1 = imageRead(imagePath)
image2 = image1
image3 = imageCopy(image1)

imageShow('image1 before function', image1)
imageShow('image2 before function', image2)
imageShow('image3 before function', image3)

for i in range(image1.shape[1]):
    for j in range(image1.shape[0]):
        setPixel(image1, i, j, 255, 0)

imageShow('image1 after pixel modify', image1)
imageShow('image2 after pixel modify', image2)
imageShow('image3 after pixel modify', image3)

cv2.destroyAllWindows()

image1 = imageRead(imagePath, cv2.IMREAD_COLOR)
image2 = image1
image3 = imageCopy(image1)

imageShow('image1 before function', image1)
imageShow('image2 before function', image2)
imageShow('image3 before function', image3)

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

imageShow('image1 after function', image1)
imageShow('image2 after function', image2)
imageShow('image3 after function', image3)

cv2.destroyAllWindows()
