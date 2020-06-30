LIBS = -lopencv_stitching -lopencv_superres -lopencv_videostab -lopencv_aruco -lopencv_bgsegm -lopencv_bioinspired -lopencv_ccalib -lopencv_dpm -lopencv_face -lopencv_photo -lopencv_fuzzy -lopencv_img_hash -lopencv_line_descriptor -lopencv_optflow -lopencv_reg -lopencv_rgbd -lopencv_saliency -lopencv_stereo -lopencv_structured_light -lopencv_phase_unwrapping -lopencv_surface_matching -lopencv_tracking -lopencv_datasets -lopencv_text -lopencv_dnn -lopencv_plot -lopencv_xfeatures2d -lopencv_shape -lopencv_video -lopencv_ml -lopencv_ximgproc -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_flann -lopencv_xobjdetect -lopencv_imgcodecs -lopencv_objdetect -lopencv_xphoto -lopencv_imgproc -lopencv_core
INC = -L/usr/local/lib -I/usr/local/include/opencv -I/usr/local/include

all : 
	make a.out

a.out: main.o utils.o functions.o
	g++ -o a.out main.o utils.o functions.o $(LIBS) $(INC)

main.o: utils.o functions.o OpenCV_Main.cpp
	g++ -c -o main.o OpenCV_Main.cpp $(LIBS) $(INC)

utils.o: OpenCV_Utils.h OpenCV_Utils.cpp
	g++ -c -o utils.o OpenCV_Utils.cpp $(LIBS) $(INC)

functions.o: OpenCV_Functions.h OpenCV_Functions.cpp
	g++ -c -o functions.o OpenCV_Functions.cpp $(LIBS) $(INC)

clean_image:
	rm *.jpg

clean_video:
	rm *.mp4

clean:
	rm -rf a.out
	rm -rf *.o
