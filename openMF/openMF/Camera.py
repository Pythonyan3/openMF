from openMF.openMF.Shapes.Point import Point
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

    def move(self, ex, ey, cx, cy):
        ex, cx = (-ex, -cx) if self.eye.z < 0 else (ex, cx)
        self.eye.point[0] -= ex
        self.eye.point[1] += ey
        self.center.point[0] -= cx
        self.center.point[1] += cy

    def rotate_around_center(self):
        camera = self.eye - self.center
        r = np.linalg.norm(camera.point)
        f = math.radians(self.rotate_y + 90)
        o = math.radians(self.rotate_x - 90)
        x = r * math.sin(o) * math.cos(f)
        y = r * math.cos(o)
        z = -(r * math.sin(o) * math.sin(f))
        self.eye = self.center + np.array([x, y, z])

    def rotate_around_eye(self):
        camera = self.center - self.eye
        r = np.linalg.norm(camera.point)
        f = math.radians(self.rotate_y + 90)
        o = math.radians(self.rotate_x + 90)
        x = r * math.sin(o) * math.cos(f)
        y = r * math.cos(o)
        z = r * math.sin(o) * math.sin(f)
        self.center = self.eye + np.array([x, y, z])
