from OpenCV_Functions import *

'''
def imageResize(image, dsize=None, fx=0.0, fy=0.0, interpolation=cv2.INTER_LINEAR):
if dsize is None and fx == 0.0 and fy == 0.0:
    fx = 1.0
    fy = 1.0
return cv2.resize(image, dsize=dsize, fx=fx, fy=fy, interpolation=interpolation)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow("image", image)

roi_x1 = 192 
roi_y1 = 303
roi_x2 = 278
roi_y2 = 352
roi_rect = CutRectROI(image, roi_x1, roi_y1, roi_x2, roi_y2)
imageShow("roi_rect", roi_rect)

height, width = roi_rect.shape[:2]
roi_resize_01 = imageResize(roi_rect, (int(width*1.5), int(height*1.5)))
roi_resize_02 = imageResize(roi_rect, fx = 1.5, fy = 1.5)

image2 = imageCopy(image)

roi_new_x1 = 16
roi_new_y1 = 330
image2 = PasteRectROI(roi_resize_01, roi_new_x1, roi_new_y1, image2)
imageShow("image2", image2)

roi_new_x1 = 219
roi_new_y1 = 338
image2 = PasteRectROI(roi_resize_02, roi_new_x1, roi_new_y1, image2)
imageShow("image2", image2)

cv2.destroyAllWindows()

