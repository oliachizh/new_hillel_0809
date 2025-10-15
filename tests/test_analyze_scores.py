import unittest
import sys
import pathlib
import pytest

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from functions import analyze_scores
from core.asserts.sum_numbers_asserts import assert_filtered_scores

@pytest.mark.analyze_scores
@pytest.mark.positive
class TestAnalyzeScoresPositive:
    @pytest.mark.parametrize('expected, pass_mark', [
        pytest.param({'CHARLIE': 700, 'DIANA': 950}, None, marks=pytest.mark.xfail(reason='known issue')),
        pytest.param({'CHARLIE': 700, 'DIANA': 950}, 10),


    ], ids=['pass_mark=default', 'pass_mark=10'])
    def test_returns_filterd_results_default_pass_mark(self, expected, pass_mark):
        students = {"Alice": 9, "Bob": 10, "Charlie": 70, "Diana": 95}
        actual = analyze_scores(students)
        assert expected == actual

    # def test_returns_filtered_dict_and_custom_pass_mark(self):
    #     students = {"Alice": 9, "Bob": 10, "Charlie": 70, "Diana": 95}
    #     expected = {'BOB': 100, 'CHARLIE': 700, 'DIANA': 950}
    #     actual = analyze_scores(students, pass_mark=10)
    #     assert expected == actual

class TestAnalyzeScoresNegative(unittest.TestCase):
    def setUp(self):
        self.students = {"Alice": 9, "Bob": 10, "Charlie": 70, "Diana": 95}
        self.pass_mark = '10'

    def test_returns_type_error_for_invalid_pass_mark(self):
        with self.assertRaises(TypeError):
            analyze_scores(self.students, pass_mark=self.pass_mark)

    def test_returns_value_error_for_empty_dict(self):
        students = {}
        with self.assertRaises(ValueError):
            analyze_scores(students)






