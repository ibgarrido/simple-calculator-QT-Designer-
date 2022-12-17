import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import (pyqtSignal, Qt)
from PyQt5 import uic


#  When using Qt Designer, we use this tuple to charge the ui file.
window_name, base_class = uic.loadUiType('calculator_window.ui')


class CalculatorWindow(window_name, base_class):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Basic Calculator V1')
        self.boton_1.clicked.connect(self.assign_1)
        self.boton_2.clicked.connect(self.assign_2)
        self.boton_3.clicked.connect(self.assign_3)
        self.boton_4.clicked.connect(self.assign_4)
        self.boton_5.clicked.connect(self.assign_5)
        self.boton_6.clicked.connect(self.assign_6)
        self.boton_7.clicked.connect(self.assign_7)
        self.boton_8.clicked.connect(self.assign_8)
        self.boton_9.clicked.connect(self.assign_9)
        self.boton_0.clicked.connect(self.assign_0)
        self.boton_decimal.clicked.connect(self.assign_decimal)

    def assign_1(self):
        if self.answer.text() == '0':
            number = self.boton_1.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_1.text()
            self.answer.setText(number)

    def assign_2(self):
        if self.answer.text() == '0':
            number = self.boton_2.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_2.text()
            self.answer.setText(number)

    def assign_3(self):
        if self.answer.text() == '0':
            number = self.boton_3.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_3.text()
            self.answer.setText(number)

    def assign_4(self):
        if self.answer.text() == '0':
            number = self.boton_4.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_4.text()
            self.answer.setText(number)

    def assign_5(self):
        if self.answer.text() == '0':
            number = self.boton_5.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_5.text()
            self.answer.setText(number)

    def assign_6(self):
        if self.answer.text() == '0':
            number = self.boton_6.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_6.text()
            self.answer.setText(number)

    def assign_7(self):
        if self.answer.text() == '0':
            number = self.boton_7.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_7.text()
            self.answer.setText(number)

    def assign_8(self):
        if self.answer.text() == '0':
            number = self.boton_8.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_8.text()
            self.answer.setText(number)

    def assign_9(self):
        if self.answer.text() == '0':
            number = self.boton_9.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_9.text()
            self.answer.setText(number)

    def assign_0(self):
        if self.answer.text() == '0':
            number = self.boton_0.text()
            self.answer.setText(number)
        else:
            number = self.answer.text()+self.boton_0.text()
            self.answer.setText(number)

    def assign_decimal(self):
        if self.boton_decimal.text() not in self.answer.text():
            number = self.answer.text()+self.boton_decimal.text()
            self.answer.setText(number)









# Debuging.
if __name__ == '__main__':
    app = QApplication([])
    calculator_window = CalculatorWindow()
    calculator_window.show()
    sys.exit(app.exec())
