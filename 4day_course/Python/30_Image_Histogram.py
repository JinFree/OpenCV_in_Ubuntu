from OpenCV_Functions import *

'''
def computeHist(image, mask=None):
    bins = np.arange(256).reshape(256,1)
    if len(image.shape)==2:
        h = np.zeros((300,256,1))
        hist_item = cv2.calcHist([image],[0],None,[256],[0,255]) 
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
        hist=np.int32(np.around(hist_item)) 
        pts = np.column_stack((bins,hist)) 
        cv2.polylines(h,[pts],False, 255)
    else:
        h = np.zeros((300,256,3))
        color = [ (255,0,0),(0,255,0),(0,0,255) ] 
        for ch, col in enumerate(color): 
            hist_item = cv2.calcHist([image],[ch],None,[256],[0,255]) 
            cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
            hist=np.int32(np.around(hist_item)) 
            pts = np.column_stack((bins,hist)) 
            cv2.polylines(h,[pts],False,col)
    return np.flipud(h)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow('image', image)
imageHist = computeHist(image)
imageShow("imageHist", imageHist)

imagegray = convertColor(image, cv2.COLOR_BGR2GRAY)
imageShow('imagegray', imagegray)
imagegrayHist = computeHist(imagegray)
imageShow("imagegrayHist", imagegrayHist)

imagehsv = convertColor(image, cv2.COLOR_BGR2HSV)
imageShow('imagehsv', imagehsv)
imagehsvHist = computeHist(imagehsv)
imageShow("imagehsvHist", imagehsvHist)

imagehls = convertColor(image, cv2.COLOR_BGR2HLS)
imageShow('imagehls', imagehls)
imagehlsHist = computeHist(imagehls)
imageShow("imagehlsHist", imagehlsHist)

cv2.destroyAllWindows()