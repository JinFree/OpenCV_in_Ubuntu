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