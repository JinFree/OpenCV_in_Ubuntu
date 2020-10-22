#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install build-essential cmake unzip -y
sudo apt install libjpeg-dev libtiff5-dev libpng-dev -y
sudo apt install ffmpeg libavcodec-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev -y
sudo apt install libv4l-dev v4l-utils -y
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev -y
sudo apt install libgtk-3-dev -y
sudo apt install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev -y
sudo apt install libatlas-base-dev gfortran libeigen3-dev -y
sudo apt install python3-pip python-pip python3-numpy python-numpy -y

cd
mkdir opencv 
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.4.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.4.0.zip
unzip opencv_contrib.zip
rm opencv.zip
rm opencv_contrib.zip
cd opencv-4.4.0
mkdir build
cd build
cmake  -D CMAKE_BUILD_TYPE=RELEASE  -D CMAKE_INSTALL_PREFIX=/usr/local  -D WITH_TBB=OFF  -D WITH_IPP=OFF  -D WITH_1394=OFF  -D BUILD_WITH_DEBUG_INFO=OFF  -D BUILD_DOCS=OFF  -D INSTALL_C_EXAMPLES=ON  -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=OFF  -D BUILD_PACKAGE=OFF  -D BUILD_TESTS=OFF  -D BUILD_PERF_TESTS=OFF  -D WITH_QT=OFF  -D WITH_GTK=ON  -D WITH_OPENGL=ON  -D BUILD_opencv_python3=ON  -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.4.0/modules -D WITH_V4L=ON  -D WITH_FFMPEG=ON  -D WITH_XINE=ON  -D OPENCV_ENABLE_NONFREE=ON  -D BUILD_NEW_PYTHON_SUPPORT=ON  -D OPENCV_SKIP_PYTHON_LOADER=ON  -D OPENCV_GENERATE_PKGCONFIG=ON  ../
make -j$(nproc)
sudo make install 
sudo ldconfig
