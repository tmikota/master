# from cgl.plugins.unreal import alchemy as alc
import sys
import unreal
from PySide2 import QtWidgets, QtGui, QtUiTools, QtCore
from cgl.plugins.unreal_engine.ui.dialogs import LevelWidget


def run():
    app = QtWidgets.QApplication.instance()

    if not app:
        app = QtWidgets.QApplication(sys.argv)
    level_dialog = LevelWidget()
    level_dialog.show()
    app.exec_()


if __name__ == '__main__':
    run()
    print("IN MAIN")
