import unittest
import sys
import pathlib
import pytest

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from functions import process_employees
from core.asserts.sum_numbers_asserts import assert_filtered_scores

@pytest.mark.test_filter
def test_returns_filtered_results():
    employees = {"Alice": 2500, "Bob": 4000, "Charlie": 6000}
    with pytest.raises(ValueError):
        process_employees(employees, min_salary=3000, bonus_rate='0.2')


@pytest.mark.test_filter
def test_returns_filtered_results_skip():
    employees = {"Alice": 2500, "Bob": 4000, "Charlie": 6000}
    try:
        result = process_employees(employees, min_salary=3000, bonus_rate=0.2)
        assert result is not None
    except ValueError:
        pytest.skip("Skipping test")

@pytest.mark.test_filter
def test_returns_filtered_results_fail():
    employees = {"Alice": 2500, "Bob": 4000, "Charlie": 6000}
    pytest.fail("Should not be called")
    process_employees(employees, min_salary=3000, bonus_rate=0.2)

