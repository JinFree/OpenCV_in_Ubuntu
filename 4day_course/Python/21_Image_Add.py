from OpenCV_Functions import *

'''
def addImage(image1, image2):
    return cv2.add(image1, image2)
'''

import os
home = os.environ['HOME']
imagePath_1 = home + "/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
imagePath_2 = home + "/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidYellowLeft.jpg"
image_1 = imageRead(imagePath_1) 
image_2 = imageRead(imagePath_2) 
imageShow('image_1', image_1)

lower_white_hsv = np.array([0, 0, 150])
upper_white_hsv = np.array([179, 10, 255])
lower_yellow_hsv = np.array([20, 75, 150])
upper_yellow_hsv = np.array([35, 255, 255])

image_1_hsv = convertColor(image_1, cv2.COLOR_BGR2HSV)

output_W_hsv = splitColor(image_1_hsv, lower_white_hsv, upper_white_hsv)
output_Y_hsv = splitColor(image_1_hsv, lower_yellow_hsv, upper_yellow_hsv)

output_hsv = addImage(output_W_hsv, output_Y_hsv)
output_bgr = convertColor(output_hsv, cv2.COLOR_HSV2BGR)

output_hsv2 = output_W_hsv+output_Y_hsv
output_bgr2 = convertColor(output_hsv2, cv2.COLOR_HSV2BGR)

imageShow("output_bgr", output_bgr)
imageShow("output_bgr2", output_bgr2)

cv2.destroyAllWindows()

image_sum_1 = addImage(image_1, image_2)
image_sum_2 = image_1 + image_2

print("image_1, value at (463, 175)", getPixel(image_1, 463, 175))
print("image_2, value at (463, 175)", getPixel(image_2, 463, 175))
print("image_sum_1, value at (463, 175)", getPixel(image_sum_1, 463, 175))
print("image_sum_2, value at (463, 175)", getPixel(image_sum_2, 463, 175))

imageShow('image_1', image_1)
imageShow('image_2', image_2)
imageShow("image_sum_1", image_sum_1)
imageShow("image_sum_2", image_sum_2)

cv2.destroyAllWindows()