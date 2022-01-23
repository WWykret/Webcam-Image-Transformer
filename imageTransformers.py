from transformations import *

class ImageTransformer:
    def __init__(self):
        self.transformations = [IdentityTransformation()]

class ImageTransformerBuilder:
    def __init__(self):
        self.image_transformer = ImageTransformer()

    def negate_image(self):
        self.image_transformer.transformations.append(NegateTransformation())

    def detect_edges(self):
        self.image_transformer.transformations.append(EdgeDetectionTransformation())

    def flip_image(self, axis: str):
        self.image_transformer.transformations.append(FlipTransformation(axis))

    def build(self):
        return self.image_transformer