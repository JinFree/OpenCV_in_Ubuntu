def imageProcessing(image):
    result = imageCopy(image)
    gray = convertColor(result, cv2.COLOR_BGR2GRAY)
    result = imageThreshold(gray, 128, 255, cv2.THRESH_BINARY)
    
    height, width = image.shape[:2]
    mylane_left = int(width*0.3)
    mylane_right = int(width*0.7)
    src_pt1 = [int(width*0.4), int(height*0.65)]
    src_pt2 = [int(width*0.6), int(height*0.65)]
    src_pt3 = [width, height]
    src_pt4 = [0, height]
    dst_pt1 = [mylane_left, 0]
    dst_pt2 = [mylane_right, 0]
    dst_pt3 = [mylane_right, height]
    dst_pt4 = [mylane_left, height]
    
    src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
    dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])
    result = imagePerspectiveTransformation(result, src_pts, dst_pts)
    image_temp = imagePerspectiveTransformation(image, src_pts, dst_pts)
    result = cannyEdge(result, 200, 400)
    
    lines = houghLinesP(result, 1, np.pi/180, 50, 30, 50)
    result = makeBlackImage(result, True)
    left_list = []
    right_list = []
    lane_width_threshold_out = 0
    lane_width_threshold_in = 100
    lane_height_threshold = 50
    for i in range(len(lines)):
        x1, y1, x2, y2 =lines[i][0] 
        if abs(y1 - y2) < lane_height_threshold:
            continue
        left_min = mylane_left - lane_width_threshold_out
        left_max = mylane_left + lane_width_threshold_in
        right_min = mylane_right - lane_width_threshold_in
        right_max = mylane_right + lane_width_threshold_out
        if left_min < x1 < left_max:
            left_list.append([x1, y1, x2, y2])
        if right_min < x1 < right_max:
            right_list.append([x1, y1, x2, y2])
            
    left_slope_list = []
    right_slope_list = []
    for i in range(len(left_list)):
        x1, y1, x2, y2 =left_list[i]
        slope = (float)(y2-y1)/((float)(x2-x1)+0.0001)
        left_slope_list.append([slope, x1, y1, x2, y2])
    for i in range(len(right_list)):
        x1, y1, x2, y2 =right_list[i]
        slope = (float)(y2-y1)/((float)(x2-x1)+0.0001)
        right_slope_list.append([slope, x1, y1, x2, y2])
    left = medianPoint(left_slope_list)
    right = medianPoint(right_slope_list)
        
    min_y = 0
    max_y = height
    if left is not None:
        min_x_left = interpolate(left[1], left[2], left[3], left[4], min_y)
        max_x_left = interpolate(left[1], left[2], left[3], left[4], max_y)
        cv2.line(image_temp, (min_x_left, min_y), (max_x_left, max_y), (255, 0, 0), 5)
    if right is not None:
        min_x_right = interpolate(right[1], right[2], right[3], right[4], min_y)
        max_x_right = interpolate(right[1], right[2], right[3], right[4], max_y)
        cv2.line(image_temp, (min_x_right, min_y), (max_x_right, max_y), (0, 0, 255), 5)    
        

    
    resized = cv2.resize(image_temp, (int(width*0.25), int(height*0.25)))
    
    result = PasteRectROI(resized, 0, 0, image)
    return result
