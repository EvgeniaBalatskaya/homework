from unittest.mock import MagicMock, patch

import pytest

from src.main import main


@pytest.fixture
def mock_input():
    """Мок для input() с возвратом нужных значений для теста."""
    # Список всех необходимых ответов на запросы input в main()
    responses = [
        "1",  # JSON-файл
        "test.json",  # Путь к JSON файлу
        "EXECUTED",  # Фильтр по статусу
        "да",  # Сортировка
        "по убыванию",  # Направление сортировки
        "нет",  # Только RUB
        "нет",  # Фильтр по описанию
        "нет",  # Выход из программы
        "4"  # Ответ на запрос выбора в меню "Выйти"
    ]
    return responses


@pytest.fixture
def mock_transactions():
    """Тестовые данные транзакций."""
    return [
        {
            "date": "2024-01-10T15:30:00",
            "description": "Покупка кофе",
            "amount": "300",
            "currency": "RUB",
            "from": "Карта 1234",
            "to": "Кофейня",
            "status": "EXECUTED",
        },
        {
            "date": "2024-02-15T10:00:00",
            "description": "Перевод зарплаты",
            "amount": "50000",
            "currency": "RUB",
            "from": "Работодатель",
            "to": "Карта 5678",
            "status": "EXECUTED",
        },
    ]


@pytest.fixture
def mock_file_readers(mock_transactions):
    """Моки для функций чтения файлов."""
    with patch("src.main.read_json", return_value=mock_transactions):
        with patch("src.main.read_csv_transactions", return_value=mock_transactions):
            with patch("src.main.read_excel_transactions", return_value=mock_transactions):
                yield


def test_main_json_input(mock_input, mock_file_readers, capsys):
    """Тест на корректную работу main() с JSON-файлом."""
    with patch("builtins.input", side_effect=mock_input):
        with patch("src.main.filter_transactions_by_description", side_effect=lambda x, y: x):
            main(test_mode=True, test_inputs=mock_input)

    captured = capsys.readouterr()
    assert "Привет! Добро пожаловать в программу работы с банковскими транзакциями." in captured.out
    assert "Распечатываю итоговый список транзакций..." in captured.out
    assert "Всего банковских операций в выборке: 2" in captured.out
    assert "Покупка кофе" in captured.out
    assert "Перевод зарплаты" in captured.out
