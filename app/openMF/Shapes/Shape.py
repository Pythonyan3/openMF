class Shape:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z
        self.rotate_x, self.rotate_y, self.rotate_z = 0, 0, 0
        self.scale_x, self.scale_y, self.scale_z = 1, 1, 1

    def get_modifications(self):
        result = '' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.z) + '\n'
        result += str(self.rotate_x) + ' ' + str(self.rotate_y) + ' ' + str(self.rotate_z) + '\n'
        result += str(self.scale_x) + ' ' + str(self.scale_y) + ' ' + str(self.scale_z) + '\n'
        return result

    def get_params(self):
        pass

    def triangles(self):
        pass
