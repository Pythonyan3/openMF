from PIL import Image
import numpy as np
from app.GObjects.Primitives import Point
from app.GObjects.Matrix import Matrix


class Scene:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.objects = dict()
        self.triangles = list()
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()

    def test_proj(self):
        proj = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 1]])
        for triangle in self.triangles:
            triangle = triangle * proj
        self.rotate(90, 'z')

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        self.line_render()

    def rotate(self, deg, axis):
        if axis == 'x':
            R = Matrix.rotate_x_matrix(deg)
        elif axis == 'y':
            R = Matrix.rotate_y_matrix(deg)
        else:
            R = Matrix.rotate_z_matrix(deg)
        for triangle in self.triangles:
            triangle = triangle * R

    def render(self, is_line=True):
        if is_line:
            self.line_render()
        else:
            pass

    def line_render(self):
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        for t in self.triangles:
            self.line(t.a.x, t.a.y, t.b.x, t.b.y)
            self.line(t.b.x, t.b.y, t.c.x, t.c.y)
            self.line(t.a.x, t.a.y, t.c.x, t.c.y)

    def line(self, x0: float, y0: float, x1: float, y1: float, color=(255, 255, 255)):
        x0, y0 = self.width / 2 + x0, self.height / 2 + y0
        x1, y1 = self.width / 2 + x1, self.height / 2 + y1
        y0, y1 = self.height - y0 - 1, self.height - y1 - 1
        steep = False
        if abs(x0 - x1) < abs(y0 - y1):
            steep = True
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx, dy = x1 - x0, y1 - y0
        error, derror = 0, abs(dy)*2
        x, y = x0, y0
        while x <= x1:
            if steep:
                if 0 <= y <= self.width - 1 and 0 <= x <= self.height - 1:
                    self.canvas[y, x] = color
            else:
                if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
                    self.canvas[x, y] = color
            error += derror
            if error > dx:
                y = y + 1 if y1 > y0 else y-1
                error -= dx*2
            x += 1

    def show(self):
        self.image.show()
