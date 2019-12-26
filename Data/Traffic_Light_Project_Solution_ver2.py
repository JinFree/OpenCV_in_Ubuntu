def imageProcessing(image):
    result = imageCopy(image)
    image_bgr = imageCopy(image)
    image_blur = imageMedianBlur(image_bgr, 10)
    gray = convertColor(result, cv2.COLOR_BGR2GRAY)
    hls = convertColor(result, cv2.COLOR_BGR2HLS)
    h, l, s = splitImage(hls)
    l_thresh = imageThreshold(l, 100, 255, cv2.THRESH_TOZERO)
    s_thresh = imageThreshold(s, 120, 255, cv2.THRESH_TOZERO)
    bitwise_and_image = cv2.bitwise_and(l_thresh, s_thresh)
    threshold = imageThreshold(bitwise_and_image, 50, 255, cv2.THRESH_BINARY)
    circles = houghCircles(threshold, cv2.HOUGH_GRADIENT, 1, 40, 100, 15, 0, 100)
    pxvalue_h = 0
    pxvalue_l = 0
    x_coord = 0
    y_coord = 0
    radius = 0
    for i in circles[0,:]:
        x = int(i[0])
        y = int(i[1])
        cv2.circle(result, (x, y), i[2], (0, 255, 0), 2)
        cv2.circle(result, (x, y), 2, (0, 0, 255), -1)
        pxvalue_l_new = getPixel(l, x, y)
        if pxvalue_l_new > pxvalue_l:
            pxvalue_l = pxvalue_l_new
            x_coord = x
            y_coord = y
            radius = i[2]
    blured_hls = convertColor(image_blur, cv2.COLOR_BGR2HLS)
    pxvalue_h = getPixel(blured_hls, x_coord, y_coord, 0)   
    pxvalue_b = getPixel(image_blur, x_coord, y_coord, 0) 
    pxvalue_g = getPixel(image_blur, x_coord, y_coord, 1) 
    pxvalue_r = getPixel(image_blur, x_coord, y_coord, 2)
    print(pxvalue_h)
    result = cv2.circle(image_bgr, (x_coord, y_coord), radius, (int(pxvalue_b), int(pxvalue_g), int(pxvalue_r)), -1)
    color = None
    if(pxvalue_h < 10 or pxvalue_h > 170):
        color = "Red"
    elif(18 < pxvalue_h and pxvalue_h < 35):
        color = "Yellow"
    elif(60 < pxvalue_h and pxvalue_h < 90):
        color = "Green"
    LightColor = color + "Light"
    result = drawText(result, LightColor, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
    return result
