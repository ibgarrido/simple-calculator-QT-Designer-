import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import (pyqtSignal, Qt)
from PyQt5 import uic
from os import path


#  When using Qt Designer, we use this tuple to charge the ui file.
window_name, base_class = uic.loadUiType(path.join('frontend', 'calculator_window.ui'))


class CalculatorWindow(window_name, base_class):
    signal_sum = pyqtSignal(int, str)
    signal_rest = pyqtSignal(int, str)
    signal_division = pyqtSignal(int, str)
    signal_product = pyqtSignal(int, str)
    signal_equal = pyqtSignal(int, str)
    signal_AC = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Basic Calculator V1')
        # Signals related to build a number
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
        # Signals related to operating numbers
        self.boton_AC.clicked.connect(self.execute_AC)
        self.boton_equal.clicked.connect(self.execute_equal)
        self.boton_addition.clicked.connect(self.execute_sum)
        self.boton_subtraction.clicked.connect(self.execute_rest)
        self.boton_division.clicked.connect(self.execute_division)
        self.boton_product.clicked.connect(self.execute_product)
#  self.answer.Text() is the number we are going to work with

    def number_on_screen(self):
        # Auxiliar function to fix syntax error
        if self.answer.text() != 'Syntax Error':
            if '.' in self.answer.text():
                if '.' == self.answer.text()[len(self.answer.text())-1]:
                    return int(self.answer.text()[:len(self.answer.text())-1])
                else:
                    return float(self.answer.text())

            else:
                return int(self.answer.text())
        else:
            pass

    # Zones of the butons to construct numbers

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

    def execute_AC(self):
        self.answer.setText('0')
        self.signal_AC.emit()
        self.enable_all_butons()

    def execute_equal(self):
        # Actions related to the button '=' (equal)
        converted_number = str(self.number_on_screen())
        self.answer.setText(converted_number)
        self.signal_product.emit(self.number_on_screen(), '=')
        self.enable_all_butons()

    def execute_sum(self):
        # Actions related to the button '+' (addition)
        if self.answer.text().isdigit() == True:
            number = int(self.answer.text())
            self.signal_sum.emit(number, '+')
        else:
            number = float(self.answer.text())
            self.signal_sum.emit(number, '+')

    def execute_rest(self):
        # Actions related to the button '-' (subtraction)
        if self.answer.text().isdigit() is True:
            number = int(self.answer.text())
            self.signal_sum.emit(number, '-')
        else:
            number = float(self.answer.text())
            self.signal_sum.emit(number, '-')

    def execute_division(self):
        # Actions related to the button '÷' (division)
        if self.answer.text().isdigit() is True:
            number = int(self.answer.text())
            self.signal_sum.emit(number, '÷')
        else:
            number = float(self.answer.text())
            self.signal_sum.emit(number, '÷')

    def execute_product(self):
        # Actions related to the button 'x' (product)
        if self.answer.text().isdigit() is True:
            number = int(self.answer.text())
            self.signal_sum.emit(number, 'x')
        else:
            number = float(self.answer.text())
            self.signal_sum.emit(number, 'x')

    def final_number(self, number: str):
        if number == 'Syntax Error':
            self.disable_all_butons()
            self.answer.setText(number)
        else:
            self.answer.setText(number)

    def disable_all_butons(self):
        self.boton_1.setEnabled(False)
        self.boton_2.setEnabled(False)
        self.boton_3.setEnabled(False)
        self.boton_4.setEnabled(False)
        self.boton_5.setEnabled(False)
        self.boton_6.setEnabled(False)
        self.boton_7.setEnabled(False)
        self.boton_8.setEnabled(False)
        self.boton_9.setEnabled(False)
        self.boton_0.setEnabled(False)
        self.boton_decimal.setEnabled(False)
        # Signals related to operating numbers
        self.boton_equal.setEnabled(False)
        self.boton_addition.setEnabled(False)
        self.boton_subtraction.setEnabled(False)
        self.boton_division.setEnabled(False)
        self.boton_product.setEnabled(False)

    def enable_all_butons(self):
        self.boton_1.setEnabled(True)
        self.boton_2.setEnabled(True)
        self.boton_3.setEnabled(True)
        self.boton_4.setEnabled(True)
        self.boton_5.setEnabled(True)
        self.boton_6.setEnabled(True)
        self.boton_7.setEnabled(True)
        self.boton_8.setEnabled(True)
        self.boton_9.setEnabled(True)
        self.boton_0.setEnabled(True)
        self.boton_decimal.setEnabled(True)
        # Signals related to operating numbers
        self.boton_equal.setEnabled(True)
        self.boton_addition.setEnabled(True)
        self.boton_subtraction.setEnabled(True)
        self.boton_division.setEnabled(True)
        self.boton_product.setEnabled(True)


    def log(self, valor):
        print(valor)
