from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import model as m
import record as rd
import ctypes


class Finance(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('', self)
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(11)
        self.label.setFont(font)

        self.namebox = QLineEdit('Enter item name', self)
        self.namebox.setFont(font)

        self.hbox = QHBoxLayout()
        self.category1 = QRadioButton('Revenue')
        self.category2 = QRadioButton('Expense')
        self.hbox.addWidget(self.category1)
        self.hbox.addWidget(self.category2)

        self.pricebox = QLineEdit('Enter price value', self)
        self.pricebox.setFont(font)

        self.datebox = QLineEdit('Full Month, Day, Year', self)
        self.datebox.setFont(font)

        self.a_button = QPushButton('Add a Record', self)
        self.a_button.setFont(font)
        self.a_button.clicked.connect(self.add)

        self.d_button = QPushButton('Delete a Record', self)
        self.d_button.setFont(font)
        self.d_button.clicked.connect(self.delete)

        self.rightbox = QVBoxLayout()
        self.rightbox.addWidget(self.namebox)
        self.rightbox.addLayout(self.hbox)
        self.rightbox.addWidget(self.pricebox)
        self.rightbox.addWidget(self.datebox)
        self.rightbox.addWidget(self.label)
        self.rightbox.addWidget(self.a_button)
        self.rightbox.addWidget(self.d_button)
        self.rightbox.setAlignment(Qt.AlignTop)
        self.rightbox.setSpacing(30)

        self.width = QWidget()
        self.width.setMaximumWidth(200)
        self.width.setLayout(self.rightbox)

        self.mainlayout = QHBoxLayout(self)
        self.mainlayout.addWidget(self.width, alignment=Qt.AlignRight)

        self.setLayout(self.rightbox)

        self.table = QTableView(self)
        self.model = QStandardItemModel()
        self.table.setGeometry(25, 25, 521, 350)

        self.load_table()

        self.setWindowIcon(QIcon('financelogo.png'))
        self.setWindowTitle('Financial Tracking Application')
        self.setFixedSize(1280, 720)
        self.move(325, 150)

    def load_table(self):
        data = m.load_items()
        if not data:
            return
        self.model.setRowCount(len(data))
        self.model.setColumnCount(len(data[0]))
        for row, val in enumerate(data):
            for col, value in enumerate(val):
                item = QStandardItem(str(value))
                self.model.setItem(row, col, item)
        self.table.setModel(self.model)

    def add(self):
        if self.category1.isChecked():
            record = rd.Records(self.namebox.text(), 'Revenue', self.pricebox.text(), self.datebox.text())
            if m.add(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()
            else:
                self.label.setStyleSheet('color: red;')
                self.label.setText('Unsuccessful')
            self.load_table()
        elif self.category2.isChecked():
            record = rd.Records(self.namebox.text(), 'Expense', self.pricebox.text(), self.datebox.text())
            if m.add(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()
            else:
                self.label.setStyleSheet('color: red;')
                self.label.setText('Unsuccessful')
        else:
            self.label.setStyleSheet('color: red;')
            self.label.setText('Empty Category')

    def delete(self):
        if self.category1.isChecked():
            record = rd.Records(self.namebox.text(), 'Revenue', self.pricebox.text(), self.datebox.text())
            if m.delete(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()
            else:
                self.label.setStyleSheet('color: red;')
                self.label.setText('Unsuccessful')
        elif self.category2.isChecked():
            record = rd.Records(self.namebox.text(), 'Expense', self.pricebox.text(), self.datebox.text())
            if m.delete(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()
            else:
                self.label.setStyleSheet('color: red;')
                self.label.setText('Unsuccessful')
        else:
            self.label.setStyleSheet('color: red;')
            self.label.setText('Empty Category')

        def input_check():
            self.label.setStyleSheet('color: red;')
            if self.namebox.text() == '':
                self.label.setText('Enter A Name')
                return False
            elif not self.category1.isChecked() and not self.category2.isChecked():
                self.label.setText('Empty Category')
                return False
            elif self.pricebox.text() == '':
                self.label.setText('Enter A Price')
                return False
            elif self.datebox.text() == '':
                self.label.setText('Enter A Date')
                return False
            else:
                return True


process = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(process)
# icon https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# isolates the python script from the IDE, "own function" so we can give separate logo that is not python exe

app = QApplication([])
scene = Finance()
scene.show()
app.exec()
