from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые транзакции из CSV-файла."""
    df = pd.read_csv(file_path)
    # Преобразуем все значения в строку
    return [dict((str(k), str(v)) for k, v in row.items()) for row in df.to_dict(orient="records")]


def read_excel_transactions(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые транзакции из Excel-файла."""
    df = pd.read_excel(file_path)
    # Преобразуем все значения в строку
    return [dict((str(k), str(v)) for k, v in row.items()) for row in df.to_dict(orient="records")]
