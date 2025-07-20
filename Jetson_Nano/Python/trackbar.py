import argparse
from opencv_functions import bar_RGB, bar_HLS, bar_HSV

def parse_args():
    parser = argparse.ArgumentParser(description="Trackbar example for adjusting RGB values.")
    parser.add_argument("--mode", type=str, default="rgb", help="[rgb, hsv, hls]")
    parser.add_argument("--size", type=int, default=100, help="Size of the trackbar window.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    args.mode = args.mode.lower()
    if args.mode == "rgb":
        bar_RGB(args.size)
    elif args.mode == "hls":
        bar_HLS(args.size)
    elif args.mode == "hsv":
        bar_HSV(args.size)
    else:
        print(f"Mode {args.mode} is not supported yet.")