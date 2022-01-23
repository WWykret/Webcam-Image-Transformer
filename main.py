from ui import App
from camera import Webcam
from imageTransformers import ImageTransformer, ImageTransformerBuilder

def main():
    webcam = Webcam(default_img='loading.png', framerate=60)
    transformer = ImageTransformer()
    application = App('camera converter', webcam, transformer)

if __name__ == '__main__':
    main()
