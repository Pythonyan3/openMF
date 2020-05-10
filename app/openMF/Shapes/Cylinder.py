import math
from PIL import Image, ImageDraw
from app.openMF.Shapes.Point import Point
from app.openMF.Shapes.Shape import Shape
from app.openMF.Shapes.Triangle import Triangle


class Cylinder(Shape):
    def __init__(self, x: float, y: float, z: float, radius: int, height: int):
        super().__init__(x, y, z)
        self.radius = radius
        self.height = height

    def get_params(self):
        return str(self.radius) + ' ' + str(self.height) + '\n'

    def triangles(self):
        img = Image.new('RGB', (800, 800), 'black')
        canvas = img.load()
        draw = ImageDraw.Draw(img)
        triangles = list()
        points = []
        half_height = self.height/2
        deg, step = 270, 360 / 20
        while deg <= 360:
            x = self.radius * math.cos(math.radians(deg))
            z = self.radius * math.sin(math.radians(deg))
            points.append(Point(x, half_height, z))
            points.append(Point(x, half_height, -z))
            points.append(Point(-x, half_height, z))
            points.append(Point(-x, half_height, -z))
            points.append(Point(x, -half_height, z))
            points.append(Point(x, -half_height, -z))
            points.append(Point(-x, -half_height, z))
            points.append(Point(-x, -half_height, -z))
            if 270 < deg < 360:
                triangles.append(Triangle(points[-5], points[-6], points[-13]))
                triangles.append(Triangle(points[-6], points[-13], points[-14]))
                triangles.append(Triangle(points[-7], points[-8], points[-15]))
                triangles.append(Triangle(points[-8], points[-15], points[-16]))

                triangles.append(Triangle(points[-1], points[-2], points[-9]))
                triangles.append(Triangle(points[-2], points[-9], points[-10]))
                triangles.append(Triangle(points[-3], points[-4], points[-11]))
                triangles.append(Triangle(points[-4], points[-11], points[-12]))

                triangles.append(Triangle(points[-1], points[-5], points[-9]))
                triangles.append(Triangle(points[-5], points[-9], points[-13]))
                triangles.append(Triangle(points[-2], points[-6], points[-10]))
                triangles.append(Triangle(points[-6], points[-10], points[-14]))

                triangles.append(Triangle(points[-3], points[-7], points[-11]))
                triangles.append(Triangle(points[-7], points[-11], points[-15]))
                triangles.append(Triangle(points[-4], points[-8], points[-12]))
                triangles.append(Triangle(points[-8], points[-12], points[-16]))
            deg += step
        triangles.append(Triangle(points[-1], points[-5], points[-9]))
        triangles.append(Triangle(points[-5], points[-9], points[-13]))
        triangles.append(Triangle(points[-5], points[-1], points[-14]))
        triangles.append(Triangle(points[-1], points[-14], points[-10]))

        triangles.append(Triangle(points[-7], points[-15], points[-3]))
        triangles.append(Triangle(points[-15], points[-3], points[-11]))
        triangles.append(Triangle(points[-7], points[-16], points[-12]))
        triangles.append(Triangle(points[-7], points[-12], points[-3]))

        triangles.append(Triangle(points[-1], points[-9], points[-10]))
        triangles.append(Triangle(points[-3], points[-11], points[-12]))
        triangles.append(Triangle(points[-5], points[-13], points[-14]))
        triangles.append(Triangle(points[-7], points[-15], points[-16]))
        return triangles