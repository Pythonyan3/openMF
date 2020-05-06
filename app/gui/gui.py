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
        self.rotateX = 0
        self.rotateY = 0
        self.rotateZ = 0
        self.ui.scene_label.resizeEvent = self.labelResizeEvent
        self.ui.rotateX.valueChanged.connect(self.rotate)
        self.ui.rotateY.valueChanged.connect(self.rotate)
        self.ui.rotateZ.valueChanged.connect(self.rotate)
        self.ui.scene_label.mousePressEvent = self.mouse_press
        self.ui.scene_label.mouseReleaseEvent = self.mouse_release

    def showEvent(self, *args, **kwargs):
        if not self.scene:
            self.scene = Scene(self.ui.scene_label.width(), self.ui.scene_label.height())
            box = Box(Point(0, 0, 0), 150, 10, 60)
            box2 = Box(Point(0, 10, 0), 130, 10, 40)
            box3 = Box(Point(-32, 65, 0), 30, 100, 30)
            box4 = Box(Point(32, 65, 0), 30, 100, 30)
            self.scene.triangles = box.triangles() + box2.triangles() + box3.triangles() + box4.triangles()
            self.scene.render()
            qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
            self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))

    def rotate(self, deg: int):
        sender = self.sender()
        if sender.objectName() == 'rotateX':
            self.scene.rotate(self.rotateX - deg, 'x')
            self.rotateX = deg
        if sender.objectName() == 'rotateY':
            self.scene.rotate(self.rotateY - deg, 'y')
            self.rotateY = deg
        if sender.objectName() == 'rotateZ':
            self.scene.rotate(self.rotateZ - deg, 'z')
            self.rotateZ = deg
        self.scene.render()
        qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
        self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_press(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouse_release(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.OpenHandCursor))

    def labelResizeEvent(self, *args, **kwargs):
        if self.scene:
            self.scene.resize(self.ui.scene_label.width(), self.ui.scene_label.height())
            qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
            self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))
