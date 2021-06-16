def imageProcessing(image):
    result = imageCopy(image)
    grayscale = convertColor(result, cv2.COLOR_BGR2GRAY)
    
    height, width = image.shape[:2]
    
    lane_left = int(width*0.3)
    lane_right = int(width*0.7)

    src_pt1 = [int(width*0.4), int(height*0.65)]
    src_pt2 = [int(width*0.6), int(height*0.65)]
    src_pt3 = [width, height]
    src_pt4 = [0, height]
    dst_pt1 = [lane_left, 0]
    dst_pt2 = [lane_right, 0]
    dst_pt3 = [lane_right, height]
    dst_pt4 = [lane_left, height]

    src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
    dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])

    grayscale = imagePerspectiveTransformation(grayscale, src_pts, dst_pts)
    edge = cannyEdge(grayscale, 150, 300)
    
    lines = houghLinesP(edge, 1, np.pi/180, 40)
    blackImage = makeBlackImage(result, True)
    
    lane_width_threshold_out = 0
    lane_width_threshold_in = 100
    lane_height_threshold = 20
    
    left_slope_list = []
    right_slope_list = [] 
    
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        if abs(y1-y2) < lane_height_threshold:
            continue
        left_min = lane_left - lane_width_threshold_out
        left_max = lane_left + lane_width_threshold_in
        right_min = lane_right - lane_width_threshold_in
        right_max = lane_right + lane_width_threshold_out
        slope = (float)(y2-y1)/(float)(x2-x1+0.00001)
        
        if left_min < x1 < left_max:
            left_slope_list.append([slope, x1, y1, x2, y2])
        if right_min < x1 < right_max:
            right_slope_list.append([slope, x1, y1, x2, y2])
            
    left_lane = medianPoint(left_slope_list)
    right_lane = medianPoint(right_slope_list)
    
    min_y = 0
    max_y = height
    min_x_left = None
    max_x_left = None
    min_x_right = None
    max_x_right = None
    left_lane_detected = False
    right_lane_detected = False
    
    if left_lane is not None:
        min_x_left = interpolate(left_lane[1], left_lane[2], left_lane[3], left_lane[4], min_y)
        max_x_left = interpolate(left_lane[1], left_lane[2], left_lane[3], left_lane[4], max_y)
        cv2.line(blackImage, (min_x_left, min_y), (max_x_left, max_y), (0, 0, 255), 5)
        left_lane_detected = True
        
    if right_lane is not None:
        min_x_right = interpolate(right_lane[1], right_lane[2], right_lane[3], right_lane[4], min_y)
        max_x_right = interpolate(right_lane[1], right_lane[2], right_lane[3], right_lane[4], max_y)
        cv2.line(blackImage, (min_x_right, min_y), (max_x_right, max_y), (255, 0, 0), 5)
        right_lane_detected = True
        
    if left_lane_detected and right_lane_detected:
        pt1 = (min_x_left, min_y)
        pt2 = (min_x_right, min_y)
        pt3 = (max_x_right, max_y)
        pt4 = (max_x_left, max_y)
        pts_roi = np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32)
        blackImage = cv2.fillPoly(blackImage, pts_roi, (0, 255,0 ))
    
    lane_drawed = imagePerspectiveTransformation(blackImage, src_pts, dst_pts, flags=cv2.WARP_INVERSE_MAP)
    result = cv2.add(image, lane_drawed)
    
    resized = cv2.resize(blackImage, None, fx=0.25, fy=0.25)
    result = PasteRectROI(resized, 0, 0, result)
    return result
