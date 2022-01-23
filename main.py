from ui import App
from camera import Webcam

def main():
    webcam = Webcam(default_img='loading.png', framerate=60)
    application = App('camera converter', webcam)

if __name__ == '__main__':
    main()
