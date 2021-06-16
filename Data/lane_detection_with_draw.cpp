void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    Mat grayscale, grayscale_transformed, edge, blackImage, lane_drawed, resized;
    int width = image.cols;
    int height = image.rows;
    int lane_left, lane_right, min_y, max_y, min_x_left, max_x_left, min_x_right, max_x_right, lane_width_threshold_out, lane_width_threshold_in, lane_height_threshold;
    
    bool left_lane_detected, right_lane_detected;
    vector<Point> src_pts, dst_pts, rois;
    vector<vector<Point>> pts_roi;
    vector<Vec4i> lines;
    vector<float> left_lane, right_lane;
    vector<vector<float>> left_slope_list, right_slope_list;
    
    convertColor(result, grayscale, COLOR_BGR2GRAY);
    lane_left = int(width*0.3);
    lane_right = int(width*0.7);
    
    src_pts.push_back(Point(int(width*0.4), int(height*0.65)));
    src_pts.push_back(Point(int(width*0.6), int(height*0.65)));
    src_pts.push_back(Point(width, height));
    src_pts.push_back(Point(0, height));
    
    dst_pts.push_back(Point(lane_left, 0));
    dst_pts.push_back(Point(lane_right, 0));
    dst_pts.push_back(Point(lane_right, height));
    dst_pts.push_back(Point(lane_left, height));
    
    imagePerspectiveTransformation(grayscale, grayscale_transformed, src_pts, dst_pts, Size(width, height));
    cannyEdge(grayscale_transformed, edge, 150, 300);
    imageHoughLinesP(edge, lines, 1, PI/180.0, 40);
    blackImage = makeBlackImage(result, true);
    
    lane_width_threshold_out = 0;
    lane_width_threshold_in = 100;
    lane_height_threshold = 20;
    
    for (int i = 0 ; i < lines.size() ; i++) 
    {
        int x1, y1, x2, y2;
        int left_min, left_max, right_min, right_max;
        float slope;
        x1 = lines[i][0]; 
        y1 = lines[i][1]; 
        x2 = lines[i][2]; 
        y2 = lines[i][3]; 
        if (abs(y1 - y2) >= lane_height_threshold)
        {
            left_min = lane_left - lane_width_threshold_out;
            left_max = lane_left + lane_width_threshold_in;
            right_min = lane_right - lane_width_threshold_in;
            right_max = lane_right + lane_width_threshold_out;
            slope = (float)(y2-y1)/(float)(x2-x1+0.00001);
            if (left_min < x1 && x1 < left_max)
            {
                vector<float> temp;
                temp.push_back(slope);
                temp.push_back(x1);
                temp.push_back(y1);
                temp.push_back(x2);
                temp.push_back(y2);
                left_slope_list.push_back(temp);
            }
            if (right_min < x1 && x1 < right_max)
            {
                vector<float> temp;
                temp.push_back(slope);
                temp.push_back(x1);
                temp.push_back(y1);
                temp.push_back(x2);
                temp.push_back(y2);
                right_slope_list.push_back(temp);
            }
        }
    }
    medianPoint(left_slope_list, left_lane);
    medianPoint(right_slope_list, right_lane);
    min_y = 0;
    max_y = height;
    min_x_left = 0;
    max_x_left = 0;
    min_x_right = 0;
    max_x_right = 0;
    left_lane_detected = false;
    right_lane_detected = false;
    
    if (left_lane.size() != 0)
    {
        min_x_left = interpolate(left_lane[1], left_lane[2], left_lane[3], left_lane[4], min_y);
        max_x_left = interpolate(left_lane[1], left_lane[2], left_lane[3], left_lane[4], max_y);
        drawLine(blackImage, blackImage, Point(min_x_left, min_y), Point(max_x_left, max_y), Scalar(0, 0, 255), 5);
        left_lane_detected = true;
    }
    
    if (right_lane.size() != 0) 
    {
        min_x_right = interpolate(right_lane[1], right_lane[2], right_lane[3], right_lane[4], min_y);
        max_x_right = interpolate(right_lane[1], right_lane[2], right_lane[3], right_lane[4], max_y);
        drawLine(blackImage, blackImage, Point(min_x_right, min_y), Point(max_x_right, max_y), Scalar(255, 0, 0), 5);
        right_lane_detected = true;
    }
    
        
    if (left_lane_detected && right_lane_detected)
    {
        rois.push_back(Point(min_x_left, min_y));
        rois.push_back(Point(min_x_right, min_y));
        rois.push_back(Point(max_x_right, max_y));
        rois.push_back(Point(max_x_left, max_y));
        pts_roi.push_back(rois);
        fillPoly(blackImage, pts_roi, Scalar(0, 255,0 ));
    }
    imagePerspectiveTransformation(blackImage, lane_drawed, dst_pts, src_pts, Size(width, height));
    add(image, lane_drawed, result);
    overlayToImage(result, blackImage, result, 0.25, 0.25);
    return;
}
