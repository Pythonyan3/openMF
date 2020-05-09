import math

import numpy as np


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        if type(other) == float:
            return Point(self.x*other, self.y*other, self.z*other)
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        x, y, z = A[0], A[1], A[2]
        return Point(x, y, z)

    def __rmul__(self, other):
        A = np.array([self.x, self.y, self.z, 1]).dot(other)
        x, y, z = A[0], A[1], A[2]
        return Point(x, y, z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def to_np(self):
        return np.array([self.x, self.y, self.z])

    def normilize(self):
        mag = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        self.x = self.x / mag
        self.y = self.y / mag
        self.z = self.z / mag

    def copy(self):
        return Point(self.x, self.y, self.z)


class Triangle:
    def __init__(self, *args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]

    def __mul__(self, other):
        a = self.a * other
        b = self.b * other
        c = self.c * other
        return Triangle(a, b, c)

    def __rmul__(self, other):
        a = self.a * other
        b = self.b * other
        c = self.c * other
        return Triangle(a, b, c)

    def sort(self):
        a, b, c = self.a.copy(), self.b.copy(), self.c.copy()
        if a.y > b.y:
            a, b = b, a
        if a.y > c.y:
            a, c = c, a
        if b.y > c.y:
            b, c = c, b
        return Triangle(a, b, c)

    def copy(self):
        return Triangle(self.a.copy(), self.b.copy(), self.c.copy())
