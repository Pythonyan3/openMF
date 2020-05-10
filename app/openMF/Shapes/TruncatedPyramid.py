from app.openMF.Shapes.Point import Point
from app.openMF.Shapes.Shape import Shape
from app.openMF.Shapes.Triangle import Triangle


class TruncatedPyramid(Shape):
    def __init__(self, x: float, y: float, z: float, bottom_width: int, top_width: int, height: int):
        super().__init__(x, y, z)
        self.bottom_width = bottom_width
        self.top_width = top_width
        self.height = height

    def get_params(self):
        return str(self.bottom_width) + ' ' + str(self.top_width) + ' ' + str(self.height) + '\n'

    def triangles(self):
        triangles = list()
        half_bw, half_tw = self.bottom_width / 2, self.top_width / 2
        bx0 = bz0 = - half_bw
        bx1 = bz1 = half_bw
        tx0 = tz0 = - half_tw
        tx1 = tz1 = half_tw
        y0, y1 = -self.height / 2, self.height / 2
        """Front Face"""
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(tx1, y1, tz0), Point(tx0, y1, tz0)))
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(tx1, y1, tz0), Point(bx1, y0, bz0)))
        """Left Face"""
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(tx0, y1, tz1), Point(tx0, y1, tz0)))
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(tx0, y1, tz1), Point(bx0, y0, bz1)))
        """Bottom Face"""
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(bx1, y0, bz1), Point(bx1, y0, bz0)))
        triangles.append(Triangle(Point(bx0, y0, bz0), Point(bx1, y0, bz1), Point(bx0, y0, bz1)))
        """Back Face"""
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(bx0, y0, bz1), Point(tx0, y1, tz1)))
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(bx0, y0, bz1), Point(bx1, y0, bz1)))
        """Right Face"""
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(bx1, y0, bz0), Point(tx1, y1, tz0)))
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(bx1, y0, bz0), Point(bx1, y0, bz1)))
        """Top Face"""
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(tx0, y1, tz0), Point(tx0, y1, tz1)))
        triangles.append(Triangle(Point(tx1, y1, tz1), Point(tx0, y1, tz0), Point(tx1, y1, tz0)))
        return triangles
