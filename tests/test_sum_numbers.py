import unittest
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from lesson_8_exceptions.homework_08 import sum_numbers
from core.asserts.sum_numbers_asserts import assert_sum_all_int_numbers

class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.valid_lst = ['1,2,3,4', '1,2,3,4,50', '1,2,3']
        self.invalid_lst = ['1,2,3,n', '1,2,3']
        self.empty_list = []

    def test_retuens_correct_sum_for_valid_input(self):
        """Should correctly sum all comma-separated integers in the list."""
        actual = sum_numbers(self.valid_lst)
        expected= [10, 60, 6]
        assert_sum_all_int_numbers(actual, expected)

    def test_returns_empty_list_for_empty_input(self):
        """Should raise ValueError when list contains empty strings."""
        actual = sum_numbers(self.empty_list)
        expected= []
        assert_sum_all_int_numbers(actual, expected)


    def test_raises_value_error_for_invalid_input(self):
        """Should raise ValueError when list contains non-numeric values or empty strings."""
        with self.assertRaises(ValueError):
            sum_numbers(self.invalid_lst)
    def test_raises_exeption_for_none_input(self):
        """Should raise ValueError when list contains None values"""
        with self.assertRaises(Exception):
            sum_numbers(None)


if __name__ == '__main__':
    unittest.main()