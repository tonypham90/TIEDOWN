# main_window.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiedown")

        layout = QVBoxLayout()

        label = QLabel("Welcome to Tiedown")
        button = QPushButton("Start")
        layout.addWidget(label)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setup_buttons(self):
        # Thêm logic xử lý cho các nút ở đây
        pass
