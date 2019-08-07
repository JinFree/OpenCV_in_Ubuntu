from OpenCV_Functions import *

'''
def imageEdgePrewitt(image):
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]], np.float32)
    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]], np.float32)
    img_dx = imageFiltering(image, kernel_x)
    img_dy = imageFiltering(image, kernel_y)
    return img_dx + img_dy
def imageEdgeSobel(image):
    img_dx = cv2.Sobel(image, -1, 1, 0, ksize=3)
    img_dy = cv2.Sobel(image, -1, 0, 1, ksize=3)
    return img_dx + img_dy
def imageEdgeScharr(image):
    img_dx = cv2.Scharr(image, -1, 1, 0)
    img_dy = cv2.Scharr(image, -1, 0, 1)
    return img_dx + img_dy
def imageEdgeLaplacianCV(image):
    return cv2.Laplacian(image, -1)
'''

imagePath = "/home/opencv-mds/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow("image", image)

image_Prewitt = imageEdgePrewitt(image)
imageShow("image_Prewitt", image_Prewitt)

image_Sobel = imageEdgeSobel(image)
imageShow("image_Sobel", image_Sobel)

image_Scharr = imageEdgeScharr(image)
imageShow("image_Scharr", image_Scharr)

image_LaplacianCV = imageEdgeLaplacianCV(image)
imageShow("image_LaplacianCV", image_LaplacianCV)

laplacian_m4_kernel = np.array([
                                [0, 1, 0],
                                [1, -4, 1],
                                [0, 1, 0]], np.float32)

image_LaplacianFilter_m4 = imageFiltering(image, laplacian_m4_kernel)
imageShow("image_LaplacianFilter_m4", image_LaplacianFilter_m4)

laplacian_4_kernel = np.array([
                                [0, -1, 0],
                                [-1, 4, -1],
                                [0, -1, 0]], np.float32)

image_LaplacianFilter_4 = imageFiltering(image, laplacian_4_kernel)
imageShow("image_LaplacianFilter_4", image_LaplacianFilter_4)

laplacian_m8_kernel = np.array([
                                [1, 1, 1],
                                [1, -8, 1],
                                [1, 1, 1]], np.float32)

image_LaplacianFilter_m8 = imageFiltering(image, laplacian_m8_kernel)
imageShow("image_LaplacianFilter_m8", image_LaplacianFilter_m8)

laplacian_8_kernel = np.array([
                                [-1, -1, -1],
                                [-1, 8, -1],
                                [-1, -1, -1]], np.float32)

image_LaplacianFilter_8 = imageFiltering(image, laplacian_4_kernel)
imageShow("image_LaplacianFilter_8", image_LaplacianFilter_8)

cv2.destroyAllWindows()