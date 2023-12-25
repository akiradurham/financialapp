from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import model as m
import ctypes


def addCourse():


def removeCourse():


class Finance(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('financelogo.png'))
        self.setWindowTitle('Financial Tracking Application')
        self.setGeometry(10, 10, 1280, 720)
        self.move(850, 300)
        self.show()


appId = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appId)
#  adding taskbar icon from https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105

app = QApplication([])
scene = Finance()
app.exec()
