from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QFormLayout,
    QTabWidget,
    QListWidget,
    QPushButton,
    QListWidgetItem,
)
from .layouts.general_info.architect_info import create_architect_info_layout
from .layouts.general_info.structural_info import create_structural_info_layout
from .layouts.site_info.site_form import create_site_form
from .layouts.site_info.site_list import create_site_list


class GeneralInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Architect information
        architect_layout, self.architect_name_input, self.architect_plan_input = (
            create_architect_info_layout()
        )

        # Structural information
        (
            structural_layout,
            self.structural_engineer_input,
            self.structural_plan_input,
        ) = create_structural_info_layout()

        # Add both layouts to the main layout
        main_layout.addLayout(architect_layout)
        main_layout.addLayout(structural_layout)

        self.setLayout(main_layout)


class SiteInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Left side: List of buildings and zones
        self.site_list = create_site_list(self)
        main_layout.addWidget(self.site_list)

        # Right side: Form to enter or update site information
        (
            form_widget,
            self.bldg_name_input,
            self.segment_input,
            self.zone_input,
            self.floor_height_input,
            self.floor_thickness_input,
            self.sheet_name_input,
        ) = create_site_form(self)
        main_layout.addWidget(form_widget)

        self.setLayout(main_layout)

    def add_site(self):
        site_name = self.bldg_name_input.text()
        if site_name:
            item = QListWidgetItem(site_name)
            self.site_list.addItem(item)
            self.clear_form()

    def update_site(self):
        current_item = self.site_list.currentItem()
        if current_item:
            current_item.setText(self.bldg_name_input.text())
            self.clear_form()

    def load_site_info(self, item):
        self.bldg_name_input.setText(item.text())
        # Load other site information if available

    def clear_form(self):
        self.bldg_name_input.clear()
        self.segment_input.clear()
        self.zone_input.clear()
        self.floor_height_input.clear()
        self.floor_thickness_input.clear()
        self.sheet_name_input.clear()


class ProjectInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        tab_widget = QTabWidget()

        # Add sub-tabs
        tab_widget.addTab(GeneralInfoTab(), "General Information")
        tab_widget.addTab(SiteInfoTab(), "Site Info")

        layout.addWidget(tab_widget)
        self.setLayout(layout)
