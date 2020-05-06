from app.GObjects.Primitives import Point, Triangle


class Shape:
    pass


class Box(Shape):
    def __init__(self, start_point: Point, width: int, height: int, length: int):
        self.s_point = start_point
        self.length = length
        self.width = width
        self.height = height

    def triangles(self):
        triangles = list()
        half_w, half_h, half_l = int(self.width / 2), int(self.height / 2), int(self.length / 2)
        x0, y0, z0 = self.s_point.x - half_w, self.s_point.y - half_h, self.s_point.z - half_l
        x1, y1, z1 = self.s_point.x + half_w, self.s_point.y + half_h, self.s_point.z + half_l
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
