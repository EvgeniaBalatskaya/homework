import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-06-02T14:00:00"},
    ]

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, "EXECUTED")
    assert result == [{"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"}]

def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    assert result == [
        {"id": 2, "state": "CANCELED", "date": "2021-06-02T14:00:00"},
        {"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"},
    ]