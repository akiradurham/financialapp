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

        self.namebox = QLineEdit('', self)
        self.namebox.setFont(font)

        self.hbox = QHBoxLayout()
        self.category1 = QRadioButton('Revenue')
        self.category2 = QRadioButton('Expense')
        self.hbox.addWidget(self.category1)
        self.hbox.addWidget(self.category2)

        self.pricebox = QLineEdit('', self)
        self.pricebox.setFont(font)

        self.datebox = QLineEdit('', self)
        self.datebox.setFont(font)

        self.a_button = QPushButton('Add a Record', self)
        self.a_button.setFont(font)
        self.a_button.clicked.connect(self.add)

        self.d_button = QPushButton('Delete a Record', self)
        self.d_button.setFont(font)
        self.d_button.clicked.connect(self.delete)

        form_layout = QFormLayout()

        label_item = QLabel("Item Name:")
        label_item.setFont(font)

        label_category = QLabel("Category:")
        label_category.setFont(font)

        label_price = QLabel("Price:")
        label_price.setFont(font)

        label_date = QLabel("Date:")
        label_date .setFont(font)

        form_layout.addRow(label_item, self.namebox)
        form_layout.addRow(label_category, self.category1)
        form_layout.addRow("", self.category2)
        form_layout.addRow(label_price, self.pricebox)
        form_layout.addRow(label_date, self.datebox)
        form_layout.addRow("", self.label)
        form_layout.addRow("", self.a_button)
        form_layout.addRow("", self.d_button)

        right_layout = QVBoxLayout()
        right_layout.addLayout(form_layout)
        right_layout.setAlignment(Qt.AlignTop)
        right_layout.setSpacing(30)

        width = QWidget()
        width.setMinimumWidth(300)
        width.setLayout(right_layout)

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(width, alignment=Qt.AlignRight)

        self.setLayout(main_layout)

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

    def which(self):
        if self.category1.isChecked():
            return 'Revenue'
        else:
            return 'Expense'

    def add(self):
        if self.input_check():
            record = rd.Records(self.namebox.text(), self.which(), self.pricebox.text(), self.datebox.text())
            if m.add(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()

    def delete(self):
        if self.input_check():
            record = rd.Records(self.namebox.text(), self.which(), self.pricebox.text(), self.datebox.text())
            if m.delete(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()

    def input_check(self):
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
