#include <utils.hpp>

void process(cv::Mat& dst_image, const cv::Mat& src_image)
{
    // Basic process function that copies the source image to the destination image
    copy_image(dst_image, src_image);
}

void copy_image(cv::Mat& dst_image, const cv::Mat& src_image)
{
    if (src_image.empty()) {
        cerr << "Error: Source image is empty!" << endl;
        return;
    }
    dst_image = src_image.clone();
}