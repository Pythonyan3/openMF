import math
import numpy as np


class Matrix:
    @staticmethod
    def tranlsation_matrix(x: float, y: float, z: float):
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
        yScale = 1/math.tan(math.radians(fov)/2)
        xScale = yScale/aspect
        return np.array([[xScale, 0, 0, 0],
                         [0, yScale, 0, 0],
                         [0, 0, (far+near)/(far-near), 1],
                         [0, 0, -2*near*far/(far-near),  0]])

    @staticmethod
    def look_at_matrix(eye, center):
        sub = center - eye
        forward = sub.point / np.linalg.norm(sub.point)
        right = np.cross(np.array([0, 1, 0]), forward)
        right = right / np.linalg.norm(right)
        up = np.cross(forward, right)
        return np.array([[right[0], up[0], forward[0], 0],
                         [right[1], up[1], forward[1], 0],
                         [right[2], up[2], forward[2], 0],
                         [-right.dot(eye.point), -up.dot(eye.point), -forward.dot(eye.point), 1]])

    @staticmethod
    def sec_look_at_matrix(eye, pitch, yaw):
        cos_pitch = math.cos(pitch)
        sin_pitch = math.sin(pitch)
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)
        xaxis = np.array([cos_yaw, 0, -sin_yaw])
        yaxis = np.array([sin_yaw*sin_pitch, cos_pitch, cos_yaw*sin_pitch])
        zaxis = np.array([sin_yaw*cos_pitch, -sin_pitch, cos_yaw * cos_pitch])
        return np.array([[xaxis[0], xaxis[1], xaxis[2], -xaxis.dot(eye.point)],
                         [yaxis[0], yaxis[1], yaxis[2], -yaxis.dot(eye.point)],
                         [zaxis[0], zaxis[1], zaxis[2], -zaxis.dot(eye.point)],
                         [0, 0, 0, 1]])
