from app.openMF.Shapes.Shape import Shape
from app.openMF.Shapes import Cylinder, Box, TruncatedPyramid
from typing import List


class MFObject(Shape):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        self.shapes: List[Shape] = list()

    def append(self, object: Shape):
        if not isinstance(object, MFObject):
            self.shapes.append(object)
        else:
            self.shapes += object.shapes

    @staticmethod
    def ra_gates(*args, **kwargs):
        new_obj = MFObject(0, 0, 0)
        new_obj.append(Box.Box(0, 0, 0, kwargs['width'], kwargs['height'], kwargs['length']))  # Base

        tower_base_x, tower_base_y = (kwargs['width']/2) * 0.53, kwargs['height']/2 + 2  # Tower base
        tower_base_width, length = int(kwargs['width']/2 * (2/3)), int(kwargs['length']*(2/3))
        new_obj.append(Box.Box(-tower_base_x, tower_base_y, 0, tower_base_width, 4, length))
        new_obj.append(Box.Box(tower_base_x, tower_base_y, 0, tower_base_width, 4, length))

        stair_width = int((tower_base_x - tower_base_width/2) * 2)  # Stairs
        new_obj.append(Box.Box(0, tower_base_y-1, 0, stair_width, 2, length))
        new_obj.append(Box.Box(0, tower_base_y+1, 0, stair_width, 2, length-4))
        column_y = int(tower_base_y+2 + kwargs['c_height'] / 2)  # Columns
        column_x = int(stair_width / 2 - 2)
        step = int(kwargs['tower_top_size'] / (kwargs['c_count'] + 1))
        column_z = int(-kwargs['tower_top_size'] / 2) + step
        for _ in range(kwargs['c_count']):
            new_obj.append(Cylinder.Cylinder(-column_x, column_y, column_z, 2, kwargs['c_height']))
            new_obj.append(Cylinder.Cylinder(column_x, column_y, column_z, 2, kwargs['c_height']))
            column_z += step
        bridge_y = column_y + kwargs['c_height'] / 2 + 2
        bridge_width = (kwargs['tower_bot_size'] - kwargs['tower_top_size']) * (bridge_y/kwargs['tower_height']) + stair_width + 2
        bridge_length = kwargs['tower_top_size'] - 3    # Bridge
        new_obj.append(Box.Box(0, bridge_y, 0, bridge_width, 5, bridge_length))

        tower_y = tower_base_y + kwargs['tower_height'] / 2 + 2  # Towers
        new_obj.append(TruncatedPyramid.TruncatedPyramid(-tower_base_x, tower_y, 0, kwargs['tower_bot_size'],
                                                         kwargs['tower_top_size'], kwargs['tower_height']))
        new_obj.append(TruncatedPyramid.TruncatedPyramid(tower_base_x, tower_y, 0, kwargs['tower_bot_size'],
                                                         kwargs['tower_top_size'], kwargs['tower_height']))

        hat_y = tower_y + kwargs['tower_height']/2 + 1  # Tower's hats
        dsize = int(kwargs['hat_size'] / 5)
        for _ in range(kwargs['hat_count']):
            new_obj.append(Box.Box(-tower_base_x, hat_y, 0, kwargs['hat_size'], 2, kwargs['hat_size']))
            new_obj.append(Box.Box(tower_base_x, hat_y, 0, kwargs['hat_size'], 2, kwargs['hat_size']))
            hat_y += 2
            kwargs['hat_size'] -= dsize
        return new_obj

    def __len__(self):
        return len(self.shapes)
