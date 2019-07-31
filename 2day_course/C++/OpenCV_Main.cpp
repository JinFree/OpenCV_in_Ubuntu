#include "OpenCV_Functions.h"

using namespace std;

int main(void) 
{
    //processingMultipleImages();
    //processingMultipleVideos();

    string road_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg";
    string road_image_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteRight.jpg";
    string road_image_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve.jpg";
    string road_image_04 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve2.jpg";
    string road_image_05 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowLeft.jpg";
    string road_image_06 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/whiteCarLaneSwitch.jpg";
    string road_image_07 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/test.png";

    processingSingleImage(road_image_01); // 1 ~ 7


    // string road_video_01 =  "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidWhiteRight.mp4";
    // string road_video_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidYellowLeft.mp4";
    // string road_video_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/challenge.mp4";

    // processingSingleVideo(road_video_01); // 1 ~ 3
    return 0;
}