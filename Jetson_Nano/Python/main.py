import os, sys
import numpy as np
import cv2
import argparse
from utils import process

def parse_args():
    parser = argparse.ArgumentParser(description="Process images or videos using OpenCV.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input image or video file.")
    parser.add_argument("--output", type=str, default="", help="Path to save the processed output. If empty, display the result.")
    return parser.parse_args()

def main(save_path="", input_path=""):
    if (is_image(input_path)):
        process_image(save_path, input_path)
    elif (is_video(input_path)):
        process_video(save_path, input_path)
    else:
        print("Error: Unsupported file type!")
    pass

def process_image(save_path="", input_path=""):
    image_name = os.path.basename(input_path)
    image_src = cv2.imread(input_path)
    if image_src is None:
        print(f"Error: Could not read image from {input_path}")
        return
    image_dst = process(image_src, image_name)
    if save_path != "":
        cv2.imwrite(save_path, image_dst)
    else:
        height, width = image_dst.shape[:2]
        cv2.namedWindow("Processed Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Processed Image", width, height)
        cv2.imshow("Processed Image", image_dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image_dst
        
def process_video(save_path="", input_path=""):
    video_name = os.path.basename(input_path)
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if save_path != "":
        out = cv2.VideoWriter(save_path, int(cap.get(cv2.CAP_PROP_FOURCC)), int(cap.get(cv2.CAP_PROP_FPS)), (int(width), int(height)))
    else:
        cv2.namedWindow("Processed Video", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Processed Video", width, height)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_dst = process(frame, video_name)
        if save_path != "":
            out.write(frame_dst)
        else:
            cv2.imshow("Processed Video", frame_dst)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    if save_path != "":
        out.release()
    else:
        cv2.destroyAllWindows()
        
def is_image(file_path):
    return os.path.splitext(file_path)[-1] in [".jpg",".jpeg",".png",".bmp",".tiff",".tif"]

def is_video(file_path):
    return os.path.splitext(file_path)[-1] in [".mp4",".avi",".mov",".mkv",".wmv",".flv"]

if __name__ == "__main__":
    args = parse_args()
    input_path = args.input
    output_path = args.output
    main(save_path=output_path, input_path=input_path)