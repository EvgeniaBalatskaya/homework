import logging

import pytest

from src.decorators import add, faulty_add


# Тестирование функции, которая должна завершиться успешно
def test_log_function_success(caplog: pytest.LogCaptureFixture) -> None:
    # Устанавливаем уровень логирования и перехватываем вывод
    with caplog.at_level(logging.DEBUG):
        add(3, 5)  # Вызываем функцию

    # Проверяем, что в логах есть нужная информация
    assert "Starting function: add" in caplog.text
    assert "add ok" in caplog.text


# Тестирование функции, которая вызывает ошибку
def test_log_function_error(caplog: pytest.LogCaptureFixture) -> None:
    # Устанавливаем уровень логирования и перехватываем вывод
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(TypeError):
            faulty_add(3, "5")  # Вызываем функцию с ошибкой

    # Проверяем, что в логах есть нужная информация
    assert "Starting function: faulty_add" in caplog.text
    assert "faulty_add error" in caplog.text
