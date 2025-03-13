import pandas as pd

from file_processing.reader import read_csv_transactions, read_excel_transactions
from file_processing.utils import read_json


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Выбор пользователем формата файла
    choice = input("Введите номер выбранного пункта: ")

    # Моки для чтения файлов
    if choice == "1":
        transactions = read_json("transactions.json")  # Убедитесь, что функция для JSON есть
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = read_csv_transactions("transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = read_excel_transactions("transactions.xlsx")
        print("Для обработки выбран Excel-файл.")
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Ошибка: Нет транзакций для обработки.")
        return

    # Печать всех транзакций, полученных из файла
    print(f"Всего операций: {len(transactions)}")
    print(transactions)

    # Фильтрация по статусу
    status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while status not in valid_statuses:
        print(f"Статус операции '{status}' недоступен.")
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()

    filtered_transactions = [tx for tx in transactions if tx.get("status", "").upper() == status]
    print(f"Операции отфильтрованы по статусу '{status}'.")

    # Дополнительная фильтрация по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        sort_order = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        if sort_order == "по возрастанию":
            filtered_transactions.sort(key=lambda x: pd.to_datetime(x["date"]), reverse=False)
            print("Операции отсортированы по дате по возрастанию.")
        elif sort_order == "по убыванию":
            filtered_transactions.sort(key=lambda x: pd.to_datetime(x["date"]), reverse=True)
            print("Операции отсортированы по дате по убыванию.")
        else:
            print("Некорректный ввод. Сортировка не будет выполнена.")

    # Фильтрация по валюте (например, рубли)
    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [tx for tx in filtered_transactions if tx.get("currency", "").upper() == "RUB"]
        print("Операции отфильтрованы по валюте 'RUB'.")

    # Фильтрация по слову в описании
    description_choice = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_choice == "да":
        word = input("Введите слово для фильтрации: ").strip().lower()
        filtered_transactions = [tx for tx in filtered_transactions if word in tx.get("description", "").lower()]

    # Печать итогового списка транзакций
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for tx in filtered_transactions:
            print(f"{tx['date']} {tx['description']}")
            print(f"Сумма: {tx['amount']} {tx['currency']}")
            print(f"Счет: {tx['from_account']} -> {tx['to_account']}")
            print("-" * 40)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
