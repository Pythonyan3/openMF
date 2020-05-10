from app.openMF.Shapes.Shape import Shape
from app.openMF.Shapes import Cylinder, Box, TruncatedPyramid
from typing import List


class MFObject(Shape):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        self.shapes: List[Shape] = list()
        self.shapes.append(Box.Box(0, 0, 0, 150, 4, 60))
        self.shapes.append(Box.Box(-40, 4, 0, 50, 4, 40))
        self.shapes.append(Box.Box(40, 4, 0, 50, 4, 40))
        self.shapes.append(Box.Box(0, 3, 0, 30, 2, 40))
        self.shapes.append(Box.Box(0, 5, 0, 30, 2, 34))
        self.shapes.append(TruncatedPyramid.TruncatedPyramid(-45, 31, 0, 30, 20, 50))
        self.shapes.append(TruncatedPyramid.TruncatedPyramid(45, 31, 0, 30, 20, 50))
        self.shapes.append(Box.Box(-45, 57, 0, 30, 2, 30))
        self.shapes.append(Box.Box(-45, 59, 0, 20, 2, 20))
        self.shapes.append(Box.Box(45, 57, 0, 30, 2, 30))
        self.shapes.append(Box.Box(45, 59, 0, 20, 2, 20))
        #self.shapes.append(Cylinder.Cylinder(-12, 21, 6, 3, 30))
        #self.shapes.append(Cylinder.Cylinder(-12, 21, -6, 3, 30))
        #self.shapes.append(Cylinder.Cylinder(12, 21, 6, 3, 30))
        #self.shapes.append(Cylinder.Cylinder(12, 21, -6, 3, 30))
        self.shapes.append(Box.Box(0, 39, 0, 66, 5, 20))

    def append(self, object: Shape):
        if not isinstance(object, MFObject):
            self.shapes.append(object)
        else:
            self.shapes += object.shapes

    def triangles(self):
        result = list()
        for shape in self.shapes:
            result += shape.triangles()
