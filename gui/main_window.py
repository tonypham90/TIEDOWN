from PySide6.QtWidgets import QMainWindow, QTabWidget
from gui.import_data_tab import ImportDataTab
from gui.display_data_tab import DisplayDataTab
from gui.input_parameters_tab import InputParametersTab
from gui.breakdown_processing_tab import BreakdownProcessingTab
from gui.display_design_tab import DisplayDesignTab
from gui.project_info_tab import ProjectInfoTab  # Import the new tab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiedown")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.create_tabs()

    def create_tabs(self):
        self.tabs.addTab(ProjectInfoTab(), "Project Info")  # Add the new tab
        self.tabs.addTab(ImportDataTab(), "Import Data")
        self.tabs.addTab(InputParametersTab(), "Settings")
        self.tabs.addTab(BreakdownProcessingTab(), "Breakdown Processing")
        self.tabs.addTab(DisplayDataTab(), "Display Data")
        self.tabs.addTab(DisplayDesignTab(), "Display Design")
