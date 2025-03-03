import logging

from functools import wraps
from typing import Any, Callable


# Настройка логирования
logging.basicConfig(level=logging.INFO)


def log() -> Callable[[Any], Any]:  # Декоратор принимает функцию и возвращает функцию
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:  # Типы для декорируемой функции
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:  # Типы для оборачиваемой функции
            logging.info(f"Starting function: {func.__name__} with arguments {args} and kwargs {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"Function {func.__name__} completed successfully with result: {result}")
                return result
            except Exception as e:
                logging.error(f"Function {func.__name__} failed with error: {e}. Arguments: {args}, {kwargs}")
                raise e

        return wrapper

    return decorator
