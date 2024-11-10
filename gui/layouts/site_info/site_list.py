from PySide6.QtWidgets import QListWidget


def create_site_list(parent):
    site_list = QListWidget()
    site_list.itemClicked.connect(parent.load_site_info)
    return site_list
