from app.GObjects.Shapes import Box
import numpy as np
import math
from app.GObjects.Primitives import Point
from app.GObjects.Scene import Scene


A = np.array([0, 0, -1])
B = np.array([33, 25, 5])
B = B / np.sqrt(np.sum(B**2))
print(A.dot(B))