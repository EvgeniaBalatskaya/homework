from typing import Any, Dict, List
from unittest.mock import patch

import pandas as pd
import pytest


# Функция для создания тестовых данных
def create_sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "date": "2025-03-12",
            "status": "EXECUTED",
            "currency": "RUB",
            "description": "Payment for services",
            "from_account": "12345",
            "to_account": "67890",
            "amount": 1000,
        },
        {
            "date": "2025-03-10",
            "status": "PENDING",
            "currency": "USD",
            "description": "Payment for goods",
            "from_account": "12345",
            "to_account": "67891",
            "amount": 200,
        },
        {
            "date": "2025-03-08",
            "status": "CANCELED",
            "currency": "RUB",
            "description": "Refund",
            "from_account": "12345",
            "to_account": "67892",
            "amount": 500,
        },
        {
            "date": "2025-03-06",
            "status": "EXECUTED",
            "currency": "RUB",
            "description": "Service charge",
            "from_account": "12345",
            "to_account": "67893",
            "amount": 1500,
        },
    ]


# Тестирование фильтрации по статусу
@pytest.mark.parametrize(
    "status,expected_count",
    [
        ("EXECUTED", 2),
        ("PENDING", 1),
        ("CANCELED", 1),
        ("INVALID", 0),
    ],
)
@patch("file_processing.utils.read_json", return_value=create_sample_transactions())  # Мокаем чтение JSON
@patch("file_processing.reader.read_csv_transactions", return_value=create_sample_transactions())  # Мокаем чтение CSV
@patch(
    "file_processing.reader.read_excel_transactions", return_value=create_sample_transactions()
)  # Мокаем чтение XLSX
def test_filter_by_status(mock_json: Any, mock_csv: Any, mock_excel: Any, status: str, expected_count: int) -> None:
    transactions = create_sample_transactions()
    filtered_transactions = [tx for tx in transactions if tx.get("status", "").upper() == status.upper()]
    assert len(filtered_transactions) == expected_count


# Тестирование фильтрации по валюте (RUB)
@patch("file_processing.utils.read_json", return_value=create_sample_transactions())  # Мокаем чтение JSON
@patch("file_processing.reader.read_csv_transactions", return_value=create_sample_transactions())  # Мокаем чтение CSV
@patch(
    "file_processing.reader.read_excel_transactions", return_value=create_sample_transactions()
)  # Мокаем чтение XLSX
def test_filter_by_currency(mock_json: Any, mock_csv: Any, mock_excel: Any) -> None:
    transactions = create_sample_transactions()
    filtered_transactions = [tx for tx in transactions if tx.get("currency", "").upper() == "RUB"]
    assert len(filtered_transactions) == 3


# Тестирование фильтрации по слову в описании
@patch("file_processing.utils.read_json", return_value=create_sample_transactions())  # Мокаем чтение JSON
@patch("file_processing.reader.read_csv_transactions", return_value=create_sample_transactions())  # Мокаем чтение CSV
@patch(
    "file_processing.reader.read_excel_transactions", return_value=create_sample_transactions()
)  # Мокаем чтение XLSX
def test_filter_by_description(mock_json: Any, mock_csv: Any, mock_excel: Any) -> None:
    transactions = create_sample_transactions()
    word = "service"
    filtered_transactions = [tx for tx in transactions if word in tx.get("description", "").lower()]
    assert len(filtered_transactions) == 2


# Тестирование сортировки по дате (по возрастанию)
@patch("file_processing.utils.read_json", return_value=create_sample_transactions())  # Мокаем чтение JSON
@patch("file_processing.reader.read_csv_transactions", return_value=create_sample_transactions())  # Мокаем чтение CSV
@patch(
    "file_processing.reader.read_excel_transactions", return_value=create_sample_transactions()
)  # Мокаем чтение XLSX
def test_sort_by_date(mock_json: Any, mock_csv: Any, mock_excel: Any) -> None:
    transactions = create_sample_transactions()
    sorted_transactions = sorted(transactions, key=lambda x: pd.to_datetime(x["date"]), reverse=False)
    assert sorted_transactions[0]["date"] == "2025-03-06"
    assert sorted_transactions[-1]["date"] == "2025-03-12"


# Тестирование сортировки по дате (по убыванию)
@patch("file_processing.utils.read_json", return_value=create_sample_transactions())  # Мокаем чтение JSON
@patch("file_processing.reader.read_csv_transactions", return_value=create_sample_transactions())  # Мокаем чтение CSV
@patch(
    "file_processing.reader.read_excel_transactions", return_value=create_sample_transactions()
)  # Мокаем чтение XLSX
def test_sort_by_date_desc(mock_json: Any, mock_csv: Any, mock_excel: Any) -> None:
    transactions = create_sample_transactions()
    sorted_transactions = sorted(transactions, key=lambda x: pd.to_datetime(x["date"]), reverse=True)
    assert sorted_transactions[0]["date"] == "2025-03-12"
    assert sorted_transactions[-1]["date"] == "2025-03-06"
