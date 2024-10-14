from PyQt5.QtWidgets import QVBoxLayout, QPushButton


def create_buttons():
    layout = QVBoxLayout()
    button_width = 100

    import_button = QPushButton("Import")
    reset_button = QPushButton("Reset")
    clean_button = QPushButton("Clean Data")

    import_button.setFixedWidth(button_width)
    reset_button.setFixedWidth(button_width)
    clean_button.setFixedWidth(button_width)

    layout.addWidget(import_button)
    layout.addWidget(reset_button)
    layout.addWidget(clean_button)

    return layout
