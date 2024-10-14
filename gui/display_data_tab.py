from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class DisplayDataTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Display Data")
        layout.addWidget(label)
        self.setLayout(layout)
