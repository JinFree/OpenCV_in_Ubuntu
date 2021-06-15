def imageProcessing(image):
    result = imageCopy(image)
    image_bgr = imageCopy(image)
    image_blur = imageBilateralFilter(image_bgr, 2, 2, 2)
    hls = convertColor(image_blur, cv2.COLOR_BGR2HLS)
    hls = imageMedianBlur(hls, 5)
    h, l, s = splitImage(hls)
    l_thresh = imageThreshold(l, 100, 255, cv2.THRESH_TOZERO)
    s_thresh = imageThreshold(s, 128, 255, cv2.THRESH_TOZERO)
    bitwise_and_image = cv2.bitwise_and(l_thresh, s_thresh)
    circles = houghCircles(bitwise_and_image, cv2.HOUGH_GRADIENT, 1, 40, 100, 15, 0, 60)
    cx = int(circles[0][0][0])
    cy = int(circles[0][0][1])
    rr = int(circles[0][0][2])
    h_value = getPixel(hls, cx, cy, 0)
    color = "None"
    color_circle = (0, 0, 255)
    if (h_value < 10 or h_value > 170):
        color = "Red"
    elif (40 < h_value and h_value < 100):
        color = "Green"
        color_circle = (0, 255, 0)
    elif (20 < h_value and h_value < 35):
        color = "Yellow"
        color_circle = (0, 255, 255)
        
    text_to_show = color + " Light"    
    result = drawCircle(result, (cx, cy), rr, color_circle, -1)
    result = drawText(result, text_to_show, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 0), 3)
    return result
