from PIL import Image

class Transformation():
    def __init__(self):
        self.next = None

    def set_next(self, next: Transformation):
        pass

    def transform_image(self, image: Image):
        pass

class FlipTransformation(Transformation):
    def __init__(self, flip_axis: str):
        pass

class NegateTransformation(Transformation):
    pass

class EdgeDetectionTransformation(Transformation):
    pass

class IdentityTransformation(Transformation):
    pass