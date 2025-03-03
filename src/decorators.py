import functools
import logging
from typing import Optional, Callable

# Декоратор log должен быть определен до использования
def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Настройка логирования
            log_handler = logging.StreamHandler() if filename is None else logging.FileHandler(filename)
            logging.basicConfig(level=logging.DEBUG, handlers=[log_handler], format='%(message)s')

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

# Теперь можно использовать декоратор
@log()  # Применяем декоратор
def add(a: int, b: int) -> int:
    return a + b

# В случае ошибки определение faulty_add функции
@log()
def faulty_add(a: int, b: int) -> int:
    return a + b  # Эта функция будет вызывать ошибку при попытке сложить int и str