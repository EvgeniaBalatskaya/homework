from unittest.mock import mock_open, patch

from file_processing.utils import read_json


def test_read_json_valid() -> None:
    """Тест корректного чтения JSON-файла."""
    mock_data = '[{"amount": 100.5, "currency": "USD", "date": "2024-03-01", "description": "Оплата подписки"}]'
    with patch("pathlib.Path.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
    expected = [{"amount": 100.5, "currency": "USD", "date": "2024-03-01", "description": "Оплата подписки"}]
    assert result == expected


def test_read_json_invalid() -> None:
    """Тест обработки ошибки при некорректном содержимом файла."""
    with patch("pathlib.Path.open", mock_open(read_data="not a json")):
        result = read_json("data/operations.json")
    assert result == []


def test_read_json_not_a_list() -> None:
    """Тест, когда JSON содержит не список, а словарь."""
    mock_data = '{"amount": 100.0, "currency": "RUB", "date": "2024-03-02", "description": "Перевод другу"}'
    with patch("pathlib.Path.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
    assert result == []


def test_read_json_file_not_found() -> None:
    """Тест обработки ошибки, если файл не найден."""
    with patch("pathlib.Path.exists", return_value=False):
        result = read_json("data/operations.json")
    assert result == []
