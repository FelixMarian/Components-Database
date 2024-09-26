import os, sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import src.db.dataBase
from assets.py.mainWindow import Ui_MainWindow

def main():
    # Create the App and MainWindow instances
    app = QApplication([])
    MainWindow = QtWidgets.QMainWindow()

    # Apply UI to main window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Components')


    src.db.dataBase.initDatabase()

    MainWindow.show()
    app.exec_()
if __name__ == '__main__':
    main();