void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    int height = image.rows;
    int width = image.cols;
    Mat gray, threshold;
    convertColor(result, gray, COLOR_BGR2GRAY);
    imageThreshold(gray, threshold, 128, 255, THRESH_BINARY);
    int mylane_left = width * 0.3;
    int mylane_right = width * 0.7;
    vector<Point> src_pts, dst_pts;
    src_pts.push_back(Point(int(width*0.4), int(height*0.65)));
    src_pts.push_back(Point(int(width*0.6), int(height*0.65)));
    src_pts.push_back(Point(width, height));
    src_pts.push_back(Point(0, height));
    dst_pts.push_back(Point(mylane_left, 0));
    dst_pts.push_back(Point(mylane_right, 0));
    dst_pts.push_back(Point(mylane_right, height));
    dst_pts.push_back(Point(mylane_left, height));
    Mat threshold_transformed, color_transformed;
    imagePerspectiveTransformation(threshold, threshold_transformed, src_pts, dst_pts, Size(width, height));
    imagePerspectiveTransformation(image, color_transformed, src_pts, dst_pts, Size(width, height));
    Mat edge;
    cannyEdge(threshold_transformed, edge, 200, 400);
    vector<Vec4i> lines;
    imageHoughLinesP(edge, lines, 1.0, PI/180.0, 50, 30, 50);
    
    vector<Vec4i> left_list, right_list;
    int lane_width_threshold_out = 0;
    int lane_width_threshold_in = 100;
    int lane_height_threshold = 50;
    for (int i = 0 ; i < lines.size() ; i++ )
    {
        int x1, y1, x2, y2;
        x1 = lines[i][0];
        y1 = lines[i][1];
        x2 = lines[i][2];
        y2 = lines[i][3];
        if (abs(y1 - y2) > lane_height_threshold)
        {
            int left_min = mylane_left - lane_width_threshold_out;
            int left_max = mylane_left + lane_width_threshold_in;
            int right_min = mylane_right - lane_width_threshold_in;
            int right_max = mylane_right + lane_width_threshold_out;
            if ((left_min < x1) && (x1 < left_max))
                left_list.push_back(Vec4i(x1, y1, x2, y2));
            if ((right_min < x1) && (x1 < right_max))
                right_list.push_back(Vec4i(x1, y1, x2, y2));
        }
    }
    vector<vector<float>> left_slope_list, right_slope_list;
    for(int i = 0 ; i < left_list.size() ; i++)
    {
        vector<float> temp;
        int x1, y1, x2, y2;
        x1 = left_list[i][0];
        y1 = left_list[i][1];
        x2 = left_list[i][2];
        y2 = left_list[i][3];
        float slope = (float)(y2-y1) / ((float)(x2-x1)+0.0001);
        temp.push_back(slope);
        temp.push_back(x1);
        temp.push_back(y1);
        temp.push_back(x2);
        temp.push_back(y2);
        left_slope_list.push_back(temp);
    }
    for(int i = 0 ; i < right_list.size() ; i++)
    {
        vector<float> temp;
        int x1, y1, x2, y2;
        x1 = right_list[i][0];
        y1 = right_list[i][1];
        x2 = right_list[i][2];
        y2 = right_list[i][3];
        float slope = (float)(y2-y1) / ((float)(x2-x1)+0.0001);
        temp.push_back(slope);
        temp.push_back(x1);
        temp.push_back(y1);
        temp.push_back(x2);
        temp.push_back(y2);
        right_slope_list.push_back(temp);
    }
    vector<float> left, right;
    medianPoint(left_slope_list, left);
    medianPoint(right_slope_list, right);
    
    int min_y = 0;
    int max_y = height;
    if( left.size() != 0)
    {
        int min_x_left = interpolate(int(left[1]), int(left[2]), int(left[3]), int(left[4]), min_y);
        int max_x_left = interpolate(int(left[1]), int(left[2]), int(left[3]), int(left[4]), min_y);
        drawLine(color_transformed, color_transformed, Point(min_x_left, min_y), Point(max_x_left, max_y), Scalar(255, 0, 0), 5);
    }
    if( right.size() != 0)
    {
        int min_x_right = interpolate(int(right[1]), int(right[2]), int(right[3]), int(right[4]), min_y);
        int max_x_right = interpolate(int(right[1]), int(right[2]), int(right[3]), int(right[4]), min_y);
        drawLine(color_transformed, color_transformed, Point(min_x_right, min_y), Point(max_x_right, max_y), Scalar(0, 0, 255), 5);
    }
    Mat resized;   
    resize(color_transformed, resized, Size(int(width*0.25), int(height*0.25))); 
        
    result = imageCopy(image);
    PasteRectROI(resized, result, Point(0, 0));
    return;
}
