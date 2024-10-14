from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class BreakdownProcessingTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Breakdown Processing")
        layout.addWidget(label)
        self.setLayout(layout)
