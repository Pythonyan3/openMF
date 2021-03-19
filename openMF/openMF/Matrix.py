import math
import numpy as np


class Matrix:
    @staticmethod
    def translation_matrix(dx: float, dy: float, dz: float):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [dx, dy, dz, 1]])

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
        scale_y = 1/math.tan(math.radians(fov/2))
        scale_x = scale_y/aspect
        return np.array([[scale_x, 0, 0, 0],
                         [0, scale_y, 0, 0],
                         [0, 0, far/(far-near), 1],
                         [0, 0, -near*far/(far-near),  0]])

    @staticmethod
    def look_at_matrix(eye, center):
        sub = eye - center
        forward = sub.point / np.linalg.norm(sub.point)
        right = np.cross(np.array([0, 1, 0]), forward)
        right = right / np.linalg.norm(right)
        up = np.cross(forward, right)
        return np.array([[right[0], up[0], forward[0], 0],
                         [right[1], up[1], forward[1], 0],
                         [right[2], up[2], forward[2], 0],
                         [-right.dot(eye.point), -up.dot(eye.point), -forward.dot(eye.point), 1]])
