#include "OpenCV_Functions.h"
void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    return;
}
string path_to_images(void)
{   
    string road_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg";
    string road_image_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteRight.jpg";
    string road_image_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve.jpg";
    string road_image_04 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve2.jpg";
    string road_image_05 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowLeft.jpg";
    string road_image_06 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/whiteCarLaneSwitch.jpg";

    string traffic_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png";
    string traffic_image_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_02.png";
    string traffic_image_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/red_light_01.png";
    string traffic_image_04 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/red_light_02.png";
    string traffic_image_05 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/yellow_light_01.png";
    string traffic_image_06 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/yellow_light_02.png";
    return traffic_image_01;
}
void processingSingleImage(string imagePath, string outputPath)
{
    Mat image = imageRead(imagePath);
    imageShow("Opened Image", image);
    Mat result;
    imageProcessing(image, result);
    cout << "test" << endl;
    imageShow("Result Image", result);
    imageWrite(outputPath, result);
    return;
}
vector<string> imageList_LaneDetection(void)
{
    string path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/";
    string path_to_data = path_to_project + "Data/";
    string path_to_road_image = path_to_data + "Lane_Detection_Images/";

    string road_image_01 = path_to_road_image + "solidWhiteCurve.jpg";
    string road_image_02 = path_to_road_image + "solidWhiteRight.jpg";
    string road_image_03 = path_to_road_image + "solidYellowCurve.jpg";
    string road_image_04 = path_to_road_image + "solidYellowCurve2.jpg";
    string road_image_05 = path_to_road_image + "solidYellowLeft.jpg";
    string road_image_06 = path_to_road_image + "whiteCarLaneSwitch.jpg";

    vector<string> images;
    images.push_back(road_image_01);
    images.push_back(road_image_02);
    images.push_back(road_image_03);
    images.push_back(road_image_04);
    images.push_back(road_image_05);
    images.push_back(road_image_06);
    return images;
}
vector<string> imageList_TrafficLightDetection(void)
{
    string path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/";
    string path_to_data = path_to_project + "Data/";
    string path_to_road_image = path_to_data + "TrafficLight_Detection/";

    string image_01 = path_to_road_image + "green_light_01.png";
    string image_02 = path_to_road_image + "green_light_02.png";
    string image_03 = path_to_road_image + "red_light_01.png";
    string image_04 = path_to_road_image + "red_light_02.png";
    string image_05 = path_to_road_image + "yellow_light_01.png";
    string image_06 = path_to_road_image + "yellow_light_02.png";

    vector<string> images;
    images.push_back(image_01);
    images.push_back(image_02);
    images.push_back(image_03);
    images.push_back(image_04);
    images.push_back(image_05);
    images.push_back(image_06);
    return images;
}
void processingMultipleImages(vector<string> list_of_images)
{
    int idx=0;
    for (string path : list_of_images)
    {
        Mat image = imageRead(path);
        imageShow("Image index is " + to_string(idx), image);
        Mat result;
        imageProcessing(image, result);
        imageShow("Result of index " + to_string(idx), result);
        imageWrite("Result_" + to_string(idx) + ".jpg", result);
        idx++;
    }
    return;
}
string path_to_videos(void)
{
    string road_video_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidWhiteRight.mp4";
    string road_video_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidYellowLeft.mp4";
    return road_video_01;
}
void processingSingleVideo(string videoPath, string outputPath)
{
    Video(videoPath, outputPath);
    return;
}
vector<string> videoList_LaneDetection(void)
{
    string path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/";
    string path_to_data = path_to_project + "Data/";
    string path_to_road_video = path_to_data + "Lane_Detection_Videos/";
    string road_video_01 = path_to_road_video + "solidWhiteRight.mp4";
    string road_video_02 = path_to_road_video + "solidYellowLeft.mp4";

    vector<string> videos;
    videos.push_back(road_video_01);
    videos.push_back(road_video_02);
    return videos;
}
void processingMultipleVideos(vector<string> list_of_videos)
{
    int idx=0;
    for (string path : list_of_videos)
    {
        Video(path, "output_" + to_string(idx) + ".mp4");
        idx++;
    }
    return;
}