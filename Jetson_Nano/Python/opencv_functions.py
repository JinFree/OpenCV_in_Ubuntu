import numpy as np
import cv2

def imageParameters(imageName, image):
    # Get Image Dimension (Grayscale or RGB-Scale)
    if len(image.shape) == 2 :
        height, width = image.shape
    elif len(image.shape) == 3 :
        height, width, channel = image.shape
    
    # Show Image Features
    print(f"{imageName}.shape is {image.shape}")
    print(f"{imageName}.shape[0] is Height: {height}")
    print(f"{imageName}.shape[1] is Width: {width}")
    
    # Show Image Dimension
    if len(image.shape) == 2 :
        print("This is Grayscale Image.")
        print(f"{imageName}.shape[2] is Not exist, So channel is 1")
    elif len(image.shape) == 3 :
        print("This is not Grayscale Image.")
        print(f"{imageName}.shape[2] is channels: {channel}")
    
    print(f"{imageName}.dtype is {image.dtype}")
    
    return height, width

def getPixel(image: cv2.Mat, x: int, y: int, c: int=None) -> list[int, np.ndarray]:
    """
    Get pixel value at (x, y) in the image.
    """
    retVal = None
    if len(image.shape) == 2:  # Grayscale image
        retVal = image[y, x]
    elif len(image.shape) == 3:  # Color image
        retVal = image[y, x, c]
    else:
        raise ValueError("Unsupported image format")
    return retVal

def setPixel(image: cv2.Mat, x: int, y: int, value: np.ndarray, c: int=None) -> None:
    """
    Set pixel value at (x, y) in the image.
    """
    if len(image.shape) == 2:  # Grayscale image
        image[y, x] = value
    elif len(image.shape) == 3:  # Color image
        image[y, x, c] = value
    else:
        raise ValueError("Unsupported image format")
    
def imageCopy(image_src: cv2.Mat) -> cv2.Mat:
    """
    Create a copy of the image.
    """
    return np.copy(image_src)

def cutRectROI(image_src: cv2.Mat, x1: int, y1: int, x2: int, y2: int) -> cv2.Mat:
    """
    Cut a rectangular Region of Interest (ROI) from the image.
    """
    assert x2 < image_src.shape[1] and y2 < image_src.shape[0], "ROI exceeds image boundaries"
    assert x1 < x2 and y1 < y2, "Invalid ROI coordinates"
    return imageCopy(image_src[y1:y2, x1:x2])

def pasteRectROI(image_src: cv2.Mat, image_roi: cv2.Mat, x1: int, y1: int) -> cv2.Mat:
    """
    Paste a rectangular Region of Interest (ROI) into the image.
    """
    assert x1 >= 0 and y1 >= 0, "Invalid paste coordinates"
    assert x1 + image_roi.shape[1] <= image_src.shape[1] and y1 + image_roi.shape[0] <= image_src.shape[0], "Pasting exceeds image boundaries"
    image_dst = imageCopy(image_src)
    image_dst[y1:y1 + image_roi.shape[0], x1:x1 + image_roi.shape[1]] = image_roi
    return imageCopy(image_dst)

def fillPolygon(image_src: cv2.Mat, points: np.ndarray, color: list[list, tuple]) -> cv2.Mat:
    assert len(points.shape) == 2 and points.shape[1] == 2, "Points must be a Nx2 array"
    image_dst = imageCopy(image_src)
    cv2.fillPoly(image_dst, [points.astype(np.int32)], color)
    return image_dst
    
def makeBlackImage(height: int, width: int, is_color: bool = False) -> cv2.Mat:
    if is_color:
        return np.zeros((height, width, 3), dtype=np.uint8)
    else:
        return np.zeros((height, width), dtype=np.uint8)    

def polyROI(image_src: cv2.Mat, points: np.ndarray) -> cv2.Mat:
    mask = makeBlackImage(image_src.shape[0], image_src.shape[1], is_color=(len(image_src.shape) == 3))
    white_color = 255 if len(image_src.shape) == 2 else (255, 255, 255)
    mask = fillPolygon(mask, points, white_color)
    return cv2.bitwise_and(image_src, mask)

def splitImage(image_src: cv2.Mat) -> list[cv2.Mat]:
    if len(image_src.shape) == 3:
        return cv2.split(image_src)
    else:
        raise ValueError("Image is not a color image")
    
