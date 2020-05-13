from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from app.gui.newObject import UiNewObjectWindow
from app.openMF.Scene import Scene
from app.openMF.Shapes.MFObject import MFObject


class NewObjectWindow(QtWidgets.QMainWindow):
    def __init__(self, scene: Scene):
        super(NewObjectWindow, self).__init__()
        self.ui = UiNewObjectWindow()
        self.ui.setupUi(self)
        self.scene = scene
        self.ui.columns_count.valueChanged.connect(self.value_changed)
        self.ui.hats_count.valueChanged.connect(self.value_changed)
        self.ui.make_button.clicked.connect(self.make_object)
        self.ui.top_tower_size.valueChanged.connect(self.value_changed)

    def value_changed(self):
        self.ui.column_height.setEnabled(self.ui.columns_count.value())
        self.ui.tower_hat_size.setEnabled(self.ui.hats_count.value())
        self.ui.tower_hat_size.setMinimum(self.ui.top_tower_size.value() + 1)

    def make_object(self):
        params = self.check_params()
        if params:
            obj = MFObject.ra_gates(**params)
            if obj:
                new_name, name, i = 'RaGates', 'RaGates', 1
                while not self.scene.objects.get(new_name) is None:
                    new_name = name + str(i)
                    i += 1
                self.scene.objects[new_name] = obj
            self.close()

    def check_params(self):
        width, height, length = self.ui.base_width.value(), self.ui.base_height.value(), self.ui.base_length.value()
        c_count = self.ui.columns_count.value()
        c_height = self.ui.column_height.value()
        tower_top_size, tower_bot_size = self.ui.top_tower_size.value(), self.ui.bottom_tower_size.value()
        tower_height = self.ui.tower_height.value()
        hat_count, hat_size = self.ui.hats_count.value(), self.ui.tower_hat_size.value()
        if tower_top_size > tower_bot_size:
            self.message('Размер верхнего основания башни, должно быть меньше размеров нижнего основания башни!')
            return False
        if hat_count > 0 and hat_size < tower_top_size:
            self.message('Размер блока верхушки башни, должен быть больше размера верхнего основания башни!')
            return False
        return {'width': width, 'height': height, 'length': length, 'c_count': c_count, 'c_height': c_height,
                'tower_top_size': tower_top_size, 'tower_bot_size': tower_bot_size, 'tower_height': tower_height,
                'hat_count': hat_count, 'hat_size': hat_size}

    def message(self, msg: str):
        QMessageBox.information(self, 'Неверные данные!', msg)