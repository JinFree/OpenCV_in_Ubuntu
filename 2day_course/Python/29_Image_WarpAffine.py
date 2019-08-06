from OpenCV_Functions import *

'''
def imageAffineTransformation(image, src_pts, dst_pts, size=None, flags=cv2.INTER_LINEAR):
    if size is None:
        rows, cols = image.shape[:2]
        size = (cols, rows)
    M = cv2.getAffineTransform(src_pts, dst_pts)
    return cv2.warpAffine(image, M, dsize=size, flags=flags)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 

src_pt1 = [195, 304]
src_pt2 = [273, 304]
src_pt3 = [280, 351]
dst_pt1 = [404, 194]
dst_pt2 = [698, 198]
dst_pt3 = [698, 386]

src_pts = np.float32([src_pt1, src_pt2, src_pt3])
dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3])

image_point = drawCircle(image, tuple(src_pt1), 10, (255, 0, 0), -1)
image_point = drawCircle(image_point, tuple(src_pt2), 10, (0, 255, 0), -1)
image_point = drawCircle(image_point, tuple(src_pt3), 10, (0, 0, 255), -1)

roadAffine_01 = imageAffineTransformation(image_point, src_pts, dst_pts)
roadAffine_02 = imageAffineTransformation(roadAffine_01, src_pts, dst_pts, flags=cv2.WARP_INVERSE_MAP)
roadAffine_03 = imageAffineTransformation(roadAffine_01, dst_pts, src_pts)

imageShow("image_point", image_point)
imageShow("roadAffine_01", roadAffine_01)
imageShow("roadAffine_02", roadAffine_02)
imageShow("roadAffine_03", roadAffine_03)

cv2.destroyAllWindows()