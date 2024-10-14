from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QFileDialog


def create_path_field(parent):
    layout = QHBoxLayout()
    path_field = QLineEdit()
    path_field.setPlaceholderText("Enter data path...")
    browse_button = QPushButton("Browse")
    browse_button.clicked.connect(lambda: browse_file(parent, path_field))
    layout.addWidget(path_field)
    layout.addWidget(browse_button)
    return layout


def browse_file(parent, path_field):
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(parent, "Select Data File")
    if file_path:
        path_field.setText(file_path)
