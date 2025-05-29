import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,    
    QMessageBox,
    QFormLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BMI Calculator')
        self.setFixedSize(420, 340)

        # Thiết lập màu nền cho ứng dụng
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#e3f2fd'))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(18)

        # Tiêu đề ứng dụng
        title_label = QLabel('💪 BMI Calculator')
        title_font = QFont('Segoe UI', 20, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #1976d2; letter-spacing: 2px; margin-bottom: 10px;")
        layout.addWidget(title_label)

        # Sử dụng QFormLayout cho việc sắp xếp hợp lý các ô nhập liệu
        form_layout = QFormLayout()
        form_layout.setSpacing(18)

        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Nhập chiều cao (m)")
        self.height_input.setFixedHeight(36)
        self.height_input.setFont(QFont('Segoe UI', 12))
        self.height_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #90caf9;
                border-radius: 8px;
                padding-left: 10px;
                background: #ffffff;
            }
            QLineEdit:focus {
                border: 2.5px solid #1976d2;
            }
        """)
        form_layout.addRow("Chiều cao (m):", self.height_input)

        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Nhập cân nặng (kg)")
        self.weight_input.setFixedHeight(36)
        self.weight_input.setFont(QFont('Segoe UI', 12))
        self.weight_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #90caf9;
                border-radius: 8px;
                padding-left: 10px;
                background: #ffffff;
            }
            QLineEdit:focus {
                border: 2.5px solid #1976d2;
            }
        """)
        form_layout.addRow("Cân nặng (kg):", self.weight_input)

        layout.addLayout(form_layout)

        # Nút Calculate với style cải tiến
        self.calculate_button = QPushButton('Tính BMI')
        self.calculate_button.setFixedHeight(40)
        button_font = QFont('Segoe UI', 13, QFont.Bold)
        self.calculate_button.setFont(button_font)
        self.calculate_button.setStyleSheet("""
            QPushButton {
                background-color: #1976d2;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 15px;
                margin-top: 8px;
                margin-bottom: 8px;
                box-shadow: 0 4px 12px rgba(25,118,210,0.08);
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.calculate_button.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.calculate_button)

        # Label hiển thị kết quả với style riêng
        self.result_label = QLabel('Kết quả')
        result_font = QFont('Segoe UI', 13)
        self.result_label.setFont(result_font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("""
            color: #263238;
            background: #bbdefb;
            border-radius: 10px;
            padding: 12px 0;
            margin-top: 10px;
            letter-spacing: 1px;
        """)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_bmi(self):
        try:
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())
            if height <= 0 or weight <= 0:
                raise ValueError

            bmi = weight / (height ** 2)
            classification = self.classify_bmi(bmi)
            self.result_label.setText(f'BMI: {bmi:.2f} - {classification}')
        except ValueError:
            QMessageBox.warning(
                self,
                'Input Error',
                'Vui lòng nhập số hợp lệ cho chiều cao và cân nặng.'
            )

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return 'Gầy'
        elif 18.5 <= bmi < 24.9:
            return 'Bình thường'
        elif 25 <= bmi < 29.9:
            return 'Thừa cân'
        else:
            return 'Béo phì'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())
    
