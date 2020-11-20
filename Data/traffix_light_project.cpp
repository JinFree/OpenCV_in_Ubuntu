void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    int height = image.rows;
    int width = image.cols;
    Mat hsv;
    convertColor(result, hsv, COLOR_BGR2HSV);
    vector<Mat> channels;
    splitImage(hsv, channels);
    Mat s_eq;
    histogramEqualize(channels[1], s_eq);
    Mat hsv2;
    mergeImage(channels[0], s_eq, channels[2], hsv2);
    Scalar red_1_lower = Scalar(0, 100, 120);
    Scalar red_1_upper = Scalar(7, 255, 255);
    Scalar red_2_lower = Scalar(170, 100, 120);
    Scalar red_2_upper = Scalar(180, 255, 255);
    Scalar green_lower = Scalar(35, 100, 120);
    Scalar green_upper = Scalar(90, 255, 255);
    Scalar yellow_lower = Scalar(17, 100, 120);
    Scalar yellow_upper = Scalar(33, 255, 255);
    Mat red_1, red_2, red, green, yellow;
    rangeColor(hsv2, red_1, red_1_lower, red_1_upper);
    rangeColor(hsv2, red_2, red_2_lower, red_2_upper);
    rangeColor(hsv2, green, green_lower, green_upper);
    rangeColor(hsv2, yellow, yellow_lower, yellow_upper);
    red = red_1 + red_2;
    vector<Point> red_point_list, green_point_list, yellow_point_list;
    if(width < height)
    {
        int x = 0.5 * width;
        for (int y = 0 ; y < height ; y++ )
        {
            int pixel_red = getPixel(red, x, y);
            int pixel_green = getPixel(green, x, y);
            int pixel_yellow = getPixel(yellow, x, y);
            if(pixel_red == 255)
                if(red_point_list.size() == 0)
                    red_point_list.push_back(Point(x, y));
            if(pixel_green == 255)
                if(green_point_list.size() == 0)
                    green_point_list.push_back(Point(x, y));
            if(pixel_yellow == 255)
                if(yellow_point_list.size() == 0)
                    yellow_point_list.push_back(Point(x, y));
        }
        for (int y = height - 1 ; y >= 0 ; y-- )
        {
            int pixel_red = getPixel(red, x, y);
            int pixel_green = getPixel(green, x, y);
            int pixel_yellow = getPixel(yellow, x, y);
            if(pixel_red == 255)
                if(red_point_list.size() == 1)
                    red_point_list.push_back(Point(x, y));
            if(pixel_green == 255)
                if(green_point_list.size() == 1)
                    green_point_list.push_back(Point(x, y));
            if(pixel_yellow == 255)
                if(yellow_point_list.size() == 1)
                    yellow_point_list.push_back(Point(x, y));
        }
    }
    Mat hls, l;
    convertColor(image, hls, COLOR_BGR2HLS);
    vector<Mat> channels_hls;
    splitImage(hls, channels_hls);
    l = channels_hls[1];
    vector<Point> value_list;
    if(red_point_list.size() == 2)
        if(width < height)
            if((red_point_list[1].y - red_point_list[0].y) < (0.7*width))
                value_list.push_back(Point(0, getPixel(l, red_point_list[0].x, red_point_list[0].y)));
    if(green_point_list.size() == 2)
        if(width < height)
            if((green_point_list[1].y - green_point_list[0].y) < (0.7*width))
                value_list.push_back(Point(1, getPixel(l, green_point_list[0].x, green_point_list[0].y)));
    if(yellow_point_list.size() == 2)
        if(width < height)
            if((yellow_point_list[1].y - yellow_point_list[0].y) < (0.7*width))
                value_list.push_back(Point(2, getPixel(l, yellow_point_list[0].x, yellow_point_list[0].y)));

    int lightness_idx = 0;
    int lightness = 0;
    if(value_list.size() == 0)
    {
        drawText(image, result, "Nothing Detected", Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, Scalar(255, 0, 0), 3);
    return;
    }
    for(int idx = 0 ; idx < value_list.size() ; idx++)
    {
        if(value_list[idx].y > lightness)
        {
            lightness = value_list[idx].y;
            lightness_idx = idx;           
        }
    }
    string traffic_light;
    if(value_list[lightness_idx].x == 0)
        traffic_light = "red light";
    if(value_list[lightness_idx].x == 1)
        traffic_light = "green light";
    if(value_list[lightness_idx].x == 2)
        traffic_light = "yellow light";
    drawText(image, result, traffic_light, Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, Scalar(255, 0, 0), 3);
    return;
}
