from app.openMF.Matrix import Matrix
from app.openMF.Shapes.Point import Point
import numpy as np
import math


class Camera:
    def __init__(self, eye: Point, center: Point, fov, near, far):
        self.eye = eye
        self.center = center
        self.fov = fov
        self.near = near
        self.far = far
        self.around_center = True
        self.rotate_x, self.rotate_y = 0, 0

    def rotate(self):
        if self.around_center:
            self.rotate_around_center()
        else:
            self.rotate_around_eye()

    def rotate_around_center(self):
        camera = self.eye - self.center
        r = np.linalg.norm(camera.point)
        f = math.radians(self.rotate_y + 90)
        o = math.radians(self.rotate_x - 90)
        x = r * math.sin(o) * math.cos(f)
        y = r * math.cos(o)
        z = r * math.sin(o) * math.sin(f)
        z = 0.001 if z == 0.0 else z
        self.eye = self.center + np.array([x, y, z])

    def rotate_around_eye(self):
        camera = self.eye - self.center
        r = np.linalg.norm(camera.point)
        f = math.radians(self.rotate_y + 90)
        o = math.radians(self.rotate_x - 90)
        x = r * math.sin(o) * math.cos(f)
        y = r * math.cos(o)
        z = r * math.sin(o) * math.sin(f)
        self.center = self.eye + np.array([x, y, z])
