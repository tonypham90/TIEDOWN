# data_processing/data_loader.py
import pandas as pd
import os


def load_csv(file_path):
    """Load data from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_csv(file_path)


def load_excel(file_path):
    """Load data from an Excel file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_excel(file_path)


def load_xml(file_path):
    """Load data from an XML file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_xml(file_path)


def load_pdf(file_path):
    """Load data from a PDF file (this may require additional libraries)."""
    # Implement logic to read PDF, e.g., using PyPDF2 or pdfplumber
    pass
