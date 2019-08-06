from OpenCV_Functions import *

'''
def drawPolygon(image, pts, isClosed, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    pts = pts.reshape((-1, 1, 2))
    return cv2.polylines(result, [pts], isClosed, color, thickness, lineType)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow('image', image)

height = image.shape[0]
width = image.shape[1]

pt1 = (0, height)
pt2 = (int(width *0.5), int(height *0.5))
pt3 = (width, height)

pts = np.vstack((pt1, pt2, pt3)).astype(np.int32)
pts_roi = np.array([[pt1, pt2, pt3]], dtype=np.int32)

poly_01 = drawPolygon(image, pts, False, (0, 0, 255), 5)
poly_02 = drawPolygon(image, pts, True, (0, 0, 255), 5)
poly_03 = cv2.fillPoly(image, pts_roi, (0, 0, 255))

imageShow("poly_01", poly_01)
imageShow("poly_02", poly_02)
imageShow("poly_03", poly_03)

cv2.destroyAllWindows()