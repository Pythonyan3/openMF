import math
import numpy as np


class Matrix:
    @staticmethod
    def rotate_x_matrix(deg):
        rad = math.radians(deg)
        return np.array([[1, 0, 0, 0],
                      [0, math.cos(rad), math.sin(rad), 0],
                      [0, -math.sin(rad), math.cos(rad), 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def rotate_y_matrix(deg):
        rad = math.radians(deg)
        return np.array([[math.cos(rad), 0, math.sin(rad), 0],
                         [0, 1, 0, 0],
                         [-math.sin(rad), 0, math.cos(rad), 0],
                         [0, 0, 0, 1]])

    @staticmethod
    def rotate_z_matrix(deg):
        rad = math.radians(deg)
        return np.array([[math.cos(rad), math.sin(rad), 0, 0],
                         [-math.sin(rad), math.cos(rad), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
