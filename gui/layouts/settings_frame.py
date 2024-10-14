from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QFormLayout


class SettingsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        settings_layout = QFormLayout()
        settings_layout.setSpacing(10)
        settings_layout.setContentsMargins(10, 10, 10, 10)

        # Example settings
        setting1_label = QLabel("Setting 1:")
        setting1_input = QLineEdit()
        settings_layout.addRow(setting1_label, setting1_input)

        setting2_label = QLabel("Setting 2:")
        setting2_input = QLineEdit()
        settings_layout.addRow(setting2_label, setting2_input)

        self.setLayout(settings_layout)
