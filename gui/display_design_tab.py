from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class DisplayDesignTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Display Design")
        layout.addWidget(label)
        self.setLayout(layout)
