def imageProcessing(image):
    result = imageCopy(image)
    hls = convertColor(result, cv2.COLOR_BGR2HLS)
    lower = np.array([0, 128, 200])
    upper = np.array([180, 255, 255])
    splitted = splitColor(hls, lower, upper)
    splitted_bgr = convertColor(splitted, cv2.COLOR_HLS2BGR)
    result = convertColor(splitted_bgr, cv2.COLOR_BGR2GRAY)
    result = imageThreshold(result, 10, 255, cv2.THRESH_BINARY)
    MORPH_ELLIPSE = imageMorphologyKernel(cv2.MORPH_ELLIPSE, 5)
    result = imageMorphologyEx(result, cv2.MORPH_CLOSE, MORPH_ELLIPSE)
    circles = houghCircles(result, cv2.HOUGH_GRADIENT, 1, 31, 23, 13, 20, 0)
    result = imageCopy(image)
    value_list = []
    for i in circles[0,:]:
        center_x = int(i[0])
        center_y = int(i[1])
        cv2.circle(result, (i[0],i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(result, (i[0],i[1]), 2, (0, 0, 255), -1)
        hls_value = getPixel(hls, center_x, center_y)
        value_list.append([hls_value])
    h_value = None
    if(len(value_list) == 1):
        h_value = value_list[0][0][0][0]
    else:
        h_value_list = []
        hl_value_list = []
        for i in range(len(value_list)):
            h_value_list.append([value_list[i][0][0][0]])
            hl_value_list.append([value_list[i][0][0][1], value_list[i][0][0][0]])
        hl_value_list.sort(key=lambda x:x[0])
        h_value = hl_value_list[len(hl_value_list)-1][1]
    #print(h_value)
    color = None
    if(h_value < 10 or h_value > 170):
        color = "Red"
    elif(20 < h_value and h_value < 35):
        color = "Yellow"
    elif(60 < h_value and h_value < 90):
        color = "Green"
    text_string = color + " Light"
    result = drawText(result, text_string, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
    return result
