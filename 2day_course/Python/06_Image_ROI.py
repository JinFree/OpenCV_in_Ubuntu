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

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

roi_x1 = 94 
roi_y1 = 274
roi_x2 = 224
roi_y2 = 366
roi_rect = CutRectROI(image, roi_x1, roi_y1, roi_x2, roi_y2)
imageShow("roi_rect", roi_rect)

image2 = imageCopy(image)
roi_new_x1 = 95
roi_new_y1 = 367
image2 = PasteRectROI(roi_rect, roi_new_x1, roi_new_y1, image2)
imageShow("image2", image2)

roi_poly_01 = np.array([[(143,192),(126,212),(126,242),(143,261),(179,261),(192,242),(192,212),(179,192)]], dtype=np.int32)
image_polyROI_01 = polyROI(image, roi_poly_01)
imageShow("image_polyROI_01", image_polyROI_01)

pt1 = (95, 367) 
pt2 = (225, 367)
pt3 = (225, 459)
pt4 = (95, 459)
roi_poly_02 = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
image_polyROI_02 = polyROI(image, roi_poly_02)
imageShow("image_polyROI_02", image_polyROI_02)

cv2.destroyAllWindows()