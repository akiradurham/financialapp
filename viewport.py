from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import pyqtgraph as graph
import model as m
import record as rd
import ctypes


class Finance(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.namebox = QLineEdit('', self)

        self.hbox = QHBoxLayout()
        self.category1 = QRadioButton('Revenue')
        self.category2 = QRadioButton('Expense')
        self.hbox.addWidget(self.category1)
        self.hbox.addWidget(self.category2)

        self.pricebox = QLineEdit('', self)

        self.datebox = QLineEdit('', self)

        self.a_button = QPushButton('Add a Record', self)
        self.a_button.clicked.connect(self.add)

        self.d_button = QPushButton('Delete a Record', self)
        self.d_button.clicked.connect(self.delete)

        self.form_layout = QFormLayout()
        self.add_labels(self.form_layout)

        self.plot = graph.PlotWidget(self)
        self.plot.setGeometry(25, 350, 521, 350)
        self.graph_setup()

        self.layout_setup()

        self.table_setup()

        self.setWindowIcon(QIcon('financelogo.png'))
        self.setWindowTitle('Financial Tracking Application')
        self.setFixedSize(1280, 720)
        self.move(325, 150)

    def table_setup(self):
        self.table = QTableView(self)
        self.model = QStandardItemModel()
        self.table.setGeometry(25, 25, 521, 300)
        headers = ['Name', 'Category', 'Price', 'Date']

        self.horizontal_header = self.table.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.setHorizontalHeaderLabels(headers)

        self.load_table()
        self.table.setModel(self.model)

    def layout_setup(self):
        right_layout = QVBoxLayout()
        right_layout.addLayout(self.form_layout)
        right_layout.setAlignment(Qt.AlignTop)
        right_layout.setSpacing(30)

        width = QWidget()
        width.setMinimumWidth(300)
        width.setLayout(right_layout)

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(width, alignment=Qt.AlignRight)

        self.setLayout(main_layout)

    def add_labels(self, form):
        label_item = QLabel("Item Name:")

        label_category = QLabel("Category:")

        label_price = QLabel("Price:")

        label_date = QLabel("Date:")

        form.addRow(label_item, self.namebox)
        form.addRow(label_category, self.hbox)
        form.addRow(label_price, self.pricebox)
        form.addRow(label_date, self.datebox)
        form.addRow("", self.label)
        form.addRow("", self.a_button)
        form.addRow("", self.d_button)

    def load_table(self):
        data = m.load_items()
        if data:
            data = sorted(data, key=lambda row: row[3], reverse=True)
            self.model.setRowCount(len(data))
            # self.model.setColumnCount(len(data[0]))
            for row, val in enumerate(data):
                for col, value in enumerate(val):
                    if col == 2 and val[1] == 'Expense':
                        value = '-$' + '{:.2f}'.format(value)
                    elif col == 2:
                        value = '$' + '{:.2f}'.format(value)
                    item = QStandardItem(str(value))
                    self.model.setItem(row, col, item)

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
                self.graph_setup()
            else:
                self.label.setStyleSheet('color: red;')
                self.label.setText('Price Format Incorrect or Repeat')

    def delete(self):
        if self.input_check():
            record = rd.Records(self.namebox.text(), self.which(), self.pricebox.text(), self.datebox.text())
            if m.delete(record):
                self.label.setStyleSheet('color: green;')
                self.label.setText('Successful')
                self.load_table()
                self.graph_setup()

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

    def graph_setup(self):
        self.plot.clear()
        data = m.load_items()
        if data:
            sorted_data = sorted(data, key=lambda row: float(row[3].replace('/', '')))
            name = [row[0] for row in sorted_data]
            category = [row[1] for row in sorted_data]
            price = [-float(row[2]) if row[1] == 'Expense' else float(row[2]) for row in sorted_data]
            date = [float(row[3].replace('/', '')) for row in sorted_data]
            scatter_plot = graph.ScatterPlotItem()
            scatter_plot.setData(date, price)
            line = graph.PlotCurveItem()
            line.setData(date, price, pen='r')
            horizontal = graph.InfiniteLine(pos=0, angle=0, pen='b')
            self.plot.addItem(scatter_plot)
            self.plot.addItem(line)
            self.plot.addItem(horizontal)


process = 'financial.app.allowing.taskbar.customization'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(process)
# icon https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# isolates the python script from the IDE, "own function" so we can give separate logo that is not python exe

app = QApplication([])
app.setStyleSheet('''
    QWidget {
        font-size: 16px;
    }
''')
scene = Finance()
scene.show()
app.exec()
