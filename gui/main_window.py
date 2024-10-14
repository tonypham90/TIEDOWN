from PyQt5.QtWidgets import QMainWindow, QTabWidget
from gui.import_data_tab import ImportDataTab
from gui.display_data_tab import DisplayDataTab
from gui.input_parameters_tab import InputParametersTab
from gui.breakdown_processing_tab import BreakdownProcessingTab
from gui.display_design_tab import DisplayDesignTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiedown")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.create_tabs()

    def create_tabs(self):
        self.tabs.addTab(InputParametersTab(), "Project Information")
        self.tabs.addTab(ImportDataTab(), "Import Data")
        self.tabs.addTab(DisplayDataTab(), "Display Data")

        self.tabs.addTab(BreakdownProcessingTab(), "Breakdown Processing")
        self.tabs.addTab(DisplayDesignTab(), "Display Design")
