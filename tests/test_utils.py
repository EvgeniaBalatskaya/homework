import pytest
from unittest.mock import mock_open, patch
from src.utils import read_json


def test_read_json_valid():
    """
    Тест для проверки успешного чтения и возврата списка транзакций.
    """
    mock_data = '[{"amount": 100.5, "currency": "USD", "date": "2024-03-01", "description": "Оплата подписки"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")

    expected = [{"amount": 100.5, "currency": "USD", "date": "2024-03-01", "description": "Оплата подписки"}]
    assert result == expected


def test_read_json_invalid():
    """
    Тест для проверки обработки ошибки при некорректном содержимом файла.
    """
    with patch("builtins.open", mock_open(read_data="not a json")):
        result = read_json("data/operations.json")
    # Ожидаем пустой список, так как JSON некорректен
    assert result == []


def test_read_json_not_a_list():
    """
    Тест для проверки ситуации, когда содержимое файла не является списком.
    """
    # Мокаем данные, которые не являются списком (это словарь, а не список)
    mock_data = '{"amount": 100.0, "currency": "RUB", "date": "2024-03-02", "description": "Перевод другу"}'  # Это словарь, а не список
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
    # Ожидаем пустой список, так как это не список
    assert result == []


def test_file_not_found():
    """
    Тест для проверки ситуации, когда файл не существует.
    """
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json("data/non_existent_file.json")
    # Ожидаем пустой список, так как файл не существует
    assert result == []


def test_file_not_a_file():
    """
    Тест для проверки ситуации, когда путь не является файлом.
    """
    with patch("pathlib.Path.exists", return_value=True), patch("pathlib.Path.is_file", return_value=False):
        result = read_json("data/not_a_file.json")
    # Ожидаем пустой список, так как это не файл
    assert result == []
