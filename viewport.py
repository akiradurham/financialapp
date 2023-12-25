from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import model as m
import ctypes


class Finance(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(1080, 500, 150, 50)
        font = self.label.font()
        font.setPointSize(11)
        self.label.setFont(font)

        self.namebox = QLineEdit('Enter item name', self)
        self.namebox.setGeometry(1080, 450, 150, 50)
        self.namebox.setFont(font)



        self.pricebox = QLineEdit('Enter price value', self)
        self.pricebox.setGeometry(1080, 310, 150, 50)
        self.pricebox.setFont(font)

        self.a_button = QPushButton('Add a Record', self)
        self.a_button.setGeometry(1080, 550, 150, 50)
        self.a_button.setFont(font)
        self.a_button.clicked.connect(self.add)

        self.d_button = QPushButton('Delete a Record', self)
        self.d_button.setGeometry(1080, 620, 150, 50)
        self.d_button.setFont(font)
        self.d_button.clicked.connect(self.delete)

        # self.rightbox = QVBoxLayout(QWidget())
        # self.rightbox.addWidget(self.label)
        # self.rightbox.addWidget(self.namebox)
        # self.rightbox.addWidget(self.pricebox)
        # self.rightbox.addWidget(self.a_button)
        # self.rightbox.addWidget(self.d_button)
        # self.rightbox.setAlignment(Qt.AlignTop and Qt.AlignRight)
        # self.rightbox.setFixedWidth(150)

        self.setWindowIcon(QIcon('financelogo.png'))
        self.setWindowTitle('Financial Tracking Application')
        self.setFixedSize(1280, 720)
        self.move(325, 150)
        self.show()

    def add(self):

#        m.add()
        self.label.setStyleSheet('color: green;')
        self.label.setText('Successful')

    def delete(self):

#        m.delete()
        self.label.setStyleSheet('color: green;')
        self.label.setText('Successful')


process = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(process)
# icon https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# isolates the python script from the IDE, "own function" so we can give separate logo that is not python exe

app = QApplication([])
scene = Finance()
app.exec()
