from OpenCV_Functions import *

'''
def imageFiltering(image, kernel, ddepth=-1):
    return cv2.filter2D(image, ddepth, kernel)
'''

imagePath = "~/OpenCV_in_Ubuntu/Data/Lane_Detection_Images/solidWhiteCurve.jpg"
image = imageRead(imagePath) 
imageShow("image", image)


mean_kernel = 1. / 25. * np.array([
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1]], np.float32)

mean_filtered_image = imageFiltering(image, mean_kernel)
imageShow("mean_filtered_image", mean_filtered_image)

gaussian_kernel = 1. / 256. * np.array([
                                [1, 4, 6, 4, 1],
                                [4, 16, 24, 16, 4],
                                [6, 24, 46, 24, 6], 
                                [4, 16, 24, 16, 4],
                                [1, 4, 6, 4, 1]], np.float32)

gaussian_filtered_image = imageFiltering(image, gaussian_kernel)
imageShow("gaussian_filtered_image", gaussian_filtered_image)

cv2.destroyAllWindows()