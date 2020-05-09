from app.GObjects.Shapes import Shape
from typing import List


class MFObject(Shape):
    def __init__(self):
        super().__init__()
        self.shapes: List[Shape] = list()
