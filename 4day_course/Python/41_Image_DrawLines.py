from OpenCV_Functions import *

'''
def splitTwoSideLines(lines, slope_threshold = (5. * np.pi / 180.)):
    lefts = []
    rights = []
    for line in lines:
        x1 = line[0,0]
        y1 = line[0,1]
        x2 = line[0,2]
        y2 = line[0,3]
        if (x2-x1) == 0:
            continue
        slope = (float)(y2-y1)/(float)(x2-x1)
        if abs(slope) < slope_threshold:
            continue
        if slope <= 0:
            lefts.append([slope, x1, y1, x2, y2])
        else:
            rights.append([slope, x1, y1, x2, y2])
    return lefts, rights
def medianPoint(x):
    if len(x) == 0:
        return None
    else:
        xx = sorted(x)
        return xx[(int)(len(xx)/2)]
def interpolate(x1, y1, x2, y2, y):
    return int(float(y - y1) * float(x2-x1) / float(y2-y1) + x1)
def lineFitting(image, lines, color = (0,0,255), thickness = 3, slope_threshold = (5. * np.pi / 180.)):
    result = imageCopy(image)
    height = image.shape[0]
    lefts, rights = splitTwoSideLines(lines, slope_threshold)
    left = medianPoint(lefts)
    right = medianPoint(rights)
    min_y = int(height*0.6)
    max_y = height
    min_x_left = interpolate(left[1], left[2], left[3], left[4], min_y)
    max_x_left = interpolate(left[1], left[2], left[3], left[4], max_y)
    min_x_right = interpolate(right[1], right[2], right[3], right[4], min_y)
    max_x_right = interpolate(right[1], right[2], right[3], right[4], max_y)
    cv2.line(result, (min_x_left, min_y), (max_x_left, max_y), color, thickness)
    cv2.line(result, (min_x_right, min_y), (max_x_right, max_y), color, thickness)
    return result
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow("image", image)

image_gray = convertColor(image, cv2.COLOR_BGR2GRAY)
image_edge = cannyEdge(image_gray, 100, 200)
height, width = image.shape[:2]
pt1 = (width*0.45, height*0.65)
pt2 = (width*0.55, height*0.65)
pt3 = (width, height*1.0)
pt4 = (0, height*1.0)
roi_corners = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
image_roi = polyROI(image_edge, roi_corners)
lines = houghLinesP(image_roi, 1, np.pi/180, 40)
image_lane = lineFitting(image, lines, (0, 0, 255), 5, 5. * np.pi / 180.)
imageShow("image_lane", image_lane)

cv2.destroyAllWindows()
