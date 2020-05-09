import math
from PIL import Image
import numpy as np
from app.GObjects.Primitives import Point, Triangle
from app.GObjects.Shapes import Box
from app.GObjects.MFObject import MFObject
from app.GObjects.Matrix import Matrix


class Scene:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.objects = dict()
        self.objects['box1'] = Box(100, 50, 0, 100, 100, 100)
        self.objects['box2'] = Box(-40, 0, 0, 70, 70, 70)
        self.objects['box3'] = Box(0, 50, 0, 20, 20, 20)
        self.selected_obj = self.objects['box1']
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()

    def select(self, name):
        self.selected_obj = self.objects[name]

    def remove(self, name):
        self.objects.pop(name)

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()

    def rotate(self, deg, axis):
        if self.selected_obj:
            if axis == 'x':
                self.selected_obj.rotate_x = deg
            elif axis == 'y':
                self.selected_obj.rotate_y = deg
            else:
                self.selected_obj.rotate_z = deg

    def scale(self, scale_x, scale_y, scale_z):
        if self.selected_obj:
            self.selected_obj.scale_x = scale_x
            self.selected_obj.scale_y = scale_y
            self.selected_obj.scale_z = scale_z

    def move(self, x, y, z):
        if self.selected_obj:
            self.selected_obj.x = x
            self.selected_obj.y = y
            self.selected_obj.z = z

    def render(self, is_line=True):
        if is_line:
            self.line_render()
        else:
            self.fill_render()

    def fill_render(self):
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        for obj in self.objects.values():
            rotate = Matrix.rotate(obj.rotate_x, obj.rotate_y, obj.rotate_z)
            tranlsate = Matrix.tranlsation_matrix(obj.x, obj.y, obj.z)
            triangles = obj.triangles()
            zBuffer = [-math.inf for x in range(self.width * self.height)]
            for t in triangles:
                tt = t.sort() * (rotate.dot(tranlsate))
                self.fill_triangle(tt.a.x, tt.a.y, tt.a.z, tt.b.x, tt.b.y, tt.b.z, tt.c.x, tt.c.y, tt.c.z, zBuffer)

    def line_render(self):
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        for obj in self.objects.values():
            color = (153, 204, 255) if obj == self.selected_obj else (255, 255, 255)
            rotate = Matrix.rotate(obj.rotate_x, obj.rotate_y, obj.rotate_z)
            translate = Matrix.tranlsation_matrix(obj.x, obj.y, obj.z)
            scale = Matrix.scale_matrix(obj.scale_x, obj.scale_y, obj.scale_z)
            viewport = Matrix.viewport_matrix(self.width, self.height)
            triangles = obj.triangles()
            for t in triangles:
                tt = t * (scale.dot(rotate).dot(translate).dot(viewport))
                self.line(tt.a.x, tt.a.y, tt.b.x, tt.b.y, color)
                self.line(tt.b.x, tt.b.y, tt.c.x, tt.c.y, color)
                self.line(tt.a.x, tt.a.y, tt.c.x, tt.c.y, color)

    def fill_triangle(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, zBuffer, color):
        if y0 == y1 and y0 == y2:
            return
        x0, x1, x2 = self.width/2 + x0, self.width/2 + x1, self.width/2 + x2
        y0, y1, y2 = self.height / 2 + y0, self.height / 2 + y1, self.height / 2 + y2
        total_height = y2 - y0
        i = 0
        while i < total_height:
            second_half = i > y1-y0 or y1 == y0
            segment_height = y2-y1 if second_half else y1-y0
            alpha = float(i / total_height)
            h = y1-y0 if second_half else 0
            beta = float((i-h)/segment_height)
            a = Point(x0+(x2-x0) * alpha, y0+(y2-y0) * alpha, 0)
            b = Point(x1+(x2-x1) * beta, y0+(y2-y0) * beta, 0) if second_half else Point(x0+(x1-x0) * beta, y0+(y1-y0) * beta, 0)
            if a.x > b.x:
                a, b = b, a
            j = a.x
            while j <= b.x:
                phi = 1.0 if b.x == a.x else float((j-a.x)/(b.x-a.x))
                P = a + (b-a)*phi
                ind = int(P.x + P.y*self.width)
                if zBuffer[ind] < P.z:
                    self.canvas[j, y0+i] = color
                    zBuffer[int((y0+i)*self.width + j)] = P.z
                j += 1
            i += 1

    def new_fill_triangle(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color=(255, 255, 255)):
        x0, x1, x2 = self.width / 2 + x0, self.width / 2 + x1, self.width / 2 + x2
        y0, y1, y2 = self.height / 2 + y0, self.height / 2 + y1, self.height / 2 + y2
        minX = int(max(0, math.ceil(min(x0, min(x1, x2)))))
        maxX = int(min(self.width-1, math.floor(max(x0, max(x1, x2)))))
        minY = int(max(0, math.ceil(min(y0, min(y1, y2)))))
        maxY = int(min(self.height - 1, math.floor(max(y0, max(y1, y2)))))
        triangle_area = (y0-y2) * (x1-x2) + (y1-y2) * (x2-x0)
        y = minY
        if triangle_area:
            while y <= maxY:
                x = minX
                while x <= maxX:
                    b1 = ((y - y2) * (x1 - x2) + (y1 - y2) * (x2 - x)) / triangle_area
                    b2 = ((y - y0) * (x2 - x0) + (y2 - y0) * (x0 - x)) / triangle_area
                    b3 = ((y - y1) * (x0 - x1) + (y0 - y1) * (x1 - x)) / triangle_area
                    if 0 <= b1 <= 1 and 0 <= b2 <= 1 and 0 <= b3 <= 1:
                        self.canvas[x, y] = color
                    x += 1
                y += 1

    def line(self, x0: float, y0: float, x1: float, y1: float, color=(255, 255, 255)):
        y0 = self.height - y0 - 1
        y1 = self.height - y1 - 1
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
