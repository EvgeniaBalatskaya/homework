import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2022-07-19T15:30:00", "19.07.2022"),
])
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
