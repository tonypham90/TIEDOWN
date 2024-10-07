# data_processing/data_processor.py
import pandas as pd


def clean_data(df):
    """Clean the DataFrame by removing duplicates and handling missing values."""
    df.drop_duplicates(inplace=True)
    df.fillna(
        method="ffill", inplace=True
    )  # Hoặc các phương pháp khác tùy theo yêu cầu
    return df


def process_data(df):
    """Process the data to perform calculations or transformations."""
    # Thực hiện các phép tính hoặc biến đổi dữ liệu ở đây
    return df  # Trả về DataFrame đã được xử lý


def summarize_data(df):
    """Summarize the data, e.g., get statistics."""
    return df.describe()  # Hoặc bất kỳ tóm tắt nào bạn cần