def mergeImages(channels: list[cv2.Mat]) -> cv2.Mat:
    if len(channels) == 3:
        return cv2.merge(channels)
    else:
        raise ValueError("Invalid number of channels for merging")
    
def convertColor(image_src: cv2.Mat, flag: int = cv2.COLOR_BGR2GRAY) -> cv2.Mat:
    return imageCopy(cv2.cvtColor(image_src, flag))

def nothing(x):
    pass

def empty_image(size: int = 10) -> cv2.Mat:
    return np.zeros((size, size, 3), np.uint8)

def bar_RGB(size: int = 10):
    window_name = "RGB Trackbar"
    cv2.namedWindow(window_name)
    cv2.resizeWindow(window_name, size, size)
    cv2.createTrackbar("R", window_name, 128, 255, nothing)
    cv2.createTrackbar("G", window_name, 128, 255, nothing)
    cv2.createTrackbar("B", window_name, 128, 255, nothing)
    
    img = empty_image(size)
    
    while True:
        r = cv2.getTrackbarPos("R", window_name)
        g = cv2.getTrackbarPos("G", window_name)
        b = cv2.getTrackbarPos("B", window_name)
        
        img[:] = [b, g, r]  # OpenCV uses BGR format
        cv2.imshow(window_name, img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
def bar_HLS(size: int = 10):
    window_name = "HLS Trackbar"
    cv2.namedWindow(window_name)
    cv2.resizeWindow(window_name, size, size)
    cv2.createTrackbar("H", window_name, 0, 179, nothing)
    cv2.createTrackbar("L", window_name, 128, 255, nothing)
    cv2.createTrackbar("S", window_name, 128, 255, nothing)
    
    img = empty_image(size)
    
    while True:
        h = cv2.getTrackbarPos("H", window_name)
        l = cv2.getTrackbarPos("L", window_name)
        s = cv2.getTrackbarPos("S", window_name)
        
        img[:] = [h, l, s]  # OpenCV uses HLS format
        img_hls = cv2.cvtColor(img, cv2.COLOR_HLS2BGR)
        cv2.imshow(window_name, img_hls)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
def bar_HSV(size: int = 10):
    window_name = "HSV Trackbar"
    cv2.namedWindow(window_name)
    cv2.resizeWindow(window_name, size, size)
    cv2.createTrackbar("H", window_name, 0, 179, nothing)
    cv2.createTrackbar("S", window_name, 128, 255, nothing)
    cv2.createTrackbar("V", window_name, 128, 255, nothing)
    
    img = empty_image(size)
    
    while True:
        h = cv2.getTrackbarPos("H", window_name)
        s = cv2.getTrackbarPos("S", window_name)
        v = cv2.getTrackbarPos("V", window_name)
        
        img[:] = [h, s, v]  # OpenCV uses HSV format
        img_hsv = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        cv2.imshow(window_name, img_hsv)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
def rangeColor(image_src: cv2.Mat, lower: list[list[int], np.array], upper: list[list[int], np.array]) -> cv2.Mat:
    image_dst = imageCopy(image_src)
    return cv2.inRange(image_dst, lower, upper)

def splitColor(image_src: cv2.Mat, lower: list[list[int], np.array], upper: list[list[int], np.array]) -> cv2.Mat:
    image_dst = imageCopy(image_src)
    mask = rangeColor(image_src, lower, upper)
    return cv2.bitwise_and(image_dst, image_dst, mask=mask)

def bar_HSV_range(image_src:cv2.Mat):
    image_hsv = convertColor(image_src, cv2.COLOR_BGR2HSV)
    window_name = "HSV range Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("H_lower", window_name, 0, 179, nothing)
    cv2.createTrackbar("S_lower", window_name, 0, 255, nothing)
    cv2.createTrackbar("V_lower", window_name, 0, 255, nothing)
    cv2.createTrackbar("H_upper", window_name, 179, 179, nothing)
    cv2.createTrackbar("S_upper", window_name, 255, 255, nothing)
    cv2.createTrackbar("V_upper", window_name, 255, 255, nothing)
    while True:
        h_lower = cv2.getTrackbarPos("H_lower", window_name)
        s_lower = cv2.getTrackbarPos("S_lower", window_name)
        v_lower = cv2.getTrackbarPos("V_lower", window_name)
        h_upper = cv2.getTrackbarPos("H_upper", window_name)
        s_upper = cv2.getTrackbarPos("S_upper", window_name)
        v_upper = cv2.getTrackbarPos("V_upper", window_name)

        lower_bound = np.array([h_lower, s_lower, v_lower])
        upper_bound = np.array([h_upper, s_upper, v_upper])
        
        image_dst = splitColor(image_hsv, lower_bound, upper_bound)
        image_bgr = cv2.cvtColor(image_dst, cv2.COLOR_HSV2BGR)
        cv2.imshow(window_name, image_bgr)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_bgr

def bar_HLS_range(image_src:cv2.Mat):
    image_hls = convertColor(image_src, cv2.COLOR_BGR2HLS)
    window_name = "HLS range Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("H_lower", window_name, 0, 179, nothing)
    cv2.createTrackbar("L_lower", window_name, 0, 255, nothing)
    cv2.createTrackbar("S_lower", window_name, 0, 255, nothing)
    cv2.createTrackbar("H_upper", window_name, 179, 179, nothing)
    cv2.createTrackbar("L_upper", window_name, 255, 255, nothing)
    cv2.createTrackbar("S_upper", window_name, 255, 255, nothing)
    while True:
        h_lower = cv2.getTrackbarPos("H_lower", window_name)
        l_lower = cv2.getTrackbarPos("L_lower", window_name)
        s_lower = cv2.getTrackbarPos("S_lower", window_name)
        h_upper = cv2.getTrackbarPos("H_upper", window_name)
        l_upper = cv2.getTrackbarPos("L_upper", window_name)
        s_upper = cv2.getTrackbarPos("S_upper", window_name)

        lower_bound = np.array([h_lower, l_lower, s_lower])
        upper_bound = np.array([h_upper, l_upper, s_upper])
        
        image_dst = splitColor(image_hls, lower_bound, upper_bound)
        image_bgr = cv2.cvtColor(image_dst, cv2.COLOR_HLS2BGR)
        cv2.imshow(window_name, image_bgr)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_bgr

def drawLine(image_src: cv2.Mat, pt1: tuple[int, int], pt2: tuple[int, int], color: list[int, np.ndarray], thickness: int = 1) -> cv2.Mat:
    """
    Draw a line on the image from pt1 to pt2 with the specified color and thickness.
    """
    image_dst = imageCopy(image_src)
    cv2.line(image_dst, pt1, pt2, color, thickness)
    return image_dst
    
def drawRect(image_src: cv2.Mat, pt1: tuple[int, int], pt2: tuple[int, int], color: list[int, np.ndarray], thickness: int = 1) -> cv2.Mat:
    """
    Draw a rectangle on the image with the specified top-left and bottom-right points, color, and thickness.
    """
    image_dst = imageCopy(image_src)
    cv2.rectangle(image_dst, pt1, pt2, color, thickness)
    return image_dst

def drawCircle(image_src: cv2.Mat, center: tuple[int, int], radius: int, color: list[int, np.ndarray], thickness: int = 1) -> cv2.Mat:
    """
    Draw a circle on the image with the specified center, radius, color, and thickness.
    """
    image_dst = imageCopy(image_src)
    cv2.circle(image_dst, center, radius, color, thickness)
    return image_dst

def drawPolygon(image_src: cv2.Mat, points: np.ndarray, isClosed:bool, color: list[int, np.ndarray], thickness: int = 1) -> cv2.Mat:
    """
    Draw a polygon on the image with the specified points, color, and thickness.
    """
    assert len(points.shape) == 2 and points.shape[1] == 2, "Points must be a Nx2 array"
    image_dst = imageCopy(image_src)
    cv2.polylines(image_dst, [points.astype(np.int32)], isClosed=isClosed, color=color, thickness=thickness)
    return image_dst

def drawText(image_src: cv2.Mat, text: str, org: tuple[int, int], fontFace: int, fontScale: float, color: list[int, np.ndarray], thickness: int = 1) -> cv2.Mat:
    """
    Draw text on the image at the specified position with the specified font, scale, color, and thickness.
    """
    image_dst = imageCopy(image_src)
    cv2.putText(image_dst, text, org, fontFace, fontScale, color, thickness)
    return image_dst

def imageThreshold(image_src: cv2.Mat, thresh: int = 127, maxval: int = 255, type: int = cv2.THRESH_BINARY) -> cv2.Mat:
    """
    Apply a binary threshold to the image.
    """
    image_dst = imageCopy(image_src)
    _, image_dst = cv2.threshold(image_dst, thresh, maxval, type)
    return image_dst

def computeHistogram(image_src: cv2.Mat) -> np.ndarray:
    """
    Compute the histogram of the image for the specified channels.
    """
    bins = np.arange(256).reshape(256,1)
    if len(image_src.shape)==2:
        h = np.zeros((300,256,1))
        hist_item = cv2.calcHist([image_src],[0],None,[256],[0,255]) 
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
        hist=np.int32(np.around(hist_item)) 
        pts = np.column_stack((bins,hist)) 
        cv2.polylines(h,[pts],False, 255)
    else:
        h = np.zeros((300,256,3))
        color = [ (255,0,0),(0,255,0),(0,0,255) ] 
        for ch, col in enumerate(color): 
            hist_item = cv2.calcHist([image_src],[ch],None,[256],[0,255]) 
            cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
            hist=np.int32(np.around(hist_item)) 
            pts = np.column_stack((bins,hist)) 
            cv2.polylines(h,[pts],False,col)
    return np.flipud(h)

def equalizeHistogram(image_src: cv2.Mat) -> cv2.Mat:
    """
    Apply histogram equalization to the image.
    """
    image_dst = imageCopy(image_src)
    if len(image_dst.shape) == 2:  # Grayscale image
        return cv2.equalizeHist(image_dst)
    elif len(image_dst.shape) == 3:  # Color image
        ch1, ch2, ch3 = cv2.split(image_dst)
        ch1 = cv2.equalizeHist(ch1) 
        ch2 = cv2.equalizeHist(ch2)
        ch3 = cv2.equalizeHist(ch3)
        return cv2.merge((ch1, ch2, ch3))
    else:
        raise ValueError("Unsupported image format for histogram equalization")
    
def imageBlur(image_src: cv2.Mat, ksize_x: int, ksize_y: int) -> cv2.Mat:
    assert ksize_x > 0 and ksize_y > 0, "Kernel size must be greater than 0"
    assert ksize_x % 2 == 1 and ksize_y % 2 == 1, "Kernel size must be odd"
    return cv2.blur(image_src, (ksize_x, ksize_y))

def bar_blur(image_src: cv2.Mat):
    window_name = "Blur Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("ksize_x", window_name, 3, 20, nothing)
    cv2.createTrackbar("ksize_y", window_name, 3, 20, nothing)
    
    while True:
        ksize_x = cv2.getTrackbarPos("ksize_x", window_name)
        ksize_y = cv2.getTrackbarPos("ksize_y", window_name)
        if ksize_x % 2 == 0: ksize_x += 1
        if ksize_y % 2 == 0: ksize_y += 1
        image_dst = imageGaussianBlur(image_src, ksize_x, ksize_y)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageGaussianBlur(image_src: cv2.Mat, ksize_x: int, ksize_y: int, sigmaX: float = 0, sigmaY: float = 0) -> cv2.Mat:
    assert ksize_x > 0 and ksize_y > 0, "Kernel size must be greater than 0"
    assert ksize_x % 2 == 1 and ksize_y % 2 == 1, "Kernel size must be odd"
    return cv2.GaussianBlur(image_src, (ksize_x, ksize_y), sigmaX, sigmaY)

def bar_gaussian_blur(image_src: cv2.Mat):
    window_name = "Gaussian Blur Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("ksize_x", window_name, 3, 20, nothing)
    cv2.createTrackbar("ksize_y", window_name, 3, 20, nothing)
    cv2.createTrackbar("sigmaX", window_name, 0, 100, nothing)
    cv2.createTrackbar("sigmaY", window_name, 0, 100, nothing)
    
    while True:
        ksize_x = cv2.getTrackbarPos("ksize_x", window_name)
        ksize_y = cv2.getTrackbarPos("ksize_y", window_name)
        if ksize_x % 2 == 0: ksize_x += 1
        if ksize_y % 2 == 0: ksize_y += 1
        sigmaX = cv2.getTrackbarPos("sigmaX", window_name)
        sigmaY = cv2.getTrackbarPos("sigmaY", window_name)
        image_dst = imageGaussianBlur(image_src, ksize_x, ksize_y, sigmaX, sigmaY)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageMedianBlur(image_src: cv2.Mat, ksize: int) -> cv2.Mat:
    assert ksize > 0, "Kernel size must be greater than 0"
    assert ksize % 2 == 1, "Kernel size must be odd"
    return cv2.medianBlur(image_src, ksize)

def bar_median_blur(image_src: cv2.Mat):
    window_name = "Median Blur Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("ksize", window_name, 3, 20, nothing)
    
    while True:
        ksize = cv2.getTrackbarPos("ksize", window_name)
        if ksize % 2 == 0: ksize += 1
        image_dst = imageMedianBlur(image_src, ksize)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageBilateralFilter(image_src: cv2.Mat, d: int, sigmaColor: float, sigmaSpace: float) -> cv2.Mat:
    assert d > 0, "Diameter must be greater than 0"
    return cv2.bilateralFilter(image_src, d, sigmaColor, sigmaSpace)

def bar_bilateral_filter(image_src: cv2.Mat):
    window_name = "Bilateral Filter Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("d", window_name, 5, 100, nothing)
    cv2.createTrackbar("sigmaColor", window_name, 75, 200, nothing)
    cv2.createTrackbar("sigmaSpace", window_name, 75, 200, nothing)
    
    while True:
        d = cv2.getTrackbarPos("d", window_name)
        sigmaColor = cv2.getTrackbarPos("sigmaColor", window_name)
        sigmaSpace = cv2.getTrackbarPos("sigmaSpace", window_name)
        image_dst = imageBilateralFilter(image_src, d, sigmaColor, sigmaSpace)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageFiltering(image_src: cv2.Mat, kernel: np.ndarray, ddepth: int=-1) -> cv2.Mat:
    """
    Apply a custom filter to the image using the specified kernel.
    """
    assert kernel.ndim == 2, "Kernel must be a 2D array"
    return cv2.filter2D(image_src, ddepth, kernel)

def houghCircles(image_src: cv2.Mat, dp: float = 1, minDist: float = 10, canny: int = 50, threshold: int = 30, minRadius: int = 0, maxRadius: int = 0) -> list[tuple[int, int, int]]:
    """
    Detect circles in the image using the Hough Circle Transform.
    """
    circles = cv2.HoughCircles(image_src, cv2.HOUGH_GRADIENT, dp, minDist, param1=canny, param2=threshold, minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        return [(x, y, r) for x, y, r in circles[0, :]]
    return []

def drawHoughCircles(image_src: cv2.Mat, circles: list[tuple[int, int, int]]) -> cv2.Mat:
    """
    Draw detected circles on the image.
    """
    image_dst = imageCopy(image_src)
    for x, y, r in circles:
        cv2.circle(image_dst, (x, y), r, (0, 255, 0), 4)  # Draw circle outline
        cv2.circle(image_dst, (x, y), 3, (0, 0, 255), -1)  # Draw center point
    return image_dst
    
def bar_hough_circles(image_src: cv2.Mat) -> cv2.Mat:
    image_gray = imageCopy(image_src) if len(image_src.shape) == 2 else imageCopy(cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY))
    window_name = "Hough Circles Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("dp", window_name, 1, 10, nothing)
    cv2.createTrackbar("minDist", window_name, 10, 100, nothing)
    cv2.createTrackbar("canny", window_name, 50, 100, nothing)
    cv2.createTrackbar("threshold", window_name, 30, 100, nothing)
    cv2.createTrackbar("minRadius", window_name, 0, 100, nothing)
    cv2.createTrackbar("maxRadius", window_name, 0, 100, nothing)
    
    while True:
        dp = cv2.getTrackbarPos("dp", window_name)
        minDist = cv2.getTrackbarPos("minDist", window_name)
        canny = cv2.getTrackbarPos("canny", window_name)
        threshold = cv2.getTrackbarPos("threshold", window_name)
        minRadius = cv2.getTrackbarPos("minRadius", window_name)
        maxRadius = cv2.getTrackbarPos("maxRadius", window_name)

        circles = houghCircles(image_gray, dp=dp, minDist=minDist, canny=canny, threshold=threshold, minRadius=minRadius, maxRadius=maxRadius)
        image_dst = drawHoughCircles(image_src, circles)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageEdgePrewitt(image_src: cv2.Mat) -> cv2.Mat:
    kernelX = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]], np.float32) 
    kernelY = np.array([[-1, -1, -1],
                        [0, 0, 0],
                        [1, 1, 1]], np.float32) 
    imageDeltaX = imageFiltering(image_src, kernelX) 
    imageDeltaY = imageFiltering(image_src, kernelY)
    return imageDeltaX + imageDeltaY
    
