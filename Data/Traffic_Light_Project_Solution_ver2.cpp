void imageProcessing(Mat &image, Mat &result)
{
    result = imageCopy(image);
    Mat image_bgr, image_blur, gray, hls, h, l, s, l_thresh, s_thresh, bitwise_and_image, threshold, blured_hls;
    int pxvalue_l, x_coord, y_coord, radius;
    vector<Vec3f> circles;
    image_bgr = imageCopy(image);
    imageMedianBlur(image_bgr, image_blur, 10);
    convertColor(result, gray, COLOR_BGR2GRAY);
    convertColor(image_blur, hls, COLOR_BGR2HLS);
    vector<Mat> hls_channels;
    splitImage(hls, hls_channels);
    h = hls_channels[0];
    l = hls_channels[1];
    s = hls_channels[2];
    imageThreshold(l, l_thresh, 100, 255, THRESH_TOZERO);
    imageThreshold(s, s_thresh, 120, 255, THRESH_TOZERO);
    bitwise_and(l_thresh, s_thresh, bitwise_and_image);
    imageThreshold(bitwise_and_image, threshold, 50, 255, THRESH_BINARY);
    imageHoughCircles(threshold, circles, HOUGH_GRADIENT, 1, 40, 100, 15, 0, 100);
    pxvalue_l = 0;
    for ( int i = 0 ; i < circles.size() ; i++ )
    {
        int x = circles[i][0];
        int y = circles[i][1];
        int pxvalue_l_new = getPixel(l, x, y);
        if ( pxvalue_l_new > pxvalue_l )
        {
            pxvalue_l = pxvalue_l_new;
            x_coord = x;
            y_coord = y;
            radius = circles[i][2];
        }
    }
    convertColor(image_blur, blured_hls, COLOR_BGR2HLS);
    int pxvalue_h = getPixel(blured_hls, x_coord, y_coord, 0);   
    int pxvalue_b = getPixel(image_blur, x_coord, y_coord, 0); 
    int pxvalue_g = getPixel(image_blur, x_coord, y_coord, 1); 
    int pxvalue_r = getPixel(image_blur, x_coord, y_coord, 2);
    drawCircle(image_bgr, result, Point(x_coord, y_coord), radius,  Scalar(pxvalue_b, pxvalue_g, pxvalue_r), -1);
    
    string color, LightColor;
    if(pxvalue_h < 10 || pxvalue_h > 170)
        color = "Red";
    else if(18 < pxvalue_h && pxvalue_h < 35)
        color = "Yellow";
    else if(60 < pxvalue_h && pxvalue_h < 90)
        color = "Green";
    LightColor = color + "Light";
    drawText(result, result, LightColor, Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, Scalar(255, 0, 0), 3);
    return;
}

