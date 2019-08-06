from OpenCV_Functions import *

'''
def histogramEqualize(image):
    if len(image.shape) == 2:
        return cv2.equalizeHist(image)
    else:
        ch1, ch2, ch3 = splitImage(image)
        ch1_eq = histogramEqualize(ch1)
        ch2_eq = histogramEqualize(ch2)
        ch3_eq = histogramEqualize(ch3)
        return mergeImage(ch1_eq, ch2_eq, ch3_eq)
'''
imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowCurve2.jpg"
image = imageRead(imagePath) 
imageShow('image', image)
image_BGR_equalized = histogramEqualize(image)
imageShow("image_BGR_equalized", image_BGR_equalized)

imagegray = convertColor(image, cv2.COLOR_BGR2GRAY)
imageShow('imagegray', imagegray)
image_GRAY_equalized = histogramEqualize(imagegray)
imageShow("image_GRAY_equalized", image_GRAY_equalized)

imagehsv = convertColor(image, cv2.COLOR_BGR2HSV)
h, s, v = splitImage(imagehsv)
s_eq = histogramEqualize(s)
v_eq = histogramEqualize(v)
image_hseqveq = mergeImage(h, s_eq, v_eq)
image_hsveq = mergeImage(h, s, v_eq)
image_hseqv = mergeImage(h, s_eq, v)
image_hseqveq_bgr = convertColor(image_hseqveq, cv2.COLOR_HSV2BGR)
image_hsveq_bgr = convertColor(image_hsveq, cv2.COLOR_HSV2BGR)
image_hseqv_bgr = convertColor(image_hseqv, cv2.COLOR_HSV2BGR)
imageShow('image', image)
imageShow("image_hseqveq_bgr", image_hseqveq_bgr)
imageShow("image_hsveq_bgr", image_hsveq_bgr)
imageShow("image_hseqv_bgr", image_hseqv_bgr)

imagehls = convertColor(image, cv2.COLOR_BGR2HLS)
h, l, s = splitImage(imagehls)
l_eq = histogramEqualize(l)
s_eq = histogramEqualize(s)
image_hleqseq = mergeImage(h, l_eq, s_eq)
image_hlseq = mergeImage(h, l, s_eq)
image_hleqs = mergeImage(h, l_eq, s)
image_hleqseq_bgr = convertColor(image_hleqseq, cv2.COLOR_HLS2BGR)
image_hlseq_bgr = convertColor(image_hlseq, cv2.COLOR_HLS2BGR)
image_hleqs_bgr = convertColor(image_hleqs, cv2.COLOR_HLS2BGR)
imageShow('image', image)
imageShow("image_hleqseq_bgr", image_hleqseq_bgr)
imageShow("image_hlseq_bgr", image_hlseq_bgr)
imageShow("image_hleqs_bgr", image_hleqs_bgr)

cv2.destroyAllWindows()