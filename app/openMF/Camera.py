import numpy as np
import math


class Camera:
    def __init__(self, eye, center, fov, near, far):
        self.eye = np.array(eye)
        self.center = np.array(center)
        self.fov = math.radians(fov)
        self.near = near
        self.far = far
        self.pitch = 0.01
        self.yaw = 0.01
