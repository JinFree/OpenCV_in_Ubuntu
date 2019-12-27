def imageProcessing(image):
    result = imageCopy(image)
    HLS = convertColor(result, cv2.COLOR_BGR2HLS)
    Y_lower = np.array([15, 52, 75])
    Y_upper = np.array([30, 190, 255])
    Y_BIN = rangeColor(HLS, Y_lower, Y_upper)
    W_lower = np.array([0, 200, 0])
    W_upper = np.array([180, 255, 255])
    W_BIN = rangeColor(HLS, W_lower, W_upper)
    result = addImage(Y_BIN, W_BIN)
    MORPH_ELLIPSE = imageMorphologyKernel(cv2.MORPH_ELLIPSE, 7)
    result = imageMorphologyEx(result, cv2.MORPH_CLOSE , MORPH_ELLIPSE)    
    MORPH_CROSS = imageMorphologyKernel(cv2.MORPH_CROSS, 3)
    result = imageMorphologyEx(result, cv2.MORPH_OPEN , MORPH_CROSS)
    result_line = imageMorphologyEx(result, cv2.MORPH_GRADIENT , MORPH_CROSS)
    height, width = image.shape[:2]
    src_pt1 = [int(width*0.4), int(height*0.65)]
    src_pt2 = [int(width*0.6), int(height*0.65)]
    src_pt3 = [int(width*0.9), int(height*0.9)]
    src_pt4 = [int(width*0.1), int(height*0.9)]
    roi_poly_02 = np.array([[tuple(src_pt1), tuple(src_pt2), tuple(src_pt3), tuple(src_pt4)]], dtype=np.int32)
    line_roi = polyROI(result_line, roi_poly_02)
    lines = houghLinesP(line_roi, 1, np.pi/180, 10, 5, 10)
    result = lineFitting(image, lines, (0, 0, 255), 5, 5. * np.pi / 180.)
    return result
