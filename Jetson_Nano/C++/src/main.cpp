#include <main.hpp>

int main(int argc, char** argv)
{
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <image_path or video_path> <save_path>" << endl;
        return -1;
    }
    string input_path = argv[1];
    string save_path = (argc > 2) ? argv[2] : "";
    cout << "Input Path: " << input_path << endl;
    cout << "Save Path: " << save_path << endl;
    if (is_image(input_path)) {
        cout << "Processing image: " << input_path << endl;
        process_image(save_path, input_path);
    } 
    else if (is_video(input_path)) {
        cout << "Processing Video: " << input_path << endl;
        process_video(save_path, input_path);
    } 
    else {
        cout << "Error: Unsupported file type!" << endl;
    }
    return 0;
}

void process_image(const std::string& save_path, const std::string& input_path)
{
    cv::Mat src_image = cv::imread(input_path);
    if (src_image.empty()) {
        cerr << "Error: Could not open or find the image!" << endl;
        return;
    }
    
    cv::Mat dst_image;
    process(dst_image, src_image);
    
    if (!save_path.empty()) {
        cv::imwrite(save_path, dst_image);
        cout << "Image saved to: " << save_path << endl;
    } 
    else {
        cout << "Processed image displayed." << endl;
        cv::namedWindow("Processed Image", cv::WINDOW_NORMAL);
        cv::imshow("Processed Image", dst_image);
        cv::waitKey(0);
    }
}

void process_video(const std::string& save_path, const std::string& input_path)
{
    cv::VideoCapture cap(input_path);
    if (!cap.isOpened()) {
        cerr << "Error: Could not open or find the video!" << endl;
        return;
    }

    cv::VideoWriter writer;
    if (!save_path.empty()) {
        writer.open(save_path, cap.get(cv::CAP_PROP_FOURCC), cap.get(cv::CAP_PROP_FPS), 
                    cv::Size((int)cap.get(cv::CAP_PROP_FRAME_WIDTH), (int)cap.get(cv::CAP_PROP_FRAME_HEIGHT)));
        if (!writer.isOpened()) {
            cerr << "Error: Could not open the video writer!" << endl;
            return;
        }
    }

    cv::Mat frame, processed_frame;
    
    cv::namedWindow("Processed Video", cv::WINDOW_NORMAL);
    while (cap.read(frame)) {
        process(processed_frame, frame);
        if (!save_path.empty()) {
            writer.write(processed_frame);
        } 
        else {
            cv::imshow("Processed Video", processed_frame);
            char c = (char)cv::waitKey(1);
            if (c==27)
                break;
        }
    }

    cap.release();
    if (writer.isOpened()) {
        writer.release();
    }
    cv::destroyAllWindows();
}

bool is_image(const string& path) {
    static const set<string> exts = {
        ".jpg",".jpeg",".png",".bmp",".tiff",".tif"
    };
    auto ext = fs::path(path).extension().string();
    transform(ext.begin(), ext.end(), ext.begin(), ::tolower);
    return exts.count(ext) > 0;
}

bool is_video(const string& path) {
    static const set<string> exts = {
        ".mp4",".avi",".mov",".mkv",".wmv",".flv"
    };
    auto ext = fs::path(path).extension().string();
    transform(ext.begin(), ext.end(), ext.begin(), ::tolower);
    return exts.count(ext) > 0;
}