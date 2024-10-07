# main.py
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow  # Nhập lớp MainWindow từ file main_window.py


def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_app()
