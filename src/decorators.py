import functools
import logging

from typing import Callable, Optional


# Декоратор с точными аннотациями типов
def log(filename: Optional[str] = None) -> Callable[[Callable[..., int]], Callable[..., int]]:
    """
    Декоратор для логирования выполнения функций
    """

    def decorator(func: Callable[..., int]) -> Callable[..., int]:
        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> int:
            # Настройка логирования
            log_handler = logging.StreamHandler() if filename is None else logging.FileHandler(filename)
            logging.basicConfig(level=logging.DEBUG, handlers=[log_handler], format="%(message)s")

            # Логируем начало выполнения функции
            logging.debug(f"Starting function: {func.__name__} with arguments {args} and kwargs {kwargs}")

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное выполнение
                logging.debug(f"{func.__name__} ok")
                return result
            except Exception as e:
                # Логируем ошибку
                logging.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


# Функция add с аннотациями
@log()  # Применяем декоратор
def add(a: int, b: int) -> int:
    """
    Функция для сложения двух чисел
    """
    return a + b


# Функция faulty_add с аннотациями
@log()  # Применяем декоратор
def faulty_add(a: int, b: int) -> int:
    """
    Функция для сложения двух чисел с возможной ошибкой
    """
    return a + b
