import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
from functions import filter_dict

def assert_sum_all_int_numbers(actual, expected):
    assert actual == expected, f'Actual: {actual}, Expected: {expected}'

def assert_filtered_scores(expected, actual):
    # expected = {'BOB': 420, 'CHARLIE': 700, 'DIANA': 950}
    # actual = analyze_scores(self.students, pass_mark=self.pass_mark)
    for key, value in expected.items():
        assert key in actual, f'Expected: {key} not found in actual: {actual}'
        assert value in actual.values(), f'Value: {value} not found in actual: {actual}'



def assert_filter_dict(d, threshold, expected):
    actual = filter_dict(d, threshold)
    assert actual == expected, f'Actual: {actual}, Expected: {expected}'



