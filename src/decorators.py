import logging

from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    # Настройка логирования
    logger = logging.getLogger(__name__)

    # Убираем избыточное использование переменной handler
    handler = logging.FileHandler(filename) if filename else logging.StreamHandler()

    # Формат логирования
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"Starting function: {func.__name__} with arguments {args} and kwargs {kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Function {func.__name__} completed successfully with result: {result}")
                return result
            except Exception as e:
                logger.error(f"Function {func.__name__} failed with error: {str(e)}. Arguments: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
