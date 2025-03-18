from typing import Dict, List
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.file_processing.reader import read_csv_transactions, read_excel_transactions


# Фикстуры
@pytest.fixture
def mock_csv_data() -> List[Dict[str, str]]:
    return [
        {"date": "2024-03-01", "amount": "100", "currency": "USD"},
        {"date": "2024-03-02", "amount": "200", "currency": "EUR"},
    ]


@pytest.fixture
def mock_excel_data() -> List[Dict[str, str]]:
    return [
        {"date": "2024-03-03", "amount": "300", "currency": "GBP"},
        {"date": "2024-03-04", "amount": "400", "currency": "JPY"},
    ]


# Тесты
@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv: MagicMock, mock_csv_data: List[Dict[str, str]]) -> None:
    """Тестирование функции чтения CSV."""
    mock_read_csv.return_value = pd.DataFrame(mock_csv_data)
    result = read_csv_transactions("fake_path.csv")
    assert result == mock_csv_data


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel: MagicMock, mock_excel_data: List[Dict[str, str]]) -> None:
    """Тестирование функции чтения Excel."""
    mock_read_excel.return_value = pd.DataFrame(mock_excel_data)
    result = read_excel_transactions("fake_path.xlsx")
    assert result == mock_excel_data