def imageEdgeSobel(image_src: cv2.Mat) -> cv2.Mat:
    imageDeltaX = cv2.Sobel(image_src, -1, 1, 0, ksize=3) 
    imageDeltaY = cv2.Sobel(image_src, -1, 0, 1, ksize=3) 
    return imageDeltaX + imageDeltaY

def imageEdgeScharr(image_src: cv2.Mat) -> cv2.Mat:
    imageDeltaX = cv2.Scharr(image_src, -1, 1, 0)
    imageDeltaY = cv2.Scharr(image_src, -1, 0, 1) 
    return imageDeltaX + imageDeltaY

def imageEdgeLaplacianCV(image_src: cv2.Mat, ksize: int=-1) -> cv2.Mat:
    return cv2.Laplacian(image_src, ksize) # ksize 지정 가능

def imageEdgeCanny(image_src: cv2.Mat, threshold1: int = 100, threshold2: int = 200) -> cv2.Mat:
    """
    Apply Canny edge detection to the image.
    """
    return cv2.Canny(image_src, threshold1, threshold2)

def bar_edge_detection(image_src: cv2.Mat):
    window_name = "Edge Detection Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("threshold1", window_name, 100, 255, nothing)
    cv2.createTrackbar("threshold2", window_name, 200, 255, nothing)
    
    while True:
        threshold1 = cv2.getTrackbarPos("threshold1", window_name)
        threshold2 = cv2.getTrackbarPos("threshold2", window_name)
        image_dst = imageEdgeCanny(image_src, threshold1, threshold2)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def imageDilation(image_src: cv2.Mat, kernel: np.ndarray = np.ones((3, 3), np.uint8), iterations: int = 1) -> cv2.Mat:
    return cv2.dilate(image_src, kernel, iterations=iterations)

