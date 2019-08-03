from OpenCV_Functions import *

'''
def getPixel(image, x, y, c=None):
    return image[y, x, c]
def setPixel(image, x, y, value, c=None):
    image[y, x, c] = value
    return image
'''

imagePath = path_to_images()
image = imageRead(imagePath)
imageShow("Opened Image", image)

x = 100
y = 200

pxvalue = getPixel(image, x, y)
print("Pixel value in {}, {}: {}".format(x, y, pxvalue))

pxvalue_b = getPixel(image, x, y, 0)
pxvalue_g = getPixel(image, x, y, 1)
pxvalue_r = getPixel(image, x, y, 2)
print("Pixel value in {}, {}: b={}, g={}, r={}".format(x, y, pxvalue_b, pxvalue_g, pxvalue_r))

for i in range(x, x+100):
    for j in range(y, y+200):
        image = setPixel(image, i, j, [(i-100)*1.2, 0, 0])
imageShow("image", image)

for i in range(x, x+100):
    for j in range(y, y+200):
        image = setPixel(image, i, j, [0, (i-100)*1.2, 0])
imageShow("image", image)

for i in range(0, image.shape[1]):
    image = setPixel(image, i, y, 0, 0)
    image = setPixel(image, i, y, 255, 1)
    image = setPixel(image, i, y, 0, 2)
imageShow("image", image)

for j in range(0, image.shape[0]):
    image = setPixel(image, x, j, [255, 0, 0])
imageShow("image", image)

pxvalue = getPixel(image, x, y)
print("Pixel value in {}, {}: {}".format(x, y, pxvalue))

pxvalue_b = getPixel(image, x, y, 0)
pxvalue_g = getPixel(image, x, y, 1)
pxvalue_r = getPixel(image, x, y, 2)
print("Pixel value in {}, {}: b={}, g={}, r={}".format(x, y, pxvalue_b, pxvalue_g, pxvalue_r))

cv2.destroyAllWindows()