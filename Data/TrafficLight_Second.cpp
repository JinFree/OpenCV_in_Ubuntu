void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    Mat image_bgr, image_blur, hls, h, l, s, l_thresh, s_thresh, bitwise_and_image;
    int cx, cy, rr, h_value;
    string color, text_to_show;
    Scalar color_circle;
    vector<Vec3f> circles;
    vector<Mat> channels;
    image_bgr = imageCopy(image);
    imageBilateralFilter(image_bgr, image_blur, 2, 2, 2);
    convertColor(image_blur, hls, COLOR_BGR2HLS);
    imageMedianBlur(hls, hls, 5);
    splitImage(hls, channels);
    
    l = channels[1];
    s = channels[2];
    
    imageThreshold(l, l_thresh, 100, 255, THRESH_TOZERO);
    imageThreshold(s, s_thresh, 128, 255, THRESH_TOZERO);
    
    cv::bitwise_and(l_thresh, s_thresh, bitwise_and_image);
    
    imageHoughCircles(bitwise_and_image, circles, HOUGH_GRADIENT, 1, 40, 100, 15, 0, 60);
    
    cx = int(circles[0][0]);
    cy = int(circles[0][1]);
    rr = int(circles[0][2]);
    
    h_value = getPixel(hls, cx, cy, 0);
    color = "None";
    color_circle = Scalar(0, 0, 255);
    if ( h_value < 10  || h_value > 170)
    {
        color = "Red";
    }
    else if(40 < h_value && h_value < 100)
    {
        color = "Green";
        color_circle = Scalar(0, 255, 0);
    }
    else if (20 < h_value && h_value < 35)
    {
        color = "Yellow";
        color_circle = Scalar(0, 255, 255);
    }
    text_to_show = color + " Light";
    drawCircle(result, result, Point(cx, cy), rr, color_circle, -1);
    drawText(result, result, text_to_show, Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, (0, 0, 0), 3);
    return;
}
