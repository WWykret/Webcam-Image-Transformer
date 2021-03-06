import cv2
from PIL import Image
from imageTransformers import IImageTransformer

class Camera:
    def get_camera_frame(self, transformer: IImageTransformer):
        pass

    def get_default_img(self, transformer: IImageTransformer):
        pass

    def get_framerate(self):
        pass

class Webcam(Camera):
    def __init__(self, default_img: str, framerate: int):
        self.vc = cv2.VideoCapture(0)
        self.framerate = framerate
        self.default_img = default_img

    def get_camera_frame(self, transformer: IImageTransformer):
        if self.vc.isOpened():
            _, frame = self.vc.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_frame = Image.fromarray(frame)
        else:
            cam_frame = Image.open('loading.png')

        return transformer.tansform_image(cam_frame)

    def get_default_img(self, transformer: IImageTransformer):
        return transformer.tansform_image(Image.open(self.default_img))

    def get_framerate(self):
        return self.framerate