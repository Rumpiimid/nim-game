from sys import exit, argv
from PyQt5 import QtWidgets
from core.core import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec_())
