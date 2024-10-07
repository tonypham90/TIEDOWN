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


# job_input_widget.py
class JobInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        # ... [Phần mã khác không thay đổi] ...

        self.submit_button.clicked.connect(self.submit_job)

    def submit_job(self):
        job_name = self.job_name_input.text()
        material = self.material_input.text()
        size = self.size_input.text()

        # Ghi lại thông tin vào console hoặc xử lý thêm
        print(f"Job Name: {job_name}, Material: {material}, Size: {size}")

        # Có thể gọi hàm import_data ở đây nếu cần
