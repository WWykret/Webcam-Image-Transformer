from PIL import Image, ImageOps, ImageFilter

class Transformation:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def transform_image(self, image: Image):
        pass

class FlipTransformation(Transformation):
    def __init__(self, flip_axis: str):
        super().__init__()
        self.flip_axis = flip_axis

    def transform_image(self, image: Image):
        if self.flip_axis in ['x', 'X']:
            image = ImageOps.flip(image)
        elif self.flip_axis in ['y', 'Y']:
            image = ImageOps.mirror(image)

        if self.next is None:
            return image
        
        return self.next.transform_image(image)

class NegateTransformation(Transformation):
    def __init__(self):
        super().__init__()

    def transform_image(self, image: Image):
        image = ImageOps.invert(image.convert('RGB'))

        if self.next is None:
            return image
        
        return self.next.transform_image(image)

class EdgeDetectionTransformation(Transformation):
    def __init__(self):
        super().__init__()

    def transform_image(self, image: Image):
        image = image.convert('L') # convert to grayscale
        image = image.filter(ImageFilter.FIND_EDGES)

        if self.next is None:
            return image
        
        return self.next.transform_image(image)

class IdentityTransformation(Transformation):
    def __init__(self):
        super().__init__()

    def transform_image(self, image: Image):
        if self.next is None:
            return image
        
        return self.next.transform_image(image)