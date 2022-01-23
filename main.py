from ui import App
from camera import Webcam
from imageTransformers import ImageTransformer, ImageTransformerBuilder
from imageSavers import FileImageSaver

def main():
    webcam = Webcam(default_img='loading.png', framerate=60)
    transformer = ImageTransformer()
    image_saver = FileImageSaver()
    application = App('camera converter', webcam, transformer, image_saver)

if __name__ == '__main__':
    main()
