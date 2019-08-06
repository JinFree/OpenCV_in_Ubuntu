from OpenCV_Functions import *

'''
def drawText(image, text, point=(10, 10), font=cv2.FONT_HERSHEY_PLAIN, fontScale=2.0, color=(255,255,255), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.putText(result, text, point, font, fontScale, color, thickness, lineType)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/TrafficLight_Detection/green_light_01.png"
image = imageRead(imagePath) 
imageShow('image', image)

image_text_01 = drawText(image, "Traffic Light", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
image_text_01 = drawCircle(image_text_01, (10, 50), 5, (0, 0, 255), -1)
imageShow("image_text_01", image_text_01)

image_text_02 = drawText(image, "cv2.FONT_HERSHEY_SIMPLEX", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_PLAIN", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_DUPLEX", (10, 150), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_COMPLEX", (10, 200), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_TRIPLEX", (10, 250), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_COMPLEX_SMALL", (10, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_SCRIPT_SIMPLEX", (10, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 0, 0), 1)
image_text_02 = drawText(image_text_02, "cv2.FONT_HERSHEY_SCRIPT_COMPLEX", (10, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (255, 0, 0), 1)
imageShow("image_text_02", image_text_02)

cv2.destroyAllWindows()