from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLabel, QLineEdit


def create_architect_info_layout():
    layout = QVBoxLayout()
    form_layout = QFormLayout()

    architect_name_label = QLabel("Architect Name:")
    architect_name_input = QLineEdit()
    form_layout.addRow(architect_name_label, architect_name_input)

    architect_plan_label = QLabel("Architect Plan:")
    architect_plan_input = QLineEdit()
    form_layout.addRow(architect_plan_label, architect_plan_input)

    layout.addLayout(form_layout)
    return layout, architect_name_input, architect_plan_input
