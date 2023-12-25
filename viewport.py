from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import model as m
import ctypes


class Finance(QWidget):
    def __init__(self):
        super().__init__()

        global label
        label = QLabel('Label', self)

        self.a_button = QPushButton('Add a Record', self)
        self.a_button.setGeometry(1080, 550, 150, 50)
        font = self.a_button.font()
        font.setPointSize(11)
        self.a_button.setFont(font)
        self.a_button.clicked.connect(self.add)

        self.d_button = QPushButton('Delete a Record', self)
        self.d_button.setGeometry(1080, 620, 150, 50)
        font = self.d_button.font()
        font.setPointSize(11)
        self.d_button.setFont(font)
        self.d_button.font().setPointSize(25)
        self.d_button.clicked.connect(self.add)

        self.setWindowIcon(QIcon('financelogo.png'))
        self.setWindowTitle('Financial Tracking Application')
        self.setGeometry(10, 10, 1280, 720)
        self.move(325, 150)
        self.show()

    def add(self):
        m.add()
        label.setText('added record')

    def delete(self):
        m.delete()
        label.setText('deleted record')


process = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(process)
# icon https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# isolates the python script from the IDE, "own function" so we can give separate logo that is not python exe

app = QApplication([])
scene = Finance()
app.exec()
