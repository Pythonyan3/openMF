import math
import numpy as np


class Matrix:
    @staticmethod
    def tranlsation_matrix(x: int, y: int, z: int):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [x, y, z, 1]])

    @staticmethod
    def scale_matrix(scale_x: float, scale_y: float, scale_z: float):
        return np.array([[scale_x, 0, 0, 0],
                         [0, scale_y, 0, 0],
                         [0, 0, scale_z, 0],
                         [0, 0, 0, 1]])

    @staticmethod
    def rotate(deg_x: int, deg_y: int, deg_z: int):
        rotate_x = Matrix.rotate_x_matrix(deg_x)
        rotate_y = Matrix.rotate_y_matrix(deg_y)
        rotate_z = Matrix.rotate_z_matrix(deg_z)
        return rotate_x.dot(rotate_y).dot(rotate_z)

    @staticmethod
    def rotate_x_matrix(deg: int):
        rad = math.radians(deg)
        return np.array([[1, 0, 0, 0],
                      [0, math.cos(rad), math.sin(rad), 0],
                      [0, -math.sin(rad), math.cos(rad), 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def rotate_y_matrix(deg: int):
        rad = math.radians(deg)
        return np.array([[math.cos(rad), 0, math.sin(rad), 0],
                         [0, 1, 0, 0],
                         [-math.sin(rad), 0, math.cos(rad), 0],
                         [0, 0, 0, 1]])

    @staticmethod
    def rotate_z_matrix(deg: int):
        rad = math.radians(deg)
        return np.array([[math.cos(rad), math.sin(rad), 0, 0],
                         [-math.sin(rad), math.cos(rad), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

    @staticmethod
    def viewport_matrix(width: int, height: int):
        w = width/2
        h = height/2
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [w, h, 0, 1]])

    @staticmethod
    def perspective_matrix(fov: float, aspect: float, near: float, far: float):
        pass

    @staticmethod
    def orthographic_matrix(width: float, height: float, near: float, far: float):
        pass
