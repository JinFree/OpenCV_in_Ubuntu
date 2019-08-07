#include "OpenCV_Utils.h"
#include "OpenCV_Functions.h"

Mat imageRead(string openPath, int flag)
{
	Mat image = imread(openPath, flag);
	if(image.empty()) 
    {
		cout<<"Image Not Opened"<<endl;
		cout<<"Program Abort"<<endl;
		exit(1);
	}
	else 
    {
		cout<<"Image Opened"<<endl;
		return image;
	}
}
void imageShow(string imageName, Mat &image, int flag)
{
	namedWindow(imageName, flag);
    imshow(imageName, image);
	waitKey();
	return;
}
void imageWrite(string imageName, Mat &image)
{
    imwrite(imageName, image);
    return;
}
Mat imageCopy(Mat &image)
{
    Mat result;
    image.copyTo(result);
    return result;
}
void Video(string openPath, string savePath)
{
    VideoCapture cap(openPath);
    if(cap.isOpened())
    {
        cout << "Video Opened" << endl;
    }
    else
    {
        cout << "Video Not Opened" << endl;
        cout << "Program Abort" << endl;
        exit(-1);
    }
    int fps = cap.get(CAP_PROP_FPS);
    int width = cap.get(CAP_PROP_FRAME_WIDTH);
    int height = cap.get(CAP_PROP_FRAME_HEIGHT);
    int fourcc = cap.get(CAP_PROP_FOURCC);
    VideoWriter out(savePath.c_str(), fourcc, fps, Size(width, height), true);
    namedWindow("Input", WINDOW_GUI_EXPANDED);
    namedWindow("Output", WINDOW_GUI_EXPANDED);
    Mat frame, output;
    while(cap.read(frame))
    {
        imageProcessing(frame, output);
        out.write(output);
        imshow("Input", frame);
        imshow("Output", output);
        char c = (char)waitKey(int(1000.0/fps));
        if (c==27)
            break;
    }
    cap.release();
    out.release();
    destroyAllWindows();
    return;
}
vector<int> imageParameters(string imagename,Mat &image)
{
    vector<int> Result;
    Size size = image.size();
    int width = image.cols;
    int height = image.rows;
    cout << imagename << ".size() is " << size<< endl;
    cout << imagename << ".rows is height: " << height<< endl;
    cout << imagename << ".cols is width: " << width<< endl;
    int channels = image.channels();
    if( channels == 1)
        cout << "This is grayscale image." << endl;
    else
        cout << "This is not grayscale image." << endl;
    cout << imagename << ".type() is " << image.type()<< endl;
    Result.push_back(height);
    Result.push_back(width);
    return Result;
}
int getPixel(Mat &image, int x, int y, int c) 
{
    if( image.type() == CV_8UC1) 
    {
        uchar* pointer = image.ptr<uchar>(y);
        return pointer[x];
    }
    else if( image.type() == CV_8UC3) 
    {
        uchar* pointer = image.ptr<uchar>(y);
        return pointer[x*3+c];
    }
}
void setPixel(Mat &image, int x, int y, int value, int c) 
{
    if( image.type() == CV_8UC1) 
    {
        uchar* pointer = image.ptr<uchar>(y);
        pointer[x] = value;
        return;
    }
    else if( image.type() == CV_8UC3) 
    {
        uchar* pointer = image.ptr<uchar>(y);
        pointer[x*3+c]= value;
        return;;
    }
}
void CutRectROI(Mat &image, Mat &result, Point pt1, Point pt2)
{
    result = image(Rect(pt1, pt2)).clone();
    return;
}
void PasteRectROI(Mat &image, Mat &result, Point pt1)
{   
    int y2 = result.rows + pt1.y;
    int x2 = result.cols + pt1.x;
    Mat dstROI(result, Rect(pt1, Point(x2, y2)));
    image.copyTo(dstROI);
    return;
}
Mat makeBlackImage(Mat &image, bool color)
{
    if(color)
        return Mat::zeros(image.size(), CV_8UC3);
    else
        return Mat::zeros(image.size(), image.type());
}
Mat fillPolyROI(Mat &image, vector<Point> points)
{
    Mat result = makeBlackImage(image, false);
    vector<vector<Point> > fillContAll;
    fillContAll.push_back(points);
    if(image.channels()==1)
        fillPoly(result, fillContAll, Scalar(255));
    else 
        fillPoly(result, fillContAll, Scalar(255, 255, 255));
    return result;
}
void polyROI(Mat &image, Mat &result, vector<Point> points) 
{
    result = fillPolyROI(image, points);
    bitwise_and(result, image, result);
    return;
}
void convertColor(Mat &image, Mat &result, int flag)
{
    cvtColor(image, result, flag);
    return;
}
void splitImage(Mat &image, vector<Mat> &channels) 
{
    split(image, channels);
    return;
}
void mergeImage(vector<Mat> &channels, Mat &image) 
{
    merge(channels, image);
    return;
}
void mergeImage(Mat &ch1, Mat &ch2, Mat &ch3, Mat &image) 
{
    vector<Mat> channels;
	channels.push_back(ch1);
	channels.push_back(ch2);
	channels.push_back(ch3);
	mergeImage(channels, image);
	return;
}
void rangeColor(Mat &image, Mat &result, Scalar &min, Scalar &max) 
{
    result = imageCopy(image);
    inRange(image, min, max, result);
    return;
}
void splitColor(Mat &image, Mat &result, Scalar &min, Scalar &max) 
{
    Mat mask = imageCopy(image);
    rangeColor(mask, mask, min, max);
    bitwise_and(image, image, result, mask);
    return;
}
void drawLine(Mat &image, Mat &result, Point pt1, Point pt2, Scalar color, int thickness) 
{
    result = imageCopy(image);
    line(result, pt1, pt2, color, thickness);
    return;
}
void drawRect(Mat &image, Mat &result, Point pt1, Point pt2, Scalar color, int thickness) 
{
    result = imageCopy(image);
    rectangle(result, pt1, pt2, color, thickness);
    return;
}
void drawRect(Mat &image, Mat &result, Rect rect, Scalar color, int thickness) 
{
    result = imageCopy(image);
    rectangle(result, rect, color, thickness);
    return;
}
void drawCircle(Mat &image, Mat &result, Point center, int radius,  Scalar color, int thickness) 
{
    result = imageCopy(image);
    circle(result, center, radius, color, thickness);
    return;
}
void drawEllipse(Mat &image, Mat &result, Point center, Size axis, double angle, double startAngle, double endAngle, Scalar color, int thickness) 
{
    result = imageCopy(image);
    ellipse(result, center, axis, angle, startAngle, endAngle, color, thickness);
    return;
}
void drawPolygon(Mat &image, Mat &result, vector<Point> points, bool isClosed, Scalar color, int thickness) 
{
    result = imageCopy(image);
    const Point *pts = (const Point *)Mat(points).data;
    int npts = Mat(points).rows;
    polylines(result, &pts, &npts, 1, isClosed, color, thickness);
    return;
}
void drawText(Mat& image, Mat &result, const string& text, Point point, int font, double fontScale, Scalar color, int thickness) 
{
    result = imageCopy(image);
    putText(result, text, point, font, fontScale, color, thickness);
    return;
}
void addImage(Mat &image1, Mat &image2, Mat &result) 
{
    add(image1, image2, result);
}
void addWeightedImage(Mat &image1, Mat &image2, Mat &result, double w1, double w2) 
{
    result = imageCopy(image1);
    if( w2 == -1) 
        addWeighted(image1, w1*0.01, image2, (100.0-w1)*0.01,0, result);
    else 
        addWeighted(image1, w1*0.01, image2, w2*0.01, 0, result);
    return;
}
void imageThreshold(Mat &image, Mat &result, double thresh, double maxval, int type) 
{
    result = imageCopy(image);
    threshold(image, result, thresh, maxval, type);
    return;
}
void imageBlur(Mat &image, Mat &result, int ksize) 
{
    result = imageCopy(image);
    Size kernelSize(ksize*2-1, ksize*2-1);
    blur(image, result, kernelSize);
    return;
}
void imageGaussianBlur(Mat &image, Mat &result, int ksize, double sigmaX, double sigmaY) 
{
    result = imageCopy(image);
    Size kernelSize(ksize*2-1, ksize*2-1);
    GaussianBlur(image, result, kernelSize, sigmaX, sigmaY);
    return;
}
void imageMedianBlur(Mat &image, Mat &result, int ksize) 
{
    result = imageCopy(image);
    medianBlur(image, result, ksize*2-1);
    return;
}
void imageBilateralFilter(Mat &image, Mat &result, int ksize, double sigmaColor, double sigmaSpace) 
{
    result = imageCopy(image);
    bilateralFilter(image, result, ksize*2-1, sigmaColor, sigmaSpace);
    return;
}
void imageFiltering(Mat &image, Mat &result, Mat &kernel, int ddepth) 
{
    result = imageCopy(image);
    filter2D(image, result, ddepth, kernel);
    return;
}
void imageEdgePrewitt(Mat &image, Mat &result) 
{
    float kernel_x[] = {-1, 0, 1,
                        -1, 0, 1,
                        -1, 0, 1};
	Mat kernelx(3, 3, CV_32F,kernel_x);
	float kernel_y[] = {-1, -1, -1,
	                    0, 0, 0,
	                    1, 1, 1};
	Mat kernely(3, 3, CV_32F,kernel_y);
	Mat dx, dy;
	imageFiltering(image, dx, kernelx);
	imageFiltering(image, dy, kernely);
	result = dx+dy;
	return;
}
void imageEdgeSobel(Mat &image, Mat &result) 
{
    Mat dx, dy;
    Sobel(image, dx, -1, 1, 0, 3);
    Sobel(image, dy, -1, 0, 1, 3);
	result = dx+dy;
	return;
}
void imageEdgeScharr(Mat &image, Mat &result) 
{
    Mat dx, dy;
    Scharr(image, dx, -1, 1, 0);
    Scharr(image, dy, -1, 0, 1);
	result = dx+dy;
	return;
}
void imageEdgeLaplacianCV(Mat &image, Mat &result) 
{
    Laplacian(image, result, -1, 1);
	return;
}
void imageEdgeLaplacianFilter2D(Mat &image, Mat &result) 
{
    float kernel_[] = {-1, -1, -1, 
                       -1, 8, -1, 
                       -1, -1, -1};
	Mat kernel(3, 3, CV_32F,kernel_);
	imageFiltering(image, result, kernel);
	return;
}
void imageEdgeLoG(Mat &image, Mat &result) 
{
    float kernel_[] = {0, 0, -1, 0, 0, 
                       0, -1, -2, -1, 0, 
                       -1, -2, 16, -2, -1, 
                       0, -1, -2, -1, 0, 
                       0, 0, -1, 0, 0};
	Mat kernel(5, 5, CV_32F,kernel_);
	imageFiltering(image, result, kernel);
	return;
}
void cannyEdge(Mat &image, Mat &result, double threshold1, double threshold2) 
{
    Canny(image, result, threshold1, threshold2);
    return;
}
void computeHist(Mat &image, Mat &result) 
{
    Mat histogram;
    if( image.channels() == 1) 
    {
        int histSize = 256;
	    float range[] = { 0, 256 };
	    const float* histRange = { range };
	    calcHist(&image, 1, 0, Mat(), histogram, 1, &histSize, &histRange);
	    int hist_w = 256; 
	    int hist_h = 300;
	    int bin_w = cvRound((double)hist_w / (double)histSize);
	    Mat histImage(hist_h, hist_w, CV_8UC1, Scalar(0, 0, 0));
	    normalize(histogram, histogram, 0, histImage.rows, NORM_MINMAX, -1, Mat());
	    for (int i = 1; i < histSize; i++) 
		    line(histImage, Point(bin_w*(i - 1), hist_h - cvRound(histogram.at<float>(i - 1))), Point(bin_w*(i), hist_h - cvRound(histogram.at<float>(i))), 255, 2, 8, 0);
	    result = imageCopy(histImage);
	    return;
	}
    else 
    {
        vector<Mat> channels;
        splitImage(image, channels);
        int i;
        for ( i=0 ; i < 3 ; i++)
            computeHist(channels[i], channels[i]);
        mergeImage(channels, result);
        return;
    }
}
void histogramEqualize(Mat &image, Mat &result) 
{
    if( image.channels() == 1) 
    {
        equalizeHist(image, result);
	    return;
	}
    else 
    {
        vector<Mat> channels;
        splitImage(image, channels);
        int i;
        for ( i=0 ; i < 3 ; i++)
            histogramEqualize(channels[i], channels[i]);
        mergeImage(channels, result);
        return;
    }
}
void imageDilation(Mat &image, Mat &result, Mat &kernel, int iterations) 
{
    dilate(image, result, kernel, Point(), iterations);
    return;
}
void imageErosion(Mat &image, Mat &result, Mat &kernel, int iterations) 
{
    erode(image, result, kernel, Point(), iterations);
    return;
}
void imageMorphologicalGradient(Mat &image, Mat &result) 
{
    float kernel_[] = {1, 1, 1, 
                       1, 1, 1, 
                       1, 1, 1};
	Mat kernel(3, 3, CV_32F,kernel_);
    Mat dilation, erosion;
    imageDilation(image, dilation, kernel);
    imageErosion(image, erosion, kernel);
    result = dilation-erosion;
    return;
}
void imageOpening(Mat &image, Mat &result, int iterations) 
{
    float kernel_[] = {1, 1, 1, 
                       1, 1, 1, 
                       1, 1, 1};
	Mat kernel(3, 3, CV_32F,kernel_);
    imageErosion(image, result, kernel, iterations);
    imageDilation(result, result, kernel, iterations);
    return;
}
void imageClosing(Mat &image, Mat &result, int iterations) 
{
    float kernel_[] = {1, 1, 1, 
                       1, 1, 1, 
                       1, 1, 1};
	Mat kernel(3, 3, CV_32F,kernel_);
    imageDilation(image, result, kernel, iterations);
    imageErosion(result, result, kernel, iterations);
    return;
}
void imageMorphologyKernel(Mat &result, int shape, int size) 
{
    result = getStructuringElement(shape, Size(size, size));
    return;
}
void imageMorphologyEx(Mat &image, Mat &result, int op, Mat &kernel, int iterations) 
{
    morphologyEx(image, result, op, kernel, Point(), iterations);
    return;
}
void imageResize(Mat &image, Mat &result, Size dsize, double fx, double fy, int interpolation) 
{
    resize(image, result, dsize, fx, fy, interpolation);
    return;
}
void imageTranslation(Mat &image, Mat &result, Size size, double dx, double dy, int interpolation) 
{
    Mat M = (Mat_<float>(2,3) << 1, 0, dx, 0, 1, dy);
    warpAffine(image, result, M, size, interpolation);
    return;
}
void imageRotation(Mat &image, Mat &result, Point center, double angle, double scale, Size size, int interpolation) 
{
    Mat M = getRotationMatrix2D(center, angle, scale);
    warpAffine(image, result, M, size, interpolation);
    return;
}
void imageAffineTransformation(Mat &image, Mat &result, vector<Point> src_pts, vector<Point> dst_pts, Size size, int  interpolation) 
{
    Point2f srcTri[3], dstTri[3];
    int i;
    for ( i=0 ; i<3; i++) 
    {
        srcTri[i] = src_pts[i];
        dstTri[i] = dst_pts[i];
    }
    Mat M = getAffineTransform(srcTri, dstTri);
    warpAffine(image, result, M, size, interpolation);
    return;
}
void imagePerspectiveTransformation(Mat &image, Mat &result, vector<Point> src_pts, vector<Point> dst_pts, Size size, int  interpolation) 
{
    Point2f srcTri[4], dstTri[4];
    int i;
    for ( i=0 ; i<4; i++) 
    {
        srcTri[i] = src_pts[i];
        dstTri[i] = dst_pts[i];
    }
    Mat M = getPerspectiveTransform(srcTri, dstTri);
    warpPerspective(image, result, M, size, interpolation);
    return;
}
void imageHoughLines(Mat &image, vector<Vec2f> &lines, double rho, double theta, int threshold) 
{
    lines.clear();
    HoughLines(image, lines, rho, theta, threshold);
    return;
}
void drawHoughLines(Mat &result, vector<Vec2f> &lines, Scalar color, int thickness) 
{
    if(result.channels()==1)
        convertColor(result, result, COLOR_GRAY2BGR);
    std::vector<cv::Vec2f>::const_iterator it= lines.begin();
    while (it!=lines.end()) 
    {
        float rho = (*it)[0];
        float theta = (*it)[1];
        Point pt1(rho/cos(theta), 0); 
        Point pt2((rho-result.rows*sin(theta))/cos(theta), result.rows);
        line(result, pt1, pt2, color, thickness);
	    ++it;
	}
	return;
}
void imageHoughLinesP(Mat &image, vector<Vec4i> &lines, double rho, double theta, int threshold, double minLineLength, double maxLineGap) 
{
    lines.clear();
    HoughLinesP(image,lines,rho,theta,threshold, minLineLength, maxLineGap);
    return;
}
void drawHoughLinesP(Mat &result, vector<Vec4i> &lines, Scalar color, int thickness) 
{
    if(result.channels()==1)
        convertColor(result, result, COLOR_GRAY2BGR);
 	vector<Vec4i>::const_iterator it= lines.begin();
    while (it!=lines.end()) 
    {
        Point pt1((*it)[0],(*it)[1]);
        Point pt2((*it)[2],(*it)[3]);
        line( result, pt1, pt2, color, thickness);
        ++it;
    }
  	return;
}
void splitTwoSideLines(vector<Vec4i> &lines, vector<vector<float>> &lefts, vector<vector<float>> &rights, float slope_threshold)
{
    int i;
    lefts.clear();
    rights.clear();
    vector<float> temp;
    for( i = 0 ; i < lines.size() ; i++ )
    {
        temp.clear();
        Vec4i line = lines[i];
        int x1, y1, x2, y2;
        x1 = line[0];
        y1 = line[1];
        x2 = line[2];
        y2 = line[3];
        if (x1 - x2 == 0)
            continue;
        float slope = (float)(y2-y1)/(float)(x2-x1);
        if (abs(slope) < slope_threshold)
            continue;
        if( slope <= 0)
        {
            temp.push_back(slope);
            temp.push_back(x1);
            temp.push_back(y1);
            temp.push_back(x2);
            temp.push_back(y2);
            lefts.push_back(temp);
        }
        else
        {
            temp.push_back(slope);
            temp.push_back(x1);
            temp.push_back(y1);
            temp.push_back(x2);
            temp.push_back(y2);
            rights.push_back(temp);
        }
    }
    return;
}
void splitOneSideLines(vector<Vec4i> &lines, vector<vector<float>> &arranged_lines, float slope_threshold)
{
    int i;
    arranged_lines.clear();
    vector<float> temp;
    for( i = 0 ; i < lines.size() ; i++ )
    {
        temp.clear();
        Vec4i line = lines[i];
        int x1, y1, x2, y2;
        x1 = line[0];
        y1 = line[1];
        x2 = line[2];
        y2 = line[3];
        if (x1 - x2 == 0)
            continue;
        float slope = (float)(y2-y1)/(float)(x2-x1);
        if (abs(slope) < slope_threshold)
            continue;
        temp.push_back(slope);
        temp.push_back(x1);
        temp.push_back(y1);
        temp.push_back(x2);
        temp.push_back(y2);
        arranged_lines.push_back(temp);
    }
    return;
}
bool comp(vector<float> a, vector<float> b)
{
    return (a[0] > b[0]);
}
void medianPoint(vector<vector<float>> &lines, vector<float> &line)
{
    line.clear();
    size_t size = lines.size();
    if (size == 0)
        return;
    sort(lines.begin(), lines.end(), comp);
    line = lines[(int)(size/2.0)];
    return;
}
int interpolate(int x1, int y1, int x2, int y2, int y)
{
    return int(float(y - y1) * float(x2-x1) / float(y2-y1) + x1);
}
void lineFittingOneSide(Mat &image, Mat &result, vector<Vec4i> &lines, Scalar color, int thickness, float slope_threshold)
{
    result = imageCopy(image);
    int height = image.rows;
    vector<vector<float>> arrangedLines;
    splitOneSideLines(lines, arrangedLines, slope_threshold);
    vector<float> medianLine;
    medianPoint(arrangedLines, medianLine);
    int min_y = int(height * 0.6);
    int max_y = height;
    int min_x = interpolate(medianLine[1], medianLine[2], medianLine[3], medianLine[4], min_y);
    int max_x = interpolate(medianLine[1], medianLine[2], medianLine[3], medianLine[4], max_y);
    line(result, Point(min_x, min_y), Point(max_x, max_y), color, thickness);
    result;
}
void lineFitting(Mat &image, Mat &result, vector<Vec4i> &lines, Scalar color, int thickness, float slope_threshold)
{
    result = imageCopy(image);
    int height = image.rows;
    vector<vector<float>> lefts, rights;
    splitTwoSideLines(lines, lefts, rights, slope_threshold);
    vector<float> left, right;
    medianPoint(lefts, left);
    medianPoint(rights, right);
    int min_y = int(height * 0.6);
    int max_y = height;
    int min_x_left = interpolate(left[1], left[2], left[3], left[4], min_y);
    int max_x_left = interpolate(left[1], left[2], left[3], left[4], max_y);
    int min_x_right = interpolate(right[1], right[2], right[3], right[4], min_y);
    int max_x_right = interpolate(right[1], right[2], right[3], right[4], max_y);
    line(result, Point(min_x_left, min_y), Point(max_x_left, max_y), color, thickness);
    line(result, Point(min_x_right, min_y), Point(max_x_right, max_y), color, thickness);
    return;
}
void imageHoughCircles(Mat &image, vector<Vec3f> &circles, int method, double dp, double minDist, double canny, double threshold, double minRadius, double maxRadius)
{
    cv::HoughCircles(image, circles, method, dp, minDist, canny, threshold, minRadius, maxRadius);
    return;
}
void drawHoughCircles(Mat &image, Mat &result, vector<Vec3f> &circles)
{
    result = imageCopy(image);
    if (circles.size() == 0)
        return;
    for (size_t i = 0 ; i < circles.size(); i++)
    {
        Vec3i c = circles[i];
        Point center = Point(c[0], c[1]);
        int radius = c[2];
        cv::circle(result, center, 2, Scalar(0, 0, 255), -1);
        cv::circle(result, center, radius, Scalar(0, 255, 0), 2);
    } 
    return;
}