def imageProcessing(image):
    result = imageCopy(image)
    height, width = image.shape[0], image.shape[1]
    
    hsv = convertColor(result, cv2.COLOR_BGR2HSV)
    h, s, v = splitImage(hsv)
    s_eq = histogramEqualize(s)
    hsv2 = mergeImage(h, s_eq, v)
    
    red_1_lower = np.array([0, 100, 120])
    red_1_upper = np.array([7, 255, 255])
    red_2_lower = np.array([170, 100, 120])
    red_2_upper = np.array([180, 255, 255])
    red_1 = rangeColor(hsv2, red_1_lower, red_1_upper)
    red_2 = rangeColor(hsv2, red_2_lower, red_2_upper)
    red = red_1 + red_2
    
    green_lower = np.array([35, 100, 120])
    green_upper = np.array([90, 255, 255])
    green = rangeColor(hsv2, green_lower, green_upper)
    
    
    yellow_lower = np.array([17, 100, 120])
    yellow_upper = np.array([33, 255, 255])
    yellow = rangeColor(hsv2, yellow_lower, yellow_upper)
    #imageShow("red", red)
    red_point_list = []
    green_point_list = []
    yellow_point_list = []
    if(width < height):
        x = int(0.5*width)
        for y in range(height):
            pixel_red = getPixel(red, x, y)
            pixel_yellow = getPixel(yellow, x, y)
            pixel_green = getPixel(green, x, y)
            if(pixel_red == 255):
                if(len(red_point_list) == 0):
                    red_point_list.append([x, y])

            if(pixel_yellow == 255):
                if(len(yellow_point_list) == 0):
                    yellow_point_list.append([x, y])

            if(pixel_green == 255):
                if(len(green_point_list) == 0):                    green_point_list.append([x, y])

        for y in range(height-1, 0, -1):
            pixel_red = getPixel(red, x, y)
            pixel_yellow = getPixel(yellow, x, y)
            pixel_green = getPixel(green, x, y)
            if(pixel_red == 255):
                if(len(red_point_list) == 1):
                    red_point_list.append([x, y])

            if(pixel_yellow == 255):
                if(len(yellow_point_list) == 1):
                    yellow_point_list.append([x, y])

            if(pixel_green == 255):
                if(len(green_point_list) == 1):
                    green_point_list.append([x, y])
    else:
        y = int(0.5*height)
        for x in range(width):
            pixel_red = getPixel(red, x, y)
            pixel_yellow = getPixel(yellow, x, y)
            pixel_green = getPixel(green, x, y)
            if(pixel_red == 255):
                if(len(red_point_list) == 0):
                    red_point_list.append([x, y])

            if(pixel_yellow == 255):
                if(len(yellow_point_list) == 0):
                    yellow_point_list.append([x, y])

            if(pixel_green == 255):
                if(len(green_point_list) == 0):
                    green_point_list.append([x, y])

        for x in range(width-1, 0, -1):
            pixel_red = getPixel(red, x, y)
            pixel_yellow = getPixel(yellow, x, y)
            pixel_green = getPixel(green, x, y)
            if(pixel_red == 255):
                if(len(red_point_list) == 1):
                    red_point_list.append([x, y])

            if(pixel_yellow == 255):
                if(len(yellow_point_list) == 1):
                    yellow_point_list.append([x, y])

            if(pixel_green == 255):
                if(len(green_point_list) == 1):
                    green_point_list.append([x, y])
    hls = convertColor(image, cv2.COLOR_BGR2HLS)
    _, l, _ = splitImage(hls)
    value_list = []    
    
    if(len(red_point_list) == 2):
        if width < height:
            if (red_point_list[1][1] - red_point_list[0][1]) < (0.7*width):
                value_list.append(["red", getPixel(l, red_point_list[0][0], red_point_list[0][1])])
    if(len(green_point_list) == 2):
        if width < height:
            if (green_point_list[1][1] - green_point_list[0][1]) < (0.7*width):
                value_list.append(["green", getPixel(l, green_point_list[0][0], green_point_list[0][1])])
    if(len(yellow_point_list) == 2):
        if width < height:
            if (yellow_point_list[1][1] - yellow_point_list[0][1]) < (0.7*width):
                value_list.append(["yellow", getPixel(l, yellow_point_list[0][0], yellow_point_list[0][1])])
    if len(value_list) == 0:
        print("nothing")
        return result
    #print("value_list", value_list)
    lightness_idx = 0
    lightness = 0
    for idx in range(len(value_list)):
        if value_list[idx][1] > lightness:
            lightness = value_list[idx][1]
            lightness_idx = idx
    result = drawText(image, "{} light".format(value_list[lightness_idx][0]), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
    return result
