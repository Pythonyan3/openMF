from app.GObjects.Primitives import Point, Triangle


class Shape:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.rotate_x, self.rotate_y, self.rotate_z = 0, 0, 0
        self.scale_x, self.scale_y, self.scale_z = 1, 1, 1


class Box(Shape):
    def __init__(self, x: float, y: float, z: float, width: int, height: int, length: int):
        super().__init__(x, y, z)
        self.length = length
        self.width = width
        self.height = height

    def triangles(self):
        triangles = list()
        half_w, half_h, half_l = int(self.width / 2), int(self.height / 2), int(self.length / 2)
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
