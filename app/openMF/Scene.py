from app.openMF.Shapes.Box import Box
from app.openMF.Camera import Camera
from PIL import Image
from app.openMF.Matrix import Matrix
import math
import numpy as np
from app.openMF.Shapes import Point, Box, Cylinder, TruncatedPyramid, MFObject


SHAPES = {'Box': Box.Box,
          'Cylinder': Cylinder.Cylinder,
          'TruncatedPyramid': TruncatedPyramid.TruncatedPyramid,
          'MFObject': MFObject.MFObject}


class Scene:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.camera = Camera(Point.Point(0.0, 0.0, 1.0), Point.Point(0.0, 0.0, 0.0), 90, 0.1, 100)
        self.objects = dict()
        self.objects['box'] = Box.Box(0, 0, 0, 100, 100, 100)
        self.selected_obj = self.objects['box']
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()

    def select(self, name):
        self.selected_obj = self.objects[name]

    def remove(self, name, new_name):
        self.objects.pop(name)
        self.selected_obj = self.objects[new_name] if new_name else None

    def resize_scene(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()

    def rotate_object(self, deg, axis):
        if self.selected_obj:
            if axis == 'x':
                self.selected_obj.rotate_x = deg
            elif axis == 'y':
                self.selected_obj.rotate_y = deg
            else:
                self.selected_obj.rotate_z = deg

    def scale_object(self, scale_x, scale_y, scale_z):
        if self.selected_obj:
            self.selected_obj.scale_x = scale_x
            self.selected_obj.scale_y = scale_y
            self.selected_obj.scale_z = scale_z

    def move_object(self, x, y, z):
        if self.selected_obj:
            self.selected_obj.x = x
            self.selected_obj.y = y
            self.selected_obj.z = z

    def render(self, is_line=True):
        if is_line:
            self.line_render()
        else:
            self.fill_render()

    def fill_render(self):
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        projection = Matrix.perspective_matrix(self.camera.fov, self.width / self.height, self.camera.near,
                                               self.camera.far)
        look = Matrix.look_at_matrix(self.camera.eye, self.camera.center)
        z_buffer = [-math.inf for _ in range(self.width * self.height)]
        for obj in self.objects.values():
            color = (153, 204, 255) if obj == self.selected_obj else (255, 255, 255)
            obj_rotate = Matrix.rotate(obj.rotate_x, obj.rotate_y, obj.rotate_z)
            obj_translate = Matrix.tranlsation_matrix(obj.x, obj.y, obj.z)
            obj_scale = Matrix.scale_matrix(obj.scale_x, obj.scale_y, obj.scale_z)
            if isinstance(obj, MFObject.MFObject):
                for shape in obj.shapes:
                    rotate = Matrix.rotate(shape.rotate_x, shape.rotate_y, shape.rotate_z)
                    translate = Matrix.tranlsation_matrix(shape.x, shape.y, shape.z)
                    scale = Matrix.scale_matrix(shape.scale_x, shape.scale_y, shape.scale_z)
                    triangles = shape.triangles()
                    for t in triangles:
                        model = scale.dot(rotate).dot(translate).dot(obj_scale).dot(obj_rotate).dot(obj_translate)
                        tt = t * (model.dot(look).dot(projection))
                        self.new_fill_triangle(tt.a.x, tt.a.y, tt.a.z, tt.b.x, tt.b.y, tt.b.z, tt.c.x, tt.c.y, tt.c.z, z_buffer, color)
            else:
                triangles = obj.triangles()
                for t in triangles:
                    model = (obj_scale.dot(obj_rotate).dot(obj_translate))
                    tt = t * (model.dot(look).dot(projection))
                    self.new_fill_triangle(tt.a.x, tt.a.y, tt.a.z, tt.b.x, tt.b.y, tt.b.z, tt.c.x, tt.c.y, tt.c.z, z_buffer, color)

    def line_render(self):
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.canvas = self.image.load()
        projection = Matrix.perspective_matrix(self.camera.fov, self.width / self.height, self.camera.near,
                                               self.camera.far)
        look = Matrix.look_at_matrix(self.camera.eye, self.camera.center)
        viewport = Matrix.viewport_matrix(self.width, self.height)
        for obj in self.objects.values():
            color = (153, 204, 255) if obj == self.selected_obj else (255, 255, 255)
            obj_rotate = Matrix.rotate(obj.rotate_x, obj.rotate_y, obj.rotate_z)
            obj_translate = Matrix.tranlsation_matrix(obj.x, obj.y, obj.z)
            obj_scale = Matrix.scale_matrix(obj.scale_x, obj.scale_y, obj.scale_z)
            if isinstance(obj, MFObject.MFObject):
                for shape in obj.shapes:
                    rotate = Matrix.rotate(shape.rotate_x, shape.rotate_y, shape.rotate_z)
                    translate = Matrix.tranlsation_matrix(shape.x, shape.y, shape.z)
                    scale = Matrix.scale_matrix(shape.scale_x, shape.scale_y, shape.scale_z)
                    triangles = shape.triangles()
                    for t in triangles:
                        model = scale.dot(rotate).dot(translate).dot(obj_scale).dot(obj_rotate).dot(obj_translate)
                        tt = t * (model.dot(look).dot(projection))
                        self.line(tt.a.x, tt.a.y, tt.b.x, tt.b.y, color)
                        self.line(tt.b.x, tt.b.y, tt.c.x, tt.c.y, color)
                        self.line(tt.a.x, tt.a.y, tt.c.x, tt.c.y, color)
            else:
                triangles = obj.triangles()
                for t in triangles:
                    model = (obj_scale.dot(obj_rotate).dot(obj_translate))
                    tt = t * (model.dot(look).dot(projection))
                    self.line(tt.a.x, tt.a.y, tt.b.x, tt.b.y, color)
                    self.line(tt.b.x, tt.b.y, tt.c.x, tt.c.y, color)
                    self.line(tt.a.x, tt.a.y, tt.c.x, tt.c.y, color)

    def new_fill_triangle(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, z_buffer, color=(255, 255, 255)):
        x0, x1, x2 = self.width / 2 + x0, self.width / 2 + x1, self.width / 2 + x2
        y0, y1, y2 = self.height-1-(self.height / 2 + y0), self.height-1-(self.height / 2 + y1), self.height-1-(self.height / 2 + y2)
        minX = int(max(0, math.ceil(min(x0, min(x1, x2)))))
        maxX = int(min(self.width-1, math.floor(max(x0, max(x1, x2)))))
        minY = int(max(0, math.ceil(min(y0, min(y1, y2)))))
        maxY = int(min(self.height - 1, math.floor(max(y0, max(y1, y2)))))
        triangle_area = (y0-y2) * (x1-x2) + (y1-y2) * (x2-x0)
        y = minY
        ab = np.array([x0, y0, z0]) - np.array([x1, y1, z1])
        ac = np.array([x0, y0, z0]) - np.array([x2, y2, z2])
        norm = np.array([ab[1]*ac[2] - ab[2]*ac[1],
                         ab[2]*ac[0] - ab[0]*ac[2],
                         ab[0]*ac[1] - ab[1]*ac[0], 1])
        l = np.linalg.norm(norm)
        shade = abs(norm[2]/l)
        if triangle_area:
            while y <= maxY:
                x = minX
                while x <= maxX:
                    b1 = ((y - y2) * (x1 - x2) + (y1 - y2) * (x2 - x)) / triangle_area
                    b2 = ((y - y0) * (x2 - x0) + (y2 - y0) * (x0 - x)) / triangle_area
                    b3 = ((y - y1) * (x0 - x1) + (y0 - y1) * (x1 - x)) / triangle_area
                    if 0 <= b1 <= 1 and 0 <= b2 <= 1 and 0 <= b3 <= 1:
                        depth = b1*z0 + b2*z1 + b3*z2
                        z_index = y * self.width + x
                        if z_buffer[z_index] < depth:
                            self.canvas[x, y] = (int(color[0] * shade), int(color[1] * shade), int(color[2] * shade))
                            z_buffer[z_index] = depth
                    x += 1
                y += 1

    def line(self, x0: float, y0: float, x1: float, y1: float, color=(255, 255, 255)):
        x0, x1 = self.width / 2 + x0, self.width / 2 + x1
        y0, y1 = self.height - 1 - (self.height / 2 + y0), self.height - 1 - (self.height / 2 + y1)
        steep = False
        if abs(x0 - x1) < abs(y0 - y1):
            steep = True
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx, dy = x1 - x0, y1 - y0
        error, derror = 0, abs(dy)*2
        x, y = x0, y0
        while x <= x1:
            if steep:
                if 0 <= y <= self.width - 1 and 0 <= x <= self.height - 1:
                    self.canvas[y, x] = color
            else:
                if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
                    self.canvas[x, y] = color
            error += derror
            if error > dx:
                y = y + 1 if y1 > y0 else y-1
                error -= dx*2
            x += 1

    def save_object(self, filename):
        with open(filename, 'w') as file:
            file.write(f'camera-eye: {self.camera.eye.x} {self.camera.eye.y} {self.camera.eye.z}\n' )
            file.write(f'camera-center: {self.camera.center.x} {self.camera.center.y} {self.camera.center.z}\n')
            file.write(f'camera-fov-near-far: {self.camera.fov} {self.camera.near} {self.camera.far}\n')
            file.write(f'camera-rotate: {self.camera.rotate_x} {self.camera.rotate_y}\n')
            for name, obj in self.objects.items():
                if isinstance(obj, MFObject.MFObject):
                    file.write(obj.__class__.__name__ + ' ' + name + ' ' + str(len(obj)) + '\n')
                    file.write(obj.get_modifications())
                    for shape in obj.shapes:
                        file.write(shape.__class__.__name__ + ' ' + name + ' 1\n')
                        file.write(shape.get_params())
                        file.write(shape.get_modifications())
                else:
                    file.write(obj.__class__.__name__ + ' ' + name + ' 1\n')
                    file.write(obj.get_params())
                    file.write(obj.get_modifications())

    def load_object(self, filename):
        try:
            objects3d = dict()
            with open(filename, 'r') as file:
                x, y, z = file.readline().strip('\n').split(' ')[1:]
                eye = Point.Point(float(x), float(y), float(z))
                x, y, z = file.readline().strip('\n').split(' ')[1:]
                center = Point.Point(float(x), float(y), float(z))
                fov, near, far = file.readline().strip('\n').split(' ')[1:]
                camera = Camera(eye, center, int(fov), float(near), float(far))
                rotate_x, rotate_y = file.readline().strip('\n').split(' ')[1:]
                camera.rotate_x, camera.rotate_y = int(rotate_x), int(rotate_y)
                while True:
                    line = file.readline()
                    if not line:
                        break
                    class_name, name, count = line.strip('\n').split(' ')
                    if class_name == 'MFObject':
                        obj = self.read_object(file)
                        objects3d[name] = obj
                    else:
                        shape = self.read_shape(file, class_name)
                        if objects3d.get(name) is not None:
                            objects3d[name].append(shape)
                        else:
                            objects3d[name] = shape
                self.objects = objects3d
                self.camera = camera
                return True
        except TypeError:
            return False

    def read_object(self, file):
        x, y, z = file.readline().strip('\n').split(' ')[1:]
        rotate_x, rotate_y, rotate_z = file.readline().strip('\n').split(' ')[1:]
        scale_x, scale_y, scale_z = file.readline().strip('\n').split(' ')[1:]
        obj = MFObject.MFObject(float(x), float(y), float(z))
        obj.rotate_x, obj.rotate_y, obj.rotate_z = float(rotate_x), float(rotate_y), float(rotate_z)
        obj.scale_x, obj.scale_y, obj.scale_z = float(scale_x), float(scale_y), float(scale_z)
        return obj

    def read_shape(self, file, class_name):
        shape_params = [int(x) for x in file.readline().strip('\n').split(' ')[1:]]
        x, y, z = file.readline().strip('\n').split(' ')[1:]
        rotate_x, rotate_y, rotate_z = file.readline().strip('\n').split(' ')[1:]
        scale_x, scale_y, scale_z = file.readline().strip('\n').split(' ')[1:]
        shape = SHAPES[class_name](float(x), float(y), float(z), *shape_params)
        shape.rotate_x, shape.rotate_y, shape.rotate_z = float(rotate_x), float(rotate_y), float(rotate_z)
        shape.scale_x, shape.scale_y, shape.scale_z = float(scale_x), float(scale_y), float(scale_z)
        return shape

    def show(self):
        self.image.show()
