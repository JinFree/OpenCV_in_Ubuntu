from OpenCV_Functions import *

'''
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
    traffic_image_07 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/traffic_light_image_01.PNG"
    traffic_image_08 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/traffic_light_image_02.PNG"
    traffic_image_09 = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/traffic_light_image_03.PNG"
    return traffic_image_01
def processingSingleImage(imagePath, outputPath = "output.jpg"):
    image = imageRead(imagePath)
    imageShow("Opened Image", image)
    result = imageProcessing(image)
    imageShow("Result Image", result)
    imageWrite(outputPath, result)
    return
'''
processingSingleImage(path_to_images())