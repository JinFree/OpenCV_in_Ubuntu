#pragma once
#include "OpenCV_Utils.h"

using namespace std;
using namespace cv;
void imageProcessing(Mat &image, Mat &result);
string path_to_images(void);
void processingSingleImage(string imagePath, string outputPath = "output.jpg");
vector<string> imageList_LaneDetection(void);
vector<string> imageList_TrafficLightDetection(void);
void processingMultipleImages(vector<string> list_of_images);
string path_to_videos(void);
void processingSingleVideo(string videoPath, string outputPath = "output.mp4");
vector<string> videoList_LaneDetection(void);
void processingMultipleVideos(vector<string> list_of_videos);