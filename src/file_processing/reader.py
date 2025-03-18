import pandas as pd
from typing import List, Dict


def read_csv_transactions(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые транзакции из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel_transactions(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые транзакции из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
