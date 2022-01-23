from transformations import *

class IImageTransformer:
    def transform_image(self, image: Image) -> Image:
        pass

    def add_transformation(self, transformation: Transformation):
        pass

class ImageTransformer(IImageTransformer):
    def __init__(self):
        self.transformations = [IdentityTransformation()]

    def add_transformation(self, transformation: Transformation):
        self.transformations.append(transformation)

    def tansform_image(self, image: Image):
        for index, transformation in enumerate(self.transformations):
            if index + 1 < len(self.transformations):
                transformation.set_next(self.transformations[index + 1])

        return self.transformations[0].transform_image(image)


class ImageTransformerBuilder:
    def __init__(self):
        self.image_transformer = ImageTransformer()

    def negate_image(self):
        self.image_transformer.add_transformation(NegateTransformation())
        return self

    def detect_edges(self):
        self.image_transformer.add_transformation(EdgeDetectionTransformation())
        return self

    def flip_on_axis(self, axis: str):
        self.image_transformer.add_transformation(FlipTransformation(axis))
        return self

    def flip_on_middle(self):
        self.flip_on_axis('x')
        self.flip_on_axis('y')
        return self

    def build(self):
        return self.image_transformer