def imageErosion(image_src: cv2.Mat, kernel: np.ndarray = np.ones((3, 3), np.uint8), iterations: int = 1) -> cv2.Mat:
    return cv2.erode(image_src, kernel, iterations=iterations)

def imageMorphologicalGradient(image_src: cv2.Mat) -> cv2.Mat:
    dilated = imageDilation(image_src)
    eroded = imageErosion(image_src)
    return cv2.subtract(dilated, eroded)

def imageOpening(image_src: cv2.Mat) -> cv2.Mat:
    eroded = imageErosion(image_src)
    return imageDilation(eroded)

def imageClosing(image_src: cv2.Mat) -> cv2.Mat:
    dilated = imageDilation(image_src)
    return imageErosion(dilated)

def getMorphologyKernel(flag:int = cv2.MORPH_RECT, size: int=5) -> np.ndarray:
    return cv2.getStructuringElement(flag, (size, size))

def imageMorphologyEx(image_src: cv2.Mat, operation: int, kernel: np.ndarray, iterations: int=1) -> cv2.Mat:
    return cv2.morphologyEx(image_src, operation, kernel, iterations=iterations)

def imageAffineTransform(image_src: cv2.Mat, src_points: np.ndarray, dst_points: np.ndarray, size: tuple[int, int]=None, flags: int=cv2.INTER_NEAREST) -> cv2.Mat:
    """
    Apply an affine transformation to the image using the specified source and destination points.
    """
    assert src_points.shape == (3, 2) and dst_points.shape == (3, 2), "Points must be 3x2 arrays"
    if size is None:
        size = (image_src.shape[1], image_src.shape[0])
    matrix = cv2.getAffineTransform(src_points.astype(np.float32), dst_points.astype(np.float32))
    return cv2.warpAffine(image_src, matrix, size, flags=flags)