/*
void imageProcessing(Mat &image, Mat &result)
{
    Mat image_bgr, image_blur, gray, hls, h, l, s, l_thresh, s_thresh, bitwise_and_image, threshold, blured_hls;
    int pxvalue_l, x_coord, y_coord, radius;
    vector<Vec3f> circles;
    vector<Mat> hls_channels;
    result = imageCopy(image);
    //image_bgr = imageCopy(image)
    image_bgr = imageCopy(image);
    //image_blur = imageMedianBlur(image_bgr, 10)
    imageMedianBlur(image_bgr, image_blur, 10);
    //gray = convertColor(result, cv2.COLOR_BGR2GRAY)
    convertColor(result, gray, COLOR_BGR2GRAY);
    //hls = convertColor(image_blur, cv2.COLOR_BGR2HLS)
    convertColor(image_blur, hls, COLOR_BGR2HLS);
    //h, l, s = splitImage(hls)
    splitImage(hls, hls_channels);
    h = hls_channels[0];
    l = hls_channels[1];
    s = hls_channels[2];
    //l_thresh = imageThreshold(l, 100, 255, cv2.THRESH_TOZERO)
    imageThreshold(l, l_thresh, 100, 255, THRESH_TOZERO);
    //s_thresh = imageThreshold(s, 120, 255, cv2.THRESH_TOZERO)
    imageThreshold(s, s_thresh, 120, 255, THRESH_TOZERO);
    //bitwise_and_image = cv2.bitwise_and(l_thresh, s_thresh)
    bitwise_and(l_thresh, s_thresh, bitwise_and_image);
    //threshold = imageThreshold(bitwise_and_image, 50, 255, cv2.THRESH_BINARY)
    imageThreshold(bitwise_and_image, threshold, 50, 255, THRESH_BINARY);
    //circles = houghCircles(threshold, cv2.HOUGH_GRADIENT, 1, 40, 100, 15, 0, 100)
    imageHoughCircles(threshold, circles, HOUGH_GRADIENT, 1, 40, 100, 15, 0, 100);
    
    //pxvalue_h = 0
    //pxvalue_l = 0
    //x_coord = 0
    //y_coord = 0
    //radius = 0
    //for i in circles[0,:]:
    //    x = int(i[0])
    //    y = int(i[1])
    //    pxvalue_l_new = getPixel(l, x, y)
    //    if pxvalue_l_new > pxvalue_l:
    //        pxvalue_l = pxvalue_l_new
    //        x_coord = x
    //        y_coord = y
    //        radius = i[2]
    
    pxvalue_l = 0;
    for ( int i = 0 ; i < circles.size() ; i++ )
    {
        int x = circles[i][0];
        int y = circles[i][1];
        int pxvalue_l_new = getPixel(l, x, y);
        if ( pxvalue_l_new > pxvalue_l )
        {
            pxvalue_l = pxvalue_l_new;
            x_coord = x;
            y_coord = y;
            radius = circles[i][2];
        }
    }
    //blured_hls = convertColor(image_blur, cv2.COLOR_BGR2HLS)
    convertColor(image_blur, blured_hls, COLOR_BGR2HLS);
    //pxvalue_h = getPixel(blured_hls, x_coord, y_coord, 0)  
    int pxvalue_h = getPixel(blured_hls, x_coord, y_coord, 0);   
    //pxvalue_b = getPixel(image_blur, x_coord, y_coord, 0)  
    int pxvalue_b = getPixel(image_blur, x_coord, y_coord, 0); 
    //pxvalue_g = getPixel(image_blur, x_coord, y_coord, 1) 
    int pxvalue_g = getPixel(image_blur, x_coord, y_coord, 1); 
    //pxvalue_r = getPixel(image_blur, x_coord, y_coord, 2)
    int pxvalue_r = getPixel(image_blur, x_coord, y_coord, 2);
    //result = cv2.circle(image_bgr, (x_coord, y_coord), radius, (int(pxvalue_b), int(pxvalue_g), int(pxvalue_r)), -1)
    drawCircle(image_bgr, result, Point(x_coord, y_coord), radius,  Scalar(pxvalue_b, pxvalue_g, pxvalue_r), -1);
    //color = None
    string color, LightColor;
    
    //if(pxvalue_h < 10 or pxvalue_h > 170):
    //    color = "Red"
    //elif(18 < pxvalue_h and pxvalue_h < 35):
    //    color = "Yellow"
    //elif(60 < pxvalue_h and pxvalue_h < 90):
    //    color = "Green"
    
    if(pxvalue_h < 10 || pxvalue_h > 170)
        color = "Red";
    else if(18 < pxvalue_h && pxvalue_h < 35)
        color = "Yellow";
    else if(60 < pxvalue_h && pxvalue_h < 90)
        color = "Green";
    //LightColor = color + "Light"
    LightColor = color + "Light";
    //result = drawText(result, LightColor, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 0, 0), 3)
    drawText(result, result, LightColor, Point(10, 50), FONT_HERSHEY_PLAIN, 2.5, Scalar(255, 0, 0), 3);
    return;
}
*/
