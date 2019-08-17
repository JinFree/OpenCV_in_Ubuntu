from OpenCV_Functions import *

def imageProcessing(src, roi):
    dst = imageCopy(src)
    dst = convertColor(dst, cv2.COLOR_BGR2GRAY)
    dst = imageBilateralFilter(dst, 5, 10, 10)
    dst = imageClosing(dst)
    dst = imageMorphologicalGradient(dst)
    dst = cannyEdge(dst, 150, 300)
    dst = polyROI(dst, roi)
    lines = houghLinesP(dst, 1.0, np.pi/180., 75, 10, 50)
    dst = lineFittingMultiRoi(src, lines, roi, (0, 0, 255), 5)
    return dst


def openImages():
    path = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Projects/"
    
    Env_list = []
    ETS_H_list = []
    PC_F_list = []
    PC_H_list = []
    PC_T_list = []
    
    ETS_H_01 = "ETS_H_01.jpg"
    ETS_H_list.append(imageRead(path+ETS_H_01))
    
    PC_F_01 = "PC_F_01.jpg"
    PC_F_02 = "PC_F_02.jpg"
    PC_F_list.append(imageRead(path+PC_F_01))
    PC_F_list.append(imageRead(path+PC_F_02))
    
    PC_H_01 = "PC_H_01.jpg"
    PC_H_02 = "PC_H_02.jpg"
    PC_H_list.append(imageRead(path+PC_H_01))
    PC_H_list.append(imageRead(path+PC_H_02))
    
    PC_T_01 = "PC_T_01.jpg"
    PC_T_02 = "PC_T_02.jpg"
    PC_T_list.append(imageRead(path+PC_T_01))
    PC_T_list.append(imageRead(path+PC_T_02))
    
    Env_list.append(ETS_H_list)
    Env_list.append(PC_F_list)
    Env_list.append(PC_H_list)
    Env_list.append(PC_T_list)
    return Env_list


def ROI_definition():
    ROI_list = []
    
    # ROI for ETS_H_list
    pt1 = (580,390)
    pt2 = (750,390)
    pt3 = (1280,720)
    pt4 = (80,720)
    ROI_list.append(np.array([[pt1, pt2, pt3, pt4]], dtype=np.int32))
   
    # ROI for PC_F_list
    pt1 = (330,300)
    pt2 = (500,300)
    pt3 = (1100,450)
    pt4 = (-300,450)
    ROI_list.append(np.array([[pt1, pt2, pt3, pt4]],\
     dtype=np.int32))
   
    # ROI for ETS_H_list
    pt1 = (200,300)
    pt2 = (620,300)
    pt3 = (1100,450)
    pt4 = (-300,450)
    ROI_list.append(np.array([[pt1, pt2, pt3, pt4]],\
     dtype=np.int32))
   
    # ROI for PC_T_list
    pt1 = (250,300)
    pt2 = (550,300)
    pt3 = (800,430)
    pt4 = (0,430)
    ROI_list.append(np.array([[pt1, pt2, pt3, pt4]],\
     dtype=np.int32))

    return ROI_list


def ProcessingImages(image_list, ROI_list):
    result_list = []
    for i in range(len(image_list)):
        inner_list = []
        for j in range(len(image_list[i])):
            inner_list.append(imageProcessing(image_list[i][j], ROI_list[i]))
        result_list.append(inner_list)
    return result_list


def showImageList(name, doubleImageList):
    for i in range(len(doubleImageList)):
        for j in range(len(doubleImageList[i])):
            imageShow("{}[{}][{}]".format(name,i,j), doubleImageList[i][j])
    return



def ProjectImages():
    ROIs = ROI_definition()
    Images = openImages()
    result_list = ProcessingImages(Images, ROIs)
    showImageList("result_list", result_list)
    cv2.destroyAllWindows()
    return


def pathVideos():
    path = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Projects/"
    Env_list = []

    ETS_H_01 = "ETS_H_01.mp4"
    Env_list.append(path+ETS_H_01)
    
    PC_F_01 = "PC_F_01.mp4"
    Env_list.append(path+PC_F_01)
    
    PC_H_01 = "PC_H_01.mp4"
    Env_list.append(path+PC_H_01)
    
    PC_T_01 = "PC_T_01.mp4"
    Env_list.append(path+PC_T_01)

    return Env_list


def processingMultipleVideos(list_of_videos, ROI_list):
    for index in range(len(list_of_videos)):
        print(list_of_videos[index])
        Video2(list_of_videos[index], "output_{}.mp4".format(index),  ROI_list[index])
    return


def ProjectVideos():
    ROIs = ROI_definition()
    videos = pathVideos()
    processingMultipleVideos(videos, ROIs)
    return

ProjectImages()
#ProjectVideos()