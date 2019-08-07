from OpenCV_Functions import *

'''
def imagePerspectiveTransformation(image, src_pts, dst_pts, size=None, flags=cv2.INTER_LANCZOS4):
    if size is None:
        rows, cols = image.shape[:2]
        size = (cols, rows)
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    return cv2.warpPerspective(image, M, dsize=size, flags=flags)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
height, width = image.shape[:2]

src_pt1 = [int(width*0.35), int(height*0.65)]
src_pt2 = [int(width*0.65), int(height*0.65)]
src_pt3 = [width, height]
src_pt4 = [0, height]
dst_pt1 = [int(width*0.1), 0]
dst_pt2 = [int(width*0.9), 0]
dst_pt3 = [int(width*0.9), height]
dst_pt4 = [int(width*0.1), height]

src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])

roadPoint = drawCircle(image, tuple(src_pt1), 10, (255, 0, 0), -1)
roadPoint = drawCircle(roadPoint, tuple(src_pt2), 10, (0, 255, 0), -1)
roadPoint = drawCircle(roadPoint, tuple(src_pt3), 10, (0, 0, 255), -1)
roadPoint = drawCircle(roadPoint, tuple(src_pt4), 10, (255, 255, 0), -1)

roadAffine_01 = imagePerspectiveTransformation(roadPoint, src_pts, dst_pts)
roadAffine_02 = imagePerspectiveTransformation(roadAffine_01, src_pts, dst_pts, flags=cv2.WARP_INVERSE_MAP)
roadAffine_03 = imagePerspectiveTransformation(roadAffine_01, dst_pts, src_pts)

imageShow("image", image)
imageShow("roadPoint", roadPoint)
imageShow("roadAffine_01", roadAffine_01)
imageShow("roadAffine_02", roadAffine_02)
imageShow("roadAffine_03", roadAffine_03)

cv2.destroyAllWindows()