import pytest

from src.decorators import log


# Пример функции с декоратором
@log()
def add(a: int, b: int) -> int:
    return a + b


@log(filename="test_log.txt")
def subtract(a: int, b: int) -> int:
    return a - b


# Тест успешного выполнения функции с логированием в консоль
def test_log_function_success(capsys: pytest.CaptureFixture) -> None:
    add(3, 5)  # Вызываем функцию
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "Starting function: add" in captured.out  # Проверяем начало
    assert "Function add completed successfully with result: 8" in captured.out  # Проверяем результат


# Тест ошибки в функции с логированием в консоль
def test_log_function_error(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(TypeError):
        add("3", 5)  # Вызываем функцию с ошибкой
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "Function add failed with error" in captured.out  # Проверяем ошибку


# Тест функции с логированием в файл
def test_log_function_with_file() -> None:
    subtract(10, 4)  # Вызываем функцию
    with open("test_log.txt", "r") as file:
        log_content = file.read()  # Читаем содержимое файла
    assert "Starting function: subtract" in log_content  # Проверяем начало
    assert "Function subtract completed successfully with result: 6" in log_content  # Проверяем результат
