from PIL import Image
import os.path

class IImageSaver:
    def save_image(self, path: str, img: Image) -> bool:
        pass

class FileImageSaver(IImageSaver):
    def save_image(self, path: str, img: Image) -> bool:
        dir = os.path.dirname(path)
        
        if not os.path.isdir(dir):
            os.makedirs(dir)

        success = False
        try:
            if not os.path.isfile(path):
                img.save(path)
                success = True
        except IOError:
            print (f'could not save file at {path}')

        return success