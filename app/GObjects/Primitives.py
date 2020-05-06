import numpy as np


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        self.x, self.y, self.z = A[0], A[1], A[2]
        return self

    def __rmul__(self, other):
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        self.x, self.y, self.z = A[0], A[1], A[2]
        return self

    def copy(self):
        return Point(self.x, self.y, self.z)


class Triangle:
    def __init__(self, *args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]

    def __mul__(self, other):
        self.a = self.a * other
        self.b = self.b * other
        self.c = self.c * other
        return self

    def __rmul__(self, other):
        self.a = self.a * other
        self.b = self.b * other
        self.c = self.c * other
        return self
