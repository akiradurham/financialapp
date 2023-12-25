from PyQt5.QtWidgets import *
import model as m

window = QApplication([])
scene = QWidget()
layout = QVBoxLayout()

layout.addWidget(QRadioButton('Option 1'))
layout.addWidget(QRadioButton('Option 2'))

scene.setLayout(layout)
scene.show()

window.exec()
