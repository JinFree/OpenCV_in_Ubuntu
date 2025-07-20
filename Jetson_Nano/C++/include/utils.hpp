#ifndef UTILS_HPP
#define UTILS_HPP

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <set>

#include <opencv2/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

#define PI 3.1415926

using namespace std;
void copy_image(cv::Mat& dst_image, const cv::Mat& src_image);
void process(cv::Mat& dst_image, const cv::Mat& src_image);

#endif // UTILS_HPP