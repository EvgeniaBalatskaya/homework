import logging  # Добавляем импорт
import pytest
from src.decorators import add, faulty_add

def test_log_function_success(caplog: pytest.CaptureFixture) -> None:
    with caplog.at_level(logging.DEBUG):  # Устанавливаем уровень логирования
        add(3, 5)  # Вызываем функцию

    # Проверяем, что в логах есть нужная информация
    assert "Starting function: add" in caplog.text
    assert "add ok" in caplog.text

def test_log_function_error(caplog: pytest.CaptureFixture) -> None:
    with caplog.at_level(logging.DEBUG):  # Устанавливаем уровень логирования
        with pytest.raises(TypeError):
            faulty_add(3, '5')  # Вызываем функцию с ошибкой

    # Проверяем, что в логах есть нужная информация
    assert "Starting function: faulty_add" in caplog.text
    assert "faulty_add error" in caplog.text
