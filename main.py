# main.py
import sys
from PyQt5.QtWidgets import QApplication
import gui  # Import the gui package


def start_app():
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_app()
