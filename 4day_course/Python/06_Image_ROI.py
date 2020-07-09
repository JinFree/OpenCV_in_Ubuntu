from OpenCV_Functions import *

'''
def CutRectROI(image, x1, y1, x2, y2):
    return image[y1:y2, x1:x2]
def PasteRectROI(image, x1, y1, dst):
    y2, x2 = image.shape[:2]
    dst[y1:y1+y2, x1:x1+x2]=image
    return dst
def makeBlackImage(image, color=False):
    height, width = image.shape[0], image.shape[1]
    if color is True:
        return np.zeros((height, width, 3), np.uint8)
    else:
        if len(image.shape) == 2:
            return np.zeros((height, width), np.uint8)
        else:
            return np.zeros((height, width, 3), np.uint8)
def fillPolyROI(image, points):
    if len(image.shape) == 2:
        channels = 1
    else:
        channels = image.shape[2]
    mask = makeBlackImage(image)
    ignore_mask_color = (255,) * channels
    cv2.fillPoly(mask, points, ignore_mask_color)
    return mask
def polyROI(image, points):
    mask = fillPolyROI(image, points)
    return cv2.bitwise_and(image, mask)
'''

import os
home = os.environ['HOME']
imagePath = home + "/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow('image', image)

roi_x1 = 192 
roi_y1 = 303
roi_x2 = 278
roi_y2 = 352
roi_rect = CutRectROI(image, roi_x1, roi_y1, roi_x2, roi_y2)
imageShow("roi_rect", roi_rect)

image2 = imageCopy(image)
roi_new_x1 = 310
roi_new_y1 = 334
image2 = PasteRectROI(roi_rect, roi_new_x1, roi_new_y1, image2)
imageShow("image2", image2)

roi_poly_01 = np.array([[(209,301), (188, 317), (197, 352), (278, 352), (278, 324), (251, 301)]], dtype=np.int32)
image_polyROI_01 = polyROI(image, roi_poly_01)
imageShow("image_polyROI_01", image_polyROI_01)

pt1 = (280, 302)
pt2 = (280, 329)
pt3 = (322, 329)
pt4 = (323, 301)
roi_poly_02 = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
image_polyROI_02 = polyROI(image, roi_poly_02)
imageShow("image_polyROI_02", image_polyROI_02)

cv2.destroyAllWindows()
