from OpenCV_Functions import *

'''
def drawPolygon(image, pts, isClosed, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    pts = pts.reshape((-1, 1, 2))
    return cv2.polylines(result, [pts], isClosed, color, thickness, lineType)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

pt1 = (143,192)
pt2 = (126,212)
pt3 = (126,242)
pt4 = (143,261)
pt5 = (179,261)
pt6 = (192,242)
pt7 = (192,212)
pt8 = (179,192)
pts = np.vstack((pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8)).astype(np.int32)
pts_roi = np.array([[pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8]], dtype=np.int32)

poly_01 = drawPolygon(image, pts, False, (0, 0, 255), 5)
poly_02 = drawPolygon(image, pts, True, (0, 0, 255), 5)
poly_03 = cv2.fillPoly(image, pts_roi, (0, 0, 255))

imageShow("poly_01", poly_01)
imageShow("poly_02", poly_02)
imageShow("poly_03", poly_03)

cv2.destroyAllWindows()