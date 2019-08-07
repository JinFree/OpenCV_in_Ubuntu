#include "OpenCV_Functions.h"

using namespace std;

int main(void) 
{
    // Traffic Light Detection Project
    //processingSingleImage("/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png");
    //processingMultipleImages(imageList_TrafficLightDetection());

    // Lane Detection Project
    //processingSingleImage("/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg");
    processingMultipleImages(imageList_LaneDetection());
    //processingSingleVideo(path_to_videos());
    //processingMultipleVideos(videoList_LaneDetection());
    return 0;
}