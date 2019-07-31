#pragma once
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#define PI 3.1415926
using namespace std;
using namespace cv;

Mat imageRead(string openPath, int flag = IMREAD_UNCHANGED);
void imageShow(string imageName, Mat &image, int flag = WINDOW_GUI_EXPANDED);
void imageWrite(string imageName, Mat &image);
Mat imageCopy(Mat &image);
void Video(string openPath, string savePath="output.avi");
vector<int> imageParameters(string imagename,Mat &image);
int getPixel(Mat &image, int x, int y, int c = 0);
void setPixel(Mat &image, int x, int y, int value, int c = 0);
void CutRectROI(Mat &image, Mat &result, Point pt1, Point pt2);
void PasteRectROI(Mat &image, Mat &result, Point pt1, Point pt2);
Mat makeBlackImage(Mat &image, bool color=false);
Mat fillPolyROI(Mat &image, vector<Point> points);
void polyROI(Mat &image, Mat &result, vector<Point> points);
void convertColor(Mat &image, Mat &result, int flag=COLOR_BGR2GRAY);
void splitImage(Mat &image, vector<Mat> &channels);
void mergeImage(vector<Mat> &channels, Mat &image);
void mergeImage(Mat &ch1, Mat &ch2, Mat &ch3, Mat &image);