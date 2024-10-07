# job_input_widget.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton


class JobInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.job_name_input = QLineEdit(self)
        self.material_input = QLineEdit(self)
        self.size_input = QLineEdit(self)

        layout.addWidget(QLabel("Job Name:"))
        layout.addWidget(self.job_name_input)
        layout.addWidget(QLabel("Material:"))
        layout.addWidget(self.material_input)
        layout.addWidget(QLabel("Size:"))
        layout.addWidget(self.size_input)

        self.submit_button = QPushButton("Submit", self)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
