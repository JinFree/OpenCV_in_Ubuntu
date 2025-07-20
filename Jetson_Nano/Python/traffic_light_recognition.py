import cv2
import os
from main import process_image
script_path = os.path.dirname(__file__)

TS_IMAGES_ROOT = "../../Data/TrafficLight_Detection"
IMAGES=["green_light_02.png",
        "red_light_02.png",
        "yellow_light_02.png"]

for image in IMAGES:
    input_path = os.path.join(script_path, TS_IMAGES_ROOT, image)
    save_path = os.path.join(script_path, "TrafficSign", image)
    image_dst = process_image("", input_path)
    cv2.imwrite(save_path, image_dst)