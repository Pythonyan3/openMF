from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from app.openMF.Scene import Scene
from PyQt5 import QtWidgets
from app.gui.openMF import UiOpenMFWindow
from app.gui.newObjectController import NewObjectWindow


class OpenMFWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenMFWindow, self).__init__()
        self.ui = UiOpenMFWindow()
        self.ui.setupUi(self)
        self.scene = Scene(self.ui.scene_label.width(), self.ui.scene_label.height())
        self.new_object_window = NewObjectWindow(self.scene)
        self.button_pressed = 0
        self.x, self.y = 0, 0
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
        self.ui.scene_label.mouseMoveEvent = self.mouse_move
        self.ui.save_action.triggered.connect(self.save_object)
        self.ui.load_action.triggered.connect(self.load_object)
        self.ui.addObject.clicked.connect(self.show_modal)
        self.new_object_window.closeEvent = self.close_modal
        self.ui.aroundCenter.clicked.connect(self.camera_rotate_mode_change)
        self.ui.aroundEye.clicked.connect(self.camera_rotate_mode_change)
        self.ui.eye_set.clicked.connect(self.eye_set)
        self.ui.center_set.clicked.connect(self.center_set)
        self.ui.rasterize_scene.triggered.connect(self.rasterize_scene)

    def rotate(self, deg: int):
        sender = self.sender()
        if sender.objectName() == 'rotateXslider':
            self.scene.rotate_object(deg, 'x')
        if sender.objectName() == 'rotateYslider':
            self.scene.rotate_object(deg, 'y')
        if sender.objectName() == 'rotateZslider':
            self.scene.rotate_object(deg, 'z')
        self.redraw()

    def camera_rotate_mode_change(self):
        self.scene.camera.around_center = self.ui.aroundCenter.isChecked()

    def eye_set(self):
        self.scene.camera.eye.point[0] = self.ui.eye_x.value()
        self.scene.camera.eye.point[1] = self.ui.eye_y.value()
        self.scene.camera.eye.point[2] = self.ui.eye_z.value()
        self.redraw()

    def center_set(self):
        self.scene.camera.center.point[0] = self.ui.center_x.value()
        self.scene.camera.center.point[1] = self.ui.center_y.value()
        self.scene.camera.center.point[2] = self.ui.center_z.value()
        self.redraw()

    def scale(self):
        self.scene.scale_object(self.ui.scaleBoxX.value(), self.ui.scaleBoxY.value(), self.ui.scaleBoxZ.value())
        self.redraw()

    def move(self):
        self.scene.move_object(self.ui.moveBoxX.value(), self.ui.moveBoxY.value(), self.ui.moveBoxZ.value())
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
        name = self.ui.objectsBox.currentText()
        if name:
            self.ui.objectsBox.removeItem(self.ui.objectsBox.currentIndex())
            self.scene.remove(name, self.ui.objectsBox.currentText())
            self.redraw()

    def redraw(self):
        self.scene.render()
        qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
        self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))

    def rasterize_scene(self):
        self.scene.render(False)
        qimage = ImageQt(self.scene.image).rgbSwapped().rgbSwapped()
        self.ui.scene_label.setPixmap(QPixmap.fromImage(qimage))

    def wheelEvent(self, *args, **kwargs):
        delta = 1 if args[0].angleDelta().y() > 0 else -1
        self.scene.camera.fov -= delta
        if self.scene.camera.fov <= 0:
            self.scene.camera.fov = 0.1
        self.redraw()

    def mouse_press(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.ClosedHandCursor))
        self.button_pressed = event.button()

    def mouse_release(self, event):
        self.ui.scene_label.setCursor(QCursor(Qt.ArrowCursor))
        self.x, self.y = 0, 0
        self.button_pressed = 0

    def mouse_move(self, *args, **kwargs):
        if self.x == 0 and self.y == 0:
            self.x, self.y = args[0].x(), args[0].y()
        dx, dy = args[0].x() - self.x, args[0].y() - self.y
        if dx != 0 or dy != 0:
            self.x, self.y = args[0].x(), args[0].y()
        if self.button_pressed == 4:
            self.scene.camera.rotate_y += dx
            self.scene.camera.rotate_x += dy
            self.scene.camera.rotate()
        elif self.button_pressed == 1:
            dx, dy = dx * 0.5, dy * 0.5
            self.scene.camera.move(dx, dy, dx, dy)
        self.ui.eye_x.setValue(self.scene.camera.eye.x)
        self.ui.eye_y.setValue(self.scene.camera.eye.y)
        self.ui.eye_z.setValue(self.scene.camera.eye.z)
        self.ui.center_x.setValue(self.scene.camera.center.x)
        self.ui.center_y.setValue(self.scene.camera.center.y)
        self.ui.center_z.setValue(self.scene.camera.center.z)
        self.redraw()

    def labelResizeEvent(self, *args, **kwargs):
        if self.scene:
            self.scene.resize_scene(self.ui.scene_label.width(), self.ui.scene_label.height())
            self.redraw()

    def show_modal(self):
        self.new_object_window.show()

    def close_modal(self, *args, **kwargs):
        self.ui.objectsBox.clear()
        self.ui.objectsBox.addItems(self.scene.objects.keys())

    def save_object(self):
        if len(self.scene.objects):
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(self, "Сохранение сцены", f"{self.ui.objectsBox.currentText()}",
                                                      "openMF Object File (*.mfs)", options=options)
            if filename:
                self.scene.save_object(filename)
        else:
            QMessageBox.information(self, 'Внимание!', 'Сцена пуста!')

    def load_object(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Загрузка сцены", "",
                                                  "openMF Object File (*.mfs)", options=options)
        if filename:
            if not self.scene.load_object(filename):
                QMessageBox.information(self, 'Внимание!', 'Не удалось прочитать файл!')
            else:
                self.ui.objectsBox.clear()
                self.ui.objectsBox.addItems(self.scene.objects.keys())
