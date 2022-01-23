import cv2
from PIL import Image

class Webcam:
    def __init__(self, default_img: str, framerate: int):
        self.vc = cv2.VideoCapture(0)
        self.framerate = framerate
        self.default_img = default_img

    def get_camera_frame(self):
        if self.vc.isOpened():
            _, frame = self.vc.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_frame = Image.fromarray(frame)
        else:
            cam_frame = Image.open('loading.png')
        return cam_frame

    def get_default_img(self):
        return Image.open(self.default_img)