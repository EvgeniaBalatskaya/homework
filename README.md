# Проект "Homework"

## Описание

Проект **"Homework"** — это виджет на **Python** для обработки банковских операций клиента.  
Он позволяет фильтровать и сортировать данные о транзакциях, следуя принципам **GitFlow** и стандартам **PEP 8**.  

## Функциональность

- Фильтрация операций по статусу (`EXECUTED`, `CANCELED` и т. д.).
- Сортировка операций по дате.
- Поддержка аннотаций типов, линтеров (`Flake8`, `mypy`, `isort`).
- Разработка по **GitFlow** с атомарными коммитами.

## Установка и запуск

### 1. Клонируйте репозиторий:

git clone https://github.com/EvgeniaBalatskaya/homework.git

### 2. Перейдите в директорию проекта:

cd homework

### 3. Установите зависимости:

poetry install

## Использование  

В проекте есть основные модули:

processing.py — фильтрация и сортировка операций.
masks.py — маскировка номеров карт и счетов.
widget.py — основной виджет.
tests/ — тесты для проверки логики.

## Документация
Подробности о модулях и API можно найти в файлах кода и в комментариях.

## Лицензия
Проект распространяется под лицензией MIT.


