import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt
import os
import datetime

class ImageViewerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setFixedSize(900, 650)

        # Cài đặt màu nền
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#e0f7fa'))
        self.setPalette(palette)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(20)

        # Tiêu đề ứng dụng
        title_label = QLabel('🖼️ Image Viewer Application')
        title_font = QFont('Segoe UI', 22, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #009688; letter-spacing: 2px; margin-bottom: 10px;")
        main_layout.addWidget(title_label)

        # Layout ngang chứa ảnh và các nút
        center_layout = QHBoxLayout()
        center_layout.setSpacing(30)

        # Label hiển thị ảnh
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap())
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(600, 400)
        self.image_label.setStyleSheet("""
            QLabel {
                border: 3px solid #b2dfdb;
                border-radius: 18px;
                background-color: #ffffff;
                margin-top: 10px;
                margin-bottom: 10px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.10);
                transition: border 0.3s;
            }
            QLabel:hover {
                border: 3px solid #009688;
            }
        """)
        center_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Layout dọc cho các nút
        button_layout = QVBoxLayout()
        button_layout.setSpacing(20)

        # Nút "Open Image"
        self.open_button = QPushButton('📂 Open Image')
        self.open_button.setFont(QFont('Segoe UI', 13, QFont.Bold))
        self.open_button.setCursor(Qt.PointingHandCursor)
        self.open_button.setStyleSheet("""
            QPushButton {
                background-color: #009688;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 8px;
                font-size: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }
            QPushButton:hover {
                background-color: #26a69a;
            }
        """)
        self.open_button.clicked.connect(self.open_image)
        button_layout.addWidget(self.open_button)

        # Nút "Close App"
        close_button = QPushButton('❌ Close App')
        close_button.setFont(QFont('Segoe UI', 13, QFont.Bold))
        close_button.setCursor(Qt.PointingHandCursor)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 8px;
                font-size: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        close_button.clicked.connect(self.close_app)
        button_layout.addWidget(close_button)

        button_layout.addStretch()
        center_layout.addLayout(button_layout)
        main_layout.addLayout(center_layout)

        # Label hiển thị thông tin ảnh (nằm phía dưới)
        self.info_label = QLabel('Image Info: ')
        self.info_label.setFont(QFont('Segoe UI', 12))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("""
            color: #333333;
            background: #e0f2f1;
            border-radius: 10px;
            padding: 12px 0;
            margin: 10px 0 20px 0;
            letter-spacing: 1px;
        """)
        main_layout.addWidget(self.info_label)

        self.setLayout(main_layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.jpeg *.bmp *.gif)')
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

            # Lấy thông tin ảnh
            file_info = os.stat(file_path)
            file_size = f"{round(file_info.st_size / 1024, 2)} KB"
            creation_time = datetime.datetime.fromtimestamp(file_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
            resolution = f"{pixmap.width()} x {pixmap.height()}"
            self.info_label.setText(
                f"File: {os.path.basename(file_path)}\nResolution: {resolution}\nSize: {file_size}\nCreated: {creation_time}"
            )

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewerApp()
    window.show()
    sys.exit(app.exec_())