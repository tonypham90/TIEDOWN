from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from .layouts.import_data_table import create_table
from .layouts.import_data_buttons import create_buttons
from .layouts.import_data_path_field import create_path_field
from .layouts.settings_frame import SettingsFrame


class ImportDataTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter(Qt.Horizontal)

        self.init_table(splitter)
        self.init_right_panel(splitter)

        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def init_table(self, splitter):
        self.table = create_table()
        splitter.addWidget(self.table)
        splitter.setStretchFactor(0, 2)

    def init_right_panel(self, splitter):
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        right_layout.addLayout(create_path_field(self))
        right_layout.addLayout(create_buttons())
        right_layout.addWidget(SettingsFrame())

        right_layout.addStretch()
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)
        splitter.setStretchFactor(1, 1)
