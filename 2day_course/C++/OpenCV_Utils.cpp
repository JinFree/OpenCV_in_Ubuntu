#include "OpenCV_Utils.h"
#include "OpenCV_Functions.h"

Mat imageRead(string openPath, int flag)
{
	Mat image = imread(openPath, flag);
	if(image.empty()) {
		cout<<"Image Not Opened"<<endl;
		cout<<"Program Abort"<<endl;
		exit(1);
	}
	else {
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
int getPixel(Mat &image, int x, int y, int c) {
    if( image.type() == CV_8UC1) {
        uchar* pointer = image.ptr<uchar>(y);
        return pointer[x];
    }
    else if( image.type() == CV_8UC3) {
        uchar* pointer = image.ptr<uchar>(y);
        return pointer[x*3+c];
    }
}
void setPixel(Mat &image, int x, int y, int value, int c) {
    if( image.type() == CV_8UC1) {
        uchar* pointer = image.ptr<uchar>(y);
        pointer[x] = value;
        return;
    }
    else if( image.type() == CV_8UC3) {
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
void PasteRectROI(Mat &image, Mat &result, Point pt1, Point pt2)
{   
    Mat dstROI(result, Rect(pt1, pt2));
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
}
void polyROI(Mat &image, Mat &result, vector<Point> points) 
{
    result = fillPolyROI(image, points);
    bitwise_and(result, image, result);
    return;
}
void convertColor(Mat &image, Mat &result, int flag=COLOR_BGR2GRAY)
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