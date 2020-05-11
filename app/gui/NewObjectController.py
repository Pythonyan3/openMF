from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from app.gui.newObject import UiNewObjectWindow
from app.openMF.Scene import Scene


class NewObjectWindow(QtWidgets.QMainWindow):
    def __init__(self, scene: Scene):
        super(NewObjectWindow, self).__init__()
        self.ui = UiNewObjectWindow()
        self.ui.setupUi(self)
        self.scene = scene
        self.ui.columns_count.valueChanged.connect(self.value_changed)
        self.ui.hats_count.valueChanged.connect(self.value_changed)
        self.ui.make_button.clicked.connect(self.make_object)

    def value_changed(self):
        self.ui.column_height.setEnabled(self.ui.columns_count.value())
        self.ui.column_radius.setEnabled(self.ui.columns_count.value())
        self.ui.tower_hat_size.setEnabled(self.ui.hats_count.value())

    def make_object(self):
        if self.check_params():
            pass

    def check_params(self):
        width, height, length = self.ui.base_width.value(), self.ui.base_height.value(), self.ui.base_length.value()
        col_count = self.ui.columns_count.value()
        radius, c_height = self.ui.column_radius.value(), self.ui.column_height.value()
        tower_top_size, tower_bot_size = self.ui.top_tower_size.value(), self.ui.bottom_tower_size.value()
        tower_height = self.ui.tower_height.value()
        hat_count, hat_size = self.ui.hats_count.value(), self.ui.tower_hat_size.value()
        if tower_top_size > tower_bot_size:
            self.message('Размер верхнего основания башни, должно быть меньше размеров нижнего основания башни!')
            return False
        if hat_size < tower_top_size:
            self.message('Размер блока верхушек башен, должен быть больше размеров верхних оснований башен!')
            return False
        if width and height and length and tower_top_size and tower_bot_size and tower_height:
            if (col_count > 0 and radius > 0 and c_height > 0) or (col_count == 0):
                if (hat_count > 0 and hat_size > 0) or hat_count == 0:
                    print('make')
                    return True
        self.message('Не все поля заполнены значениями!\n' 
                     'Значение всех полей, кроме кол-ва колонн и верхушек, должны быть больше 0!')

    def message(self, msg: str):
        QMessageBox.information(self, 'Неверные данные!', msg)