void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    Mat result_gray, result_edge, result_roi, image_lane;
    vector<Vec4i> lines;
    convertColor(result,result_gray, COLOR_BGR2GRAY);
    cannyEdge(result_gray,result_edge, 100, 200);
    int height = result.rows;
    int width = result.cols;
    Point pt1, pt2, pt3, pt4;
    vector<Point> roi_corners;
    pt1 = Point(width*0.45, height*0.65);
    pt2 = Point(width*0.55, height*0.65);
    pt3 = Point(width, height*1.0);
    pt4 = Point(0, height*1.0);
    roi_corners.push_back(pt1);
    roi_corners.push_back(pt2);
    roi_corners.push_back(pt3);
    roi_corners.push_back(pt4);
    polyROI(result_edge,result_roi, roi_corners);
    imageHoughLinesP(result_roi, lines, 1.0, PI/180., 30, 20,100);
    lineFitting(image, result, lines);
    return;
}
