import pytest

from src.decorators import log


# Пример теста для функции без ошибок
@log()
def add(a: int, b: int) -> int:
    return a + b


def test_log_function_success(capsys: pytest.CaptureFixture) -> None:
    add(3, 5)  # Вызываем функцию
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "Starting function: add" in captured.out  # Проверяем начало в stdout
    assert "Function add completed successfully with result: 8" in captured.out


# Пример теста для функции с ошибкой
@log()
def faulty_add(a: int, b: int) -> int:
    return a + b


def test_log_function_error(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(TypeError):
        faulty_add(3, "5")  # Вызываем функцию с ошибкой
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "Starting function: faulty_add" in captured.out  # Проверяем начало в stdout
    assert "Function faulty_add failed with error:" in captured.out  # Проверяем ошибку
