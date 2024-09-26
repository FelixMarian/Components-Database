import os, sys
sys.path.append(os.path.abspath('assets'))
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from assets.py.mainWindow import Ui_MainWindow
import db.dataBase

def main():
    # Create the App and MainWindow instances
    app = QApplication([])
    MainWindow = QtWidgets.QMainWindow()

    # Apply UI to main window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Components')


    db.dataBase.initDatabase()

    MainWindow.show()
    app.exec_()
if __name__ == '__main__':
    main();