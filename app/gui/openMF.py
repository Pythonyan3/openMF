# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openMF.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiOpenMFWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/3d-modeling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rotateYslider = QtWidgets.QSlider(self.layoutWidget)
        self.rotateYslider.setMaximum(360)
        self.rotateYslider.setSingleStep(10)
        self.rotateYslider.setOrientation(QtCore.Qt.Horizontal)
        self.rotateYslider.setObjectName("rotateYslider")
        self.verticalLayout.addWidget(self.rotateYslider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rotateXslider = QtWidgets.QSlider(self.layoutWidget)
        self.rotateXslider.setMaximum(360)
        self.rotateXslider.setSingleStep(10)
        self.rotateXslider.setOrientation(QtCore.Qt.Vertical)
        self.rotateXslider.setTickInterval(0)
        self.rotateXslider.setObjectName("rotateXslider")
        self.horizontalLayout.addWidget(self.rotateXslider)
        self.scene_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scene_label.sizePolicy().hasHeightForWidth())
        self.scene_label.setSizePolicy(sizePolicy)
        self.scene_label.setMinimumSize(QtCore.QSize(300, 300))
        self.scene_label.setText("")
        self.scene_label.setScaledContents(True)
        self.scene_label.setObjectName("scene_label")
        self.horizontalLayout.addWidget(self.scene_label)
        self.rotateZslider = QtWidgets.QSlider(self.layoutWidget)
        self.rotateZslider.setMaximum(360)
        self.rotateZslider.setSingleStep(10)
        self.rotateZslider.setOrientation(QtCore.Qt.Vertical)
        self.rotateZslider.setObjectName("rotateZslider")
        self.horizontalLayout.addWidget(self.rotateZslider)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.command_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.command_edit.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.command_edit.setFont(font)
        self.command_edit.setFrame(False)
        self.command_edit.setObjectName("command_edit")
        self.verticalLayout.addWidget(self.command_edit)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.manipulatingContainer = QtWidgets.QVBoxLayout(self.widget)
        self.manipulatingContainer.setContentsMargins(0, 0, 0, 0)
        self.manipulatingContainer.setObjectName("manipulatingContainer")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.objectsBox = QtWidgets.QComboBox(self.widget1)
        self.objectsBox.setStyleSheet("font: 75 8pt \"Sitka\";")
        self.objectsBox.setObjectName("objectsBox")
        self.verticalLayout_2.addWidget(self.objectsBox)
        self.addObject = QtWidgets.QPushButton(self.widget1)
        self.addObject.setStyleSheet("font: 75 10pt \"Sitka\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/sphinx.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addObject.setIcon(icon1)
        self.addObject.setIconSize(QtCore.QSize(25, 25))
        self.addObject.setObjectName("addObject")
        self.verticalLayout_2.addWidget(self.addObject)
        self.addShape = QtWidgets.QPushButton(self.widget1)
        self.addShape.setStyleSheet("font: 75 10pt \"Sitka\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/shapes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addShape.setIcon(icon2)
        self.addShape.setIconSize(QtCore.QSize(25, 25))
        self.addShape.setObjectName("addShape")
        self.verticalLayout_2.addWidget(self.addShape)
        self.removeObject = QtWidgets.QPushButton(self.widget1)
        self.removeObject.setStyleSheet("font: 75 10pt \"Sitka\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeObject.setIcon(icon3)
        self.removeObject.setIconSize(QtCore.QSize(25, 25))
        self.removeObject.setObjectName("removeObject")
        self.verticalLayout_2.addWidget(self.removeObject, 0, QtCore.Qt.AlignTop)
        self.manipulatingContainer.addWidget(self.widget1)
        self.widget2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy)
        self.widget2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scaleBoxX = QtWidgets.QDoubleSpinBox(self.widget2)
        self.scaleBoxX.setStyleSheet("font: 75 10pt \"Sitka\";")
        self.scaleBoxX.setValue(1.0)
        self.scaleBoxX.setMinimum(0.01)
        self.scaleBoxX.setMaximum(3.0)
        self.scaleBoxX.setSingleStep(0.01)
        self.scaleBoxX.setObjectName("scaleBoxX")
        self.horizontalLayout_2.addWidget(self.scaleBoxX)
        self.scaleBoxY = QtWidgets.QDoubleSpinBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.scaleBoxY.setFont(font)
        self.scaleBoxY.setStyleSheet("font: 75 10pt \"Sitka\";")
        self.scaleBoxY.setValue(1.0)
        self.scaleBoxY.setMinimum(0.01)
        self.scaleBoxY.setMaximum(3.0)
        self.scaleBoxY.setSingleStep(0.01)
        self.scaleBoxY.setObjectName("scaleBoxY")
        self.horizontalLayout_2.addWidget(self.scaleBoxY)
        self.scaleBoxZ = QtWidgets.QDoubleSpinBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.scaleBoxZ.setFont(font)
        self.scaleBoxZ.setStyleSheet("font: 75 10pt \"Sitka\";")
        self.scaleBoxZ.setValue(1.0)
        self.scaleBoxZ.setMinimum(0.01)
        self.scaleBoxZ.setMaximum(3.0)
        self.scaleBoxZ.setSingleStep(0.01)
        self.scaleBoxZ.setObjectName("scaleBoxZ")
        self.horizontalLayout_2.addWidget(self.scaleBoxZ)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.scaleButton = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.scaleButton.setFont(font)
        self.scaleButton.setStyleSheet("font: 75 12pt \"Sitka\";")
        self.scaleButton.setObjectName("scaleButton")
        self.verticalLayout_3.addWidget(self.scaleButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.moveBoxX = QtWidgets.QSpinBox(self.widget2)
        self.moveBoxX.setMinimum(-1000)
        self.moveBoxX.setMaximum(1000)
        self.moveBoxX.setObjectName("moveBoxX")
        self.horizontalLayout_3.addWidget(self.moveBoxX)
        self.moveBoxY = QtWidgets.QSpinBox(self.widget2)
        self.moveBoxY.setMinimum(-1000)
        self.moveBoxY.setMaximum(1000)
        self.moveBoxY.setObjectName("moveBoxY")
        self.horizontalLayout_3.addWidget(self.moveBoxY)
        self.moveBoxZ = QtWidgets.QSpinBox(self.widget2)
        self.moveBoxZ.setMinimum(-1000)
        self.moveBoxZ.setMaximum(1000)
        self.moveBoxZ.setObjectName("moveBoxZ")
        self.horizontalLayout_3.addWidget(self.moveBoxZ)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.moveButton = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.moveButton.setFont(font)
        self.moveButton.setStyleSheet("font: 75 12pt \"Sitka\";")
        self.moveButton.setObjectName("moveButton")
        self.verticalLayout_4.addWidget(self.moveButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.manipulatingContainer.addWidget(self.widget2)
        self.verticalLayout_6.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.load_action = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/3d-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_action.setIcon(icon4)
        self.load_action.setObjectName("load_action")
        self.save_action = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_action.setIcon(icon5)
        self.save_action.setObjectName("save_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_action.setIcon(icon6)
        self.exit_action.setObjectName("exit_action")
        self.menu.addSeparator()
        self.menu.addAction(self.load_action)
        self.menu.addAction(self.save_action)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "openMF"))
        self.rotateYslider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Вращение вокруг оси Y</p></body></html>"))
        self.rotateXslider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Вращение вокруг оси Х</p></body></html>"))
        self.rotateZslider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Вращение вокруг оси Z</p></body></html>"))
        self.command_edit.setPlaceholderText(_translate("MainWindow", "Введите команду..."))
        self.addObject.setText(_translate("MainWindow", "Добавить объект"))
        self.addShape.setText(_translate("MainWindow", "Добавить фигуру"))
        self.removeObject.setText(_translate("MainWindow", "Удалить объект"))
        self.scaleButton.setText(_translate("MainWindow", "Масштабировать"))
        self.moveButton.setText(_translate("MainWindow", "Переместить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.load_action.setText(_translate("MainWindow", "Загрузить объект"))
        self.save_action.setText(_translate("MainWindow", "Сохранить объект"))
        self.exit_action.setText(_translate("MainWindow", "Выход"))
