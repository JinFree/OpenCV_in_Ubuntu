from OpenCV_Utils import *


def imageProcessing(image):
    result = imageCopy(image)
    return result


def processingSingleImage(imagePath, outputPath = "output.jpg"):
    image = imageRead(imagePath)
    imageShow("Opened Image", image)
    result = imageProcessing(image)
    imageShow("Result Image", result)
    imageWrite(outputPath, result)
    return


def imageList():
    path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/"
    path_to_data = path_to_project + "Data/"
    path_to_road_image = path_to_data + "Lane_Detection_Images/"

    road_image_01 = path_to_road_image + "solidWhiteCurve.jpg"
    road_image_02 = path_to_road_image + "solidWhiteRight.jpg"
    road_image_03 = path_to_road_image + "solidYellowCurve.jpg"
    road_image_04 = path_to_road_image + "solidYellowCurve2.jpg"
    road_image_05 = path_to_road_image + "solidYellowLeft.jpg"
    road_image_06 = path_to_road_image + "whiteCarLaneSwitch.jpg"
    road_image_07 = path_to_road_image + "test.png"

    images=[]
    images.append(road_image_01)
    images.append(road_image_02)
    images.append(road_image_03)
    images.append(road_image_04)
    images.append(road_image_05)
    images.append(road_image_06)
    images.append(road_image_07)
    return images


def processingMultipleImages():
    list_of_images = imageList()
    for index in range(len(list_of_images)):
        image = imageRead(list_of_images[index])
        imageShow("Image index is {}".format(index), image)
        result = imageProcessing(image)
        imageShow("Result of index {}".format(index), result)
        imageWrite("Result_{}.jpg".format(index), result)
    return


def processingSingleVideo(videoPath, outputPath = "output.avi"):
    Video(videoPath, outputPath)
    return


def videoList():
    path_to_project = "/home/opencv-mds/OpenCV_in_Ubuntu/"
    path_to_data = path_to_project + "Data/"
    path_to_road_video = path_to_data + "Lane_Detection_Videos/"
    road_video_01 = path_to_road_video + "solidWhiteRight.mp4"
    road_video_02 = path_to_road_video + "solidYellowLeft.mp4"
    road_video_03 = path_to_road_video + "challenge.mp4"
    
    videos=[]
    videos.append(road_video_01)
    videos.append(road_video_02)
    videos.append(road_video_03)
    return videos


def processingMultipleVideos():
    list_of_videos = videoList()
    for index in range(len(list_of_videos)):
        Video(list_of_videos[index], "output_{}.mp4".format(index))
    return
