#include "OpenCV_Utils.h"
#include "OpenCV_Functions.h"

Mat imageRead(string openPath, int flag)
{
	Mat image = imread(openPath, flag);
	if(image.empty()) {
		cout<<"Image Not Opened"<<endl;
		cout<<"Program Abort"<<endl;
		exit(1);
	}
	else {
		cout<<"Image Opened"<<endl;
		return image;
	}
}
void imageShow(string imageName, Mat &image, int flag)
{
	namedWindow(imageName, flag);
    imshow(imageName, image);
	waitKey();
	return;
}
void imageWrite(string imageName, Mat &image)
{
    imwrite(imageName, image);
    return;
}
Mat imageCopy(Mat &image)
{
    Mat result;
    image.copyTo(result);
    return result;
}
void Video(string openPath, string savePath)
{
    VideoCapture cap(openPath);
    if(cap.isOpened())
    {
        cout << "Video Opened" << endl;
    }
    else
    {
        cout << "Video Not Opened" << endl;
        cout << "Program Abort" << endl;
        exit(-1);
    }
    int fps = cap.get(CAP_PROP_FPS);
    int width = cap.get(CAP_PROP_FRAME_WIDTH);
    int height = cap.get(CAP_PROP_FRAME_HEIGHT);
    int fourcc = cap.get(CAP_PROP_FOURCC);
    VideoWriter out(savePath.c_str(), fourcc, fps, Size(width, height), true);
    namedWindow("Input", WINDOW_GUI_EXPANDED);
    namedWindow("Output", WINDOW_GUI_EXPANDED);
    Mat frame, output;
    while(cap.read(frame))
    {
        imageProcessing(frame, output);
        out.write(output);
        imshow("Input", frame);
        imshow("Output", output);
        char c = (char)waitKey(int(1000.0/fps));
        if (c==27)
            break;
    }
    cap.release();
    out.release();
    destroyAllWindows();
    return;
}