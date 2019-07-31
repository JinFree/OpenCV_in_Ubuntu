#include "OpenCV_Functions.h"
void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    return;
}
void processingSingleImage(string imagePath, string outputPath)
{
    Mat image = imageRead(imagePath);
    imageShow("Opened Image", image);
    Mat result;
    imageProcessing(image, result);
    imageShow("Result Image", result);
    imageWrite(outputPath, result);
    return;
}
vector<string> imageList(void)
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
    string road_image_07 = path_to_road_image + "test.png";

    vector<string> images;
    images.push_back(road_image_01);
    images.push_back(road_image_02);
    images.push_back(road_image_03);
    images.push_back(road_image_04);
    images.push_back(road_image_05);
    images.push_back(road_image_06);
    images.push_back(road_image_07);
    return images;
}
void processingMultipleImages(void)
{
    vector<string> images = imageList();
    int idx=0;
    for (string path : images)
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
void processingSingleVideo(string videoPath, string outputPath)
{
    Video(videoPath, outputPath);
    return;
}
vector<string> videoList(void)
{
    string path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/";
    string path_to_data = path_to_project + "Data/";
    string path_to_road_video = path_to_data + "Lane_Detection_Videos/";
    string road_video_01 = path_to_road_video + "solidWhiteRight.mp4";
    string road_video_02 = path_to_road_video + "solidYellowLeft.mp4";
    string road_video_03 = path_to_road_video + "challenge.mp4";

    vector<string> videos;
    videos.push_back(road_video_01);
    videos.push_back(road_video_02);
    videos.push_back(road_video_03);
    return videos;
}
void processingMultipleVideos(void)
{
    vector<string> videos = videoList();
    int idx=0;
    for (string path : videos)
    {
        Video(path, "output_" + to_string(idx) + ".mp4");
        idx++;
    }
    return;
}