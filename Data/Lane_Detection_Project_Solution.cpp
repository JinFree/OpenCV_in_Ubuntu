void imageProcessing(Mat &image, Mat &result)
{
    //result = imageCopy(image)
    result = imageCopy(image);
    //HLS = convertColor(result, cv2.COLOR_BGR2HLS)
    Mat HLS;
    convertColor(result, HLS, COLOR_BGR2HLS);
    //Y_lower = np.array([15, 52, 75])
    Scalar Y_lower = Scalar(15, 52, 75);
    //Y_upper = np.array([30, 190, 255])
    Scalar Y_upper = Scalar(30, 190, 255);
    //Y_BIN = rangeColor(HLS, Y_lower, Y_upper)
    Mat Y_BIN;
    inRange(HLS, Y_lower, Y_upper, Y_BIN);
    //W_lower = np.array([0, 200, 0])
    Scalar W_lower = Scalar(0, 200, 0);
    //W_upper = np.array([180, 255, 255])
    Scalar W_upper = Scalar(180, 255, 255);
    //W_BIN = rangeColor(HLS, W_lower, W_upper)
    Mat W_BIN;
    inRange(HLS, W_lower, W_upper, W_BIN);
    //result = addImage(Y_BIN, W_BIN)
    addImage(Y_BIN, W_BIN, result);
    //MORPH_ELLIPSE = imageMorphologyKernel(cv2.MORPH_ELLIPSE, 7)
    Mat KERNEL_ELLIPSE;
    imageMorphologyKernel(KERNEL_ELLIPSE, MORPH_ELLIPSE, 7); 
    //result = imageMorphologyEx(result, cv2.MORPH_CLOSE , MORPH_ELLIPSE)
    imageMorphologyEx(result, result, MORPH_CLOSE, KERNEL_ELLIPSE); 
    //MORPH_CROSS = imageMorphologyKernel(cv2.MORPH_CROSS, 3)
    Mat KERNEL_CROSS;
    imageMorphologyKernel(KERNEL_CROSS, MORPH_CROSS, 3); 
    //result = imageMorphologyEx(result, cv2.MORPH_OPEN , MORPH_CROSS)
    imageMorphologyEx(result, result, MORPH_OPEN, KERNEL_CROSS); 
    //result_line = imageMorphologyEx(result, cv2.MORPH_GRADIENT , MORPH_CROSS)
    Mat result_line;
    imageMorphologyEx(result, result_line, MORPH_GRADIENT, KERNEL_CROSS); 
    //height, width = image.shape[:2]
    int width = image.cols;
    int height = image.rows;
    //src_pt1 = [int(width*0.4), int(height*0.65)]
    //src_pt2 = [int(width*0.6), int(height*0.65)]
    //src_pt3 = [int(width*0.9), int(height*0.9)]
    //src_pt4 = [int(width*0.1), int(height*0.9)]
    //roi_poly_02 = np.array([[tuple(src_pt1), tuple(src_pt2), tuple(src_pt3), tuple(src_pt4)]], dtype=np.int32)
    vector<Point> points;
    points.push_back(Point(int(width*0.4), int(height*0.65)));
    points.push_back(Point(int(width*0.6), int(height*0.65)));
    points.push_back(Point(int(width*0.9), int(height*0.9)));
    points.push_back(Point(int(width*0.1), int(height*0.9)));
    //line_roi = polyROI(result_line, roi_poly_02)
    Mat line_roi;
    polyROI(result_line, line_roi, points); 
    //lines = houghLinesP(line_roi, 1, np.pi/180, 10, 5, 10)
    vector<Vec4i> lines;
    imageHoughLinesP(line_roi, lines, 1, 3.141592/180., 10, 5, 10); 
    //result = lineFitting(image, lines, (0, 0, 255), 5, 5. * np.pi / 180.)
    lineFitting(image, result, lines, Scalar(0, 0, 255), 5, 3.141592 * 5. / 180.);
    return;
}
