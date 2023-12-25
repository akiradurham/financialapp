from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import model as m
import ctypes


def addRecord():


def deleteRecord():


appId = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appId)
#  adding taskbar icon from https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
#  isolates the python script from the IDE, "own function" so we can give separate logo that is not python exe
app = QApplication([])
app.setWindowIcon(QIcon('financiallogo.png'))
window = QMainWindow()

window.setWindowTitle('Finance Tracker Application')
window.addButton = QPushButton('Add Record')
window.deleteButton = QPushButton('Delete Record')
window.addButton.clicked(addRecord())
window.deleteButton.clicked(deleteRecord())
window.show()

app.exec()
