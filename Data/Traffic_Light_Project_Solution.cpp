bool compari(Point a, Point b)
{
    return (a.x > b.x);
}
void sort_for_circles(vector<Point> &points, Point &point)
{
    size_t size = points.size();
    if (size == 0)
        return;
    if (size == 1)
    {
        point = points[0];
        return;
    }
    sort(points.begin(), points.end(), compari);
    if( points[0].x > points[size-1].x)
    {
        point = points[0];
    }
    else if (points[0].x < points[size-1].x)
    {
        point = points[size-1];
    }
    return;
}
void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    imageParameters("result", result);
    Mat hls, splitted, splitted_bgr, kernel_ellipse;
    Scalar lower(0, 128, 200);
    Scalar upper(180, 255, 255);
    convertColor(result, hls, COLOR_BGR2HLS);
    splitColor(hls, splitted, lower, upper);
    convertColor(splitted, splitted_bgr, COLOR_HLS2BGR);
    convertColor(splitted_bgr, result, COLOR_BGR2GRAY);
    imageThreshold(result, result, 10, 255, THRESH_BINARY);
    imageMorphologyKernel(kernel_ellipse, MORPH_ELLIPSE, 5);
    imageMorphologyEx(result, result, MORPH_CLOSE, kernel_ellipse);
    vector<Vec3f> circles;
    imageHoughCircles(result, circles, HOUGH_GRADIENT, 1, 31, 23, 13, 20, 0);
    result = imageCopy(image);
    vector<Point> value_list;
    for (int i= 0;i < circles.size(); i++)
    {
        int x = circles[i][0];
        int y = circles[i][1];
        int r = circles[i][2];
        int h = getPixel(hls, x, y, 0);
        int l = getPixel(hls, x, y, 1);
        int b = getPixel(result, x, y, 0);
        int g = getPixel(result, x, y, 1);
        int red = getPixel(result, x, y, 2);
        drawCircle(result, result, Point(x, y), r, Scalar(0, 0, 0), 5);
        drawCircle(result, result, Point(x, y), r, Scalar(b, g, red), -1);
        drawCircle(result, result, Point(x, y), 1, Scalar(0, 0, 0), -1);
        value_list.push_back(Point(l, h));
    }
    Point hl_value;
    sort_for_circles(value_list, hl_value);
    int h_value = hl_value.y;
    String color;
    if(h_value < 10 || h_value > 170)
        color = "Red";
    else if(20 < h_value && h_value < 35)
        color = "Yellow";
    else if(60 < h_value and h_value < 90)
        color = "Green";
    String text_string = color + " Light";
    drawText(result, result, text_string, Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, Scalar(255, 0, 0), 3);
    return;
}