def imagePerspectiveTransform(image_src: cv2.Mat, src_points: np.ndarray, dst_points: np.ndarray, size: tuple[int, int]=None, flags: int=cv2.INTER_NEAREST) -> cv2.Mat:
    """
    Apply a perspective transformation to the image using the specified source and destination points.
    """
    assert src_points.shape == (4, 2) and dst_points.shape == (4, 2), "Points must be 4x2 arrays"
    if size is None:
        size = (image_src.shape[1], image_src.shape[0])
    matrix = cv2.getPerspectiveTransform(src_points.astype(np.float32), dst_points.astype(np.float32))
    return cv2.warpPerspective(image_src, matrix, size, flags=flags)

def houghLines(image_src: cv2.Mat, rho: float = 1, theta: float = np.pi / 180, threshold: int = 100) -> list[tuple[int, int, int, int]]:
    lines = cv2.HoughLines(image_src, rho, theta, threshold)
    if lines is not None:
        return_lines = []
        for i in range(len(lines)):
            rho, theta = lines[i][0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            return_lines.append((x1, y1, x2, y2))
        return return_lines
    return []

def drawHoughLines(image_src: cv2.Mat, lines: list[tuple[int, int, int, int]], color: list[int, np.ndarray] = (0, 255, 0), thickness: int = 2) -> cv2.Mat:
    image_dst = imageCopy(image_src)
    for x1, y1, x2, y2 in lines:
        cv2.line(image_dst, (x1, y1), (x2, y2), color, thickness)
    return image_dst

def bar_hough_lines(image_src: cv2.Mat) -> cv2.Mat:
    window_name = "Hough Lines Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("threshold1", window_name, 100, 255, nothing)
    cv2.createTrackbar("threshold2", window_name, 200, 255, nothing)
    cv2.createTrackbar("rho", window_name, 1, 10, nothing)
    cv2.createTrackbar("theta", window_name, 1, 180, nothing)
    cv2.createTrackbar("threshold", window_name, 100, 200, nothing)
    
    while True:
        threshold1 = cv2.getTrackbarPos("threshold1", window_name)
        threshold2 = cv2.getTrackbarPos("threshold2", window_name)
        rho = cv2.getTrackbarPos("rho", window_name)
        theta = cv2.getTrackbarPos("theta", window_name) * np.pi / 180
        threshold = cv2.getTrackbarPos("threshold", window_name)

        image_canny = imageEdgeCanny(image_src, threshold1, threshold2)
        lines = houghLines(image_canny, rho=rho, theta=theta, threshold=threshold)
        image_dst = drawHoughLines(image_src, lines)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst

def houghLinesP(image_src: cv2.Mat, rho: float = 1, theta: float = np.pi / 180, threshold: int = 100, minLineLength: int = 50, maxLineGap: int = 10) -> list[tuple[int, int, int, int]]:
    lines = cv2.HoughLinesP(image_src, rho, theta, threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)
    if lines is not None:
        return [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines[:, 0]]
    return []

def drawHoughLinesP(image_src: cv2.Mat, lines: list[tuple[int, int, int, int]], color: list[int, np.ndarray] = (0, 255, 0), thickness: int = 2) -> cv2.Mat:
    image_dst = imageCopy(image_src)
    for x1, y1, x2, y2 in lines:
        cv2.line(image_dst, (x1, y1), (x2, y2), color, thickness)
    return image_dst

def bar_hough_lines_p(image_src: cv2.Mat) -> cv2.Mat:
    window_name = "Hough Lines P Trackbar"
    height, width = image_src.shape[:2]
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.createTrackbar("threshold1", window_name, 100, 255, nothing)
    cv2.createTrackbar("threshold2", window_name, 200, 255, nothing)
    cv2.createTrackbar("rho", window_name, 1, 10, nothing)
    cv2.createTrackbar("theta", window_name, 1, 180, nothing)
    cv2.createTrackbar("threshold", window_name, 100, 200, nothing)
    cv2.createTrackbar("minLineLength", window_name, 50, 200, nothing)
    cv2.createTrackbar("maxLineGap", window_name, 10, 50, nothing)
    
    while True:
        threshold1 = cv2.getTrackbarPos("threshold1", window_name)
        threshold2 = cv2.getTrackbarPos("threshold2", window_name)
        rho = cv2.getTrackbarPos("rho", window_name)
        theta = cv2.getTrackbarPos("theta", window_name) * np.pi / 180
        threshold = cv2.getTrackbarPos("threshold", window_name)
        minLineLength = cv2.getTrackbarPos("minLineLength", window_name)
        maxLineGap = cv2.getTrackbarPos("maxLineGap", window_name)
        image_canny = imageEdgeCanny(image_src, threshold1=threshold1, threshold2=threshold2)
        lines = houghLinesP(image_canny, rho=rho, theta=theta, threshold=threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)
        image_dst = drawHoughLinesP(image_src, lines)
        cv2.imshow(window_name, image_dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return image_dst