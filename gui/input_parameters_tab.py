from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class InputParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Input Parameters")
        layout.addWidget(label)
        self.setLayout(layout)
