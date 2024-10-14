from PyQt5.QtWidgets import QTableWidget


def create_table():
    table = QTableWidget()
    table.setRowCount(10)  # Example row count
    table.setColumnCount(5)  # Example column count
    return table
