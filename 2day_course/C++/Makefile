LIBS = -L/usr/local/LIBS
LIBS += `pkg-config --libs opencv4 2> /dev/null || pkg-config --libs opencv`
INC = -I/usr/local/include 
INC +=  `pkg-config --cflags opencv4 2> /dev/null || pkg-config --cflags opencv`

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
