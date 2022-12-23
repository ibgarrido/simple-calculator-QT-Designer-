from PyQt5.QtCore import QObject, pyqtSignal


class CalculatorLogic(QObject):

    signal_number = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.number = 0
        self.counter = 0
        self.awaited_action = None

    def send_number(self, number: str):
        self.signal_number.emit(number)

    def apply_action(self, number, action):
        # Case 1: initial
        if self.counter == 0:
            if action in ['+', '-', 'x', '÷']:
                self.number = number
                self.send_number('0')
                self.awaited_action = action
            # Case 1 cant happen again
            self.counter += 1
        # case 2: Executing awaited action
        else:
            if self.awaited_action == '+':
                self.number += number
                self.counter += 1
                self.send_number('0')
                self.awaited_action = action
            elif self.awaited_action == '-':
                self.number -= number
                self.counter += 1
                self.send_number('0')
                self.awaited_action = action
            elif self.awaited_action == 'x':
                self.number *= number
                self.counter += 1
                self.send_number('0')
                self.awaited_action = action
            elif self.awaited_action == '÷':
                try:
                    self.number = self.number/number
                    self.counter += 1
                    self.awaited_action = action
                    self.send_number('0')
                except ZeroDivisionError:
                    self.send_number('Syntax Error')
            if action == '=':
                self.send_number(str(self.number))
                self.counter = 0
                self.awaited_action = None

    def force_zero(self):
        # It forces to fix all class values in default values (Works with AC buton)
        self.number = 0
        self.counter = 0
        self.awaited_action = None
