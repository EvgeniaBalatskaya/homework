import unittest
from src.processing import filter_by_state, sort_by_date


class TestProcessingFunctions(unittest.TestCase):
    def test_filter_by_state(self):
        data = [
            {"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2021-06-02T14:00:00"},
        ]
        result = filter_by_state(data, "EXECUTED")
        self.assertEqual(result, [{"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"}])

    def test_sort_by_date(self):
        data = [
            {"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2021-06-02T14:00:00"},
        ]
        result = sort_by_date(data)
        self.assertEqual(
            result,
            [
                {"id": 2, "state": "CANCELED", "date": "2021-06-02T14:00:00"},
                {"id": 1, "state": "EXECUTED", "date": "2021-06-01T14:00:00"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
