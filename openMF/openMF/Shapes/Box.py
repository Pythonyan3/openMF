from openMF.openMF.Shapes.Point import Point
from openMF.openMF.Shapes.Shape import Shape
from openMF.openMF.Shapes.Triangle import Triangle


class Box(Shape):
    def __init__(self, x: float, y: float, z: float, width: int, height: int, length: int):
        super().__init__(x, y, z)
        self.length = length
        self.width = width
        self.height = height

    def get_params(self):
        return 'Box_params: ' + str(self.width) + ' ' + str(self.height) + ' ' + str(self.length) + '\n'

    def triangles(self):
        triangles = list()
        half_w, half_h, half_l = self.width / 2, self.height / 2, self.length / 2
        x0, y0, z0 = - half_w, - half_h, - half_l
        x1, y1, z1 = half_w, half_h, half_l
        """Front Face"""
        triangles.append(Triangle(Point(x0, y0, z0), Point(x1, y1, z0), Point(x0, y1, z0)))
        triangles.append(Triangle(Point(x0, y0, z0), Point(x1, y1, z0), Point(x1, y0, z0)))
        """Left Face"""
        triangles.append(Triangle(Point(x0, y0, z0), Point(x0, y1, z1), Point(x0, y1, z0)))
        triangles.append(Triangle(Point(x0, y0, z0), Point(x0, y1, z1), Point(x0, y0, z1)))
        """Bottom Face"""
        triangles.append(Triangle(Point(x0, y0, z0), Point(x1, y0, z1), Point(x1, y0, z0)))
        triangles.append(Triangle(Point(x0, y0, z0), Point(x1, y0, z1), Point(x0, y0, z1)))
        """Back Face"""
        triangles.append(Triangle(Point(x1, y1, z1), Point(x0, y0, z1), Point(x0, y1, z1)))
        triangles.append(Triangle(Point(x1, y1, z1), Point(x0, y0, z1), Point(x1, y0, z1)))
        """Right Face"""
        triangles.append(Triangle(Point(x1, y1, z1), Point(x1, y0, z0), Point(x1, y1, z0)))
        triangles.append(Triangle(Point(x1, y1, z1), Point(x1, y0, z0), Point(x1, y0, z1)))
        """Top Face"""
        triangles.append(Triangle(Point(x1, y1, z1), Point(x0, y1, z0), Point(x0, y1, z1)))
        triangles.append(Triangle(Point(x1, y1, z1), Point(x0, y1, z0), Point(x1, y1, z0)))
        return triangles
