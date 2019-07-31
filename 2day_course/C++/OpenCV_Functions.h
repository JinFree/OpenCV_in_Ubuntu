#pragma once
#include "OpenCV_Utils.h"

using namespace std;
using namespace cv;
void imageProcessing(Mat &image, Mat &result);
void processingSingleImage(string imagePath, string outputPath = "output.jpg");
vector<string> imageList(void);
void processingMultipleImages(void);
void processingSingleVideo(string videoPath, string outputPath = "output.mp4");
vector<string> videoList(void);
void processingMultipleVideos(void);