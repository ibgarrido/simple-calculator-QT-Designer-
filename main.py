from sys import exit
from frontend.calculator_window import CalculatorWindow
from backend.calculator_logic import CalculatorLogic
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    calculator_window = CalculatorWindow()
    calculator_logic = CalculatorLogic()
    # Signals frontend
    calculator_window.signal_sum.connect(calculator_logic.apply_action)
    calculator_window.signal_rest.connect(calculator_logic.apply_action)
    calculator_window.signal_division.connect(calculator_logic.apply_action)
    calculator_window.signal_product.connect(calculator_logic.apply_action)
    calculator_window.signal_AC.connect(calculator_logic.force_zero)
    # signals backend
    calculator_logic.signal_number.connect(calculator_window.final_number)

    calculator_window.show()
    exit(app.exec())
