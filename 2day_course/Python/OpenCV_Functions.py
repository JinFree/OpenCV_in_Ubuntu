from OpenCV_Utils import *


def imageProcessing(image):
    result = imageCopy(image)
    return result


def path_to_images():
    road_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
    road_image_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteRight.jpg"
    road_image_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve.jpg"
    road_image_04 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve2.jpg"
    road_image_05 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowLeft.jpg"
    road_image_06 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/whiteCarLaneSwitch.jpg"
    road_image_07 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/test.png"

    traffic_image_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
    traffic_image_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_02.png"
    traffic_image_03 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/red_light_01.png"
    traffic_image_04 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/red_light_02.png"
    traffic_image_05 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/yellow_light_01.png"
    traffic_image_06 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/yellow_light_02.png"
    return traffic_image_01


def processingSingleImage(imagePath, outputPath = "output.jpg"):
    image = imageRead(imagePath)
    imageShow("Opened Image", image)
    result = imageProcessing(image)
    imageShow("Result Image", result)
    imageWrite(outputPath, result)
    return


def imageList_LaneDetection():
    path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/"
    path_to_data = path_to_project + "Data/"
    path_to_road_image = path_to_data + "Lane_Detection_Images/"

    image_01 = path_to_road_image + "solidWhiteCurve.jpg"
    image_02 = path_to_road_image + "solidWhiteRight.jpg"
    image_03 = path_to_road_image + "solidYellowCurve.jpg"
    image_04 = path_to_road_image + "solidYellowCurve2.jpg"
    image_05 = path_to_road_image + "solidYellowLeft.jpg"
    image_06 = path_to_road_image + "whiteCarLaneSwitch.jpg"

    images=[]
    images.append(image_01)
    images.append(image_02)
    images.append(image_03)
    images.append(image_04)
    images.append(image_05)
    images.append(image_06)
    return images


def imageList_TrafficLightDetection():
    path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/"
    path_to_data = path_to_project + "Data/"
    path_to_road_image = path_to_data + "TrafficLight_Detection/"

    image_01 = path_to_road_image + "green_light_01.png"
    image_02 = path_to_road_image + "green_light_02.png"
    image_03 = path_to_road_image + "red_light_01.png"
    image_04 = path_to_road_image + "red_light_02.png"
    image_05 = path_to_road_image + "yellow_light_01.png"
    image_06 = path_to_road_image + "yellow_light_02.png"
    
    images=[]
    images.append(image_01)
    images.append(image_02)
    images.append(image_03)
    images.append(image_04)
    images.append(image_05)
    images.append(image_06)
    return images


def processingMultipleImages(list_of_images):
    for index in range(len(list_of_images)):
        image = imageRead(list_of_images[index])
        imageShow("Image index is {}".format(index), image)
        result = imageProcessing(image)
        imageShow("Result of index {}".format(index), result)
        imageWrite("Result_{}.jpg".format(index), result)
    return


def path_to_videos():
    road_video_01 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidWhiteRight.mp4"
    road_video_02 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Videos/solidYellowLeft.mp4"
    return road_video_01


def processingSingleVideo(videoPath, outputPath = "output.avi"):
    Video(videoPath, outputPath)
    return


def videoList_LaneDetection():
    path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/"
    path_to_data = path_to_project + "Data/"
    path_to_road_video = path_to_data + "Lane_Detection_Videos/"
    road_video_01 = path_to_road_video + "solidWhiteRight.mp4"
    road_video_02 = path_to_road_video + "solidYellowLeft.mp4"
    
    videos=[]
    videos.append(road_video_01)
    videos.append(road_video_02)
    return videos


def processingMultipleVideos(list_of_videos):
    for index in range(len(list_of_videos)):
        Video(list_of_videos[index], "output_{}.mp4".format(index))
    return
