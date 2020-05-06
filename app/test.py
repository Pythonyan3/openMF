from app.GObjects.Shapes import Box
import numpy as np
import math
from app.GObjects.Primitives import Point
from app.GObjects.Scene import Scene


A = np.array([50, 50, 50, 1])

B = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [25, 25, 25, 1]])

C = np.array([[math.cos(math.radians(45)), math.sin(math.radians(45)), 0, 0],
              [-math.sin(math.radians(45)), math.cos(math.radians(45)), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
A = A.dot(C)
print(round(A[0]), "---", round(A[1]), "---", float(A[2]), "---")
scene = Scene(800, 800)
box = Box(Point(50, 50, 50), 100, 100, 100)
