#include "OpenCV_Functions.h"

using namespace std;

int main(void) 
{
    // Traffic Light Detection Project
    //processingSingleImage("../../Data/TrafficLight_Detection/green_light_01.png");
    //processingMultipleImages(imageList_TrafficLightDetection());

    // Lane Detection Project
    //processingSingleImage("../../Data/Lane_Detection_Images/test.png");
    processingMultipleImages(imageList_LaneDetection());
    //processingSingleVideo(path_to_videos());
    //processingMultipleVideos(videoList_LaneDetection());
    return 0;
}
