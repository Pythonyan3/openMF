import math

import numpy as np


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.point = np.array([x, y, z])

    @property
    def x(self):
        return self.point[0]

    @property
    def y(self):
        return self.point[1]

    @property
    def z(self):
        return self.point[2]

    def __mul__(self, other):
        if type(other) == float:
            result = self.point * other
            return Point(result[0], result[1], result[2])
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        return Point(A[0], A[1], A[2])

    def __rmul__(self, other):
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        return Point(A[0], A[1], A[2])

    def __add__(self, other):
        result = self.point + other
        return Point(result[0], result[1], result[2])

    def __sub__(self, other):
        result = self.point - other
        return Point(result[0], result[1], result[2])

    def normilize(self):
        norm = np.linalg.norm(self.point)
        self.point = self.point / norm

    def copy(self):
        return Point(self.x, self.y, self.z)
