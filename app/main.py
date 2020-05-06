from PyQt5 import QtWidgets
from app.gui.gui import OpenMFWindow
import sys


app = QtWidgets.QApplication([])
conn_window = OpenMFWindow()
conn_window.show()

sys.exit(app.exec())
