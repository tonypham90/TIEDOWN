from PySide6.QtWidgets import (
    QFormLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


def create_site_form(parent):
    form_layout = QFormLayout()

    bldg_name_input = QLineEdit()
    form_layout.addRow(QLabel("Building Name:"), bldg_name_input)

    segment_input = QLineEdit()
    form_layout.addRow(QLabel("Segment:"), segment_input)

    zone_input = QLineEdit()
    form_layout.addRow(QLabel("Zone:"), zone_input)

    floor_height_input = QLineEdit()
    form_layout.addRow(QLabel("Floor Height:"), floor_height_input)

    floor_thickness_input = QLineEdit()
    form_layout.addRow(QLabel("Floor Thickness:"), floor_thickness_input)

    sheet_name_input = QLineEdit()
    form_layout.addRow(QLabel("Sheet Name:"), sheet_name_input)

    # Buttons to add or update site information
    button_layout = QHBoxLayout()
    add_button = QPushButton("Add Site")
    add_button.clicked.connect(parent.add_site)
    update_button = QPushButton("Update Site")
    update_button.clicked.connect(parent.update_site)
    button_layout.addWidget(add_button)
    button_layout.addWidget(update_button)

    form_layout.addRow(button_layout)

    form_widget = QWidget()
    form_widget.setLayout(form_layout)

    return (
        form_widget,
        bldg_name_input,
        segment_input,
        zone_input,
        floor_height_input,
        floor_thickness_input,
        sheet_name_input,
    )
