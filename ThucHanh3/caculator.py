import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        self.setFixedSize(340, 420)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#f1f8e9'))
        self.setPalette(palette)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        self.display = QLineEdit()
        self.display.setFont(QFont('Segoe UI', 18))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #aed581;
                border-radius: 8px;
                background: #ffffff;
                padding-right: 10px;
            }
        """)
        main_layout.addWidget(self.display)

        grid = QGridLayout()
        grid.setSpacing(12)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4)
        ]

        for btn in buttons:
            if len(btn) == 3:
                text, row, col = btn
                button = QPushButton(text)
                grid.addWidget(button, row, col)
            else:
                text, row, col, rowspan, colspan = btn
                button = QPushButton(text)
                grid.addWidget(button, row, col, rowspan, colspan)
            button.setFont(QFont('Segoe UI', 15))
            button.setFixedHeight(48)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #aed581;
                    border: none;
                    border-radius: 8px;
                    color: #263238;
                }
                QPushButton:hover {
                    background-color: #7cb342;
                    color: white;
                }
            """)
            button.clicked.connect(self.on_button_clicked)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())