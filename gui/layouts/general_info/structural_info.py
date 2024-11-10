from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLabel, QLineEdit


def create_structural_info_layout():
    layout = QVBoxLayout()
    form_layout = QFormLayout()

    structural_engineer_label = QLabel("Structural Engineer:")
    structural_engineer_input = QLineEdit()
    form_layout.addRow(structural_engineer_label, structural_engineer_input)

    structural_plan_label = QLabel("Structural Plan:")
    structural_plan_input = QLineEdit()
    form_layout.addRow(structural_plan_label, structural_plan_input)

    layout.addLayout(form_layout)
    return layout, structural_engineer_input, structural_plan_input
