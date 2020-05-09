from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from app.GObjects.Shapes import Box, Point
from app.GObjects.Scene import Scene
from PyQt5 import QtWidgets
from app.gui.openMF import UiOpenMFWindow


class OpenMFWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenMFWindow, self).__init__()
        self.ui = UiOpenMFWindow()
        self.ui.setupUi(self)
        self.scene = None
        self.ui.scene_label.resizeEvent = self.labelResizeEvent
        self.ui.rotateXslider.valueChanged.connect(self.rotate)
        self.ui.rotateYslider.valueChanged.connect(self.rotate)
        self.ui.rotateZslider.valueChanged.connect(self.rotate)
        self.ui.scene_label.mousePressEvent = self.mouse_press
        self.ui.scene_label.mouseReleaseEvent = self.mouse_release
        self.ui.objectsBox.currentTextChanged.connect(self.select_object)
        self.ui.removeObject.clicked.connect(self.remove_object)
        self.ui.scaleButton.clicked.connect(self.scale)
        self.ui.moveButton.clicked.connect(self.move)

    def showEvent(self, *args, **kwargs):
        if not self.scene:
            self.scene = Scene(self.ui.scene_label.width(), self.ui.scene_label.height())
            self.ui.objectsBox.addItems(self.scene.objects.keys())
            self.redraw()

    def rotate(self, deg: int):
        sender = self.sender()
        if sender.objectName() == 'rotateXslider':
            self.scene.rotate(deg, 'x')
        if sender.objectName() == 'rotateYslider':
            self.scene.rotate(deg, 'y')
        if sender.objectName() == 'rotateZslider':
            self.scene.rotate(deg, 'z')
        self.redraw()

    def scale(self):
        self.scene.scale(self.ui.scaleBoxX.value(), self.ui.scaleBoxY.value(), self.ui.scaleBoxZ.value())
        self.redraw()

    def move(self):
        self.scene.move(self.ui.moveBoxX.value(), self.ui.moveBoxY.value(), self.ui.moveBoxZ.value())
        self.redraw()

    def select_object(self, name):
        if name:
            self.scene.select(name)
            self.ui.rotateXslider.setValue(self.scene.selected_obj.rotate_x)
            self.ui.rotateYslider.setValue(self.scene.selected_obj.rotate_y)
            self.ui.rotateZslider.setValue(self.scene.selected_obj.rotate_z)
            self.ui.scaleBoxX.setValue(self.scene.selected_obj.scale_x)
            self.ui.scaleBoxY.setValue(self.scene.selected_obj.scale_y)
            self.ui.scaleBoxZ.setValue(self.scene.selected_obj.scale_z)
            self.ui.moveBoxX.setValue(self.scene.selected_obj.x)
            self.ui.moveBoxY.setValue(self.scene.selected_obj.y)
            self.ui.moveBoxZ.setValue(self.scene.selected_obj.z)
            self.redraw()

    def remove_object(self):
        if self.ui.objectsBox.currentText():
            self.scene.remove(self.ui.objectsBox.currentText())
            self.ui.objectsBox.removeItem(self.ui.objectsBox.currentIndex())
            self.redraw()

    def redraw(self):
        self.scene.render()
        qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
        self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_press(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouse_release(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.ArrowCursor))

    def labelResizeEvent(self, *args, **kwargs):
        if self.scene:
            self.scene.resize(self.ui.scene_label.width(), self.ui.scene_label.height())
            self.redraw()
