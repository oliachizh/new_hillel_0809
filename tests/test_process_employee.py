import unittest
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from functions import process_employees
from core.asserts.sum_numbers_asserts import assert_filtered_scores

class TestProcessEmployeePositive(unittest.TestCase):
    def test_returns_filtered_results(self):
        employees = {"Alice": 2500, "Bob": 4000, "Charlie": 6000}
        actual = process_employees(employees, min_salary=3000, bonus_rate=0.2)
        expected = {"Bob": 4800.0, 'Charlie': 7200.0}
        self.assertEqual(actual, expected)