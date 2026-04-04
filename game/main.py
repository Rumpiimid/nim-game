import sys
import os
from PyQt5 import QtWidgets


if getattr(sys, 'frozen', False):
    base_path = getattr(sys, '_MEIPASS', None)
    if base_path is None:
        base_path = os.path.dirname(__file__)
    os.chdir(base_path)
else:
    base_path = os.path.dirname(__file__)

os.environ['QT_PLUGIN_PATH'] = os.path.join(base_path, 'qt5_plugins')

ui_path = os.path.join(base_path, 'ui')
if ui_path not in sys.path:
    sys.path.insert(0, ui_path)

from core.core import Window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
