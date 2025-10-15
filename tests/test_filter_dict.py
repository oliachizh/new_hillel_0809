import unittest
import sys
import pathlib
import pytest
import os



sys.path.append(str(pathlib.Path(__file__).parent.parent))
from functions import filter_dict
from core.asserts.sum_numbers_asserts import assert_filter_dict
current_env = os.getenv("ENVIRONMENT", "prod")
@pytest.mark.xfail
class TestFilterDictPositive(unittest.TestCase):
    def test_filter_dict_positive(self):
        d = {"a": 5, "b": 6, "c": 4}
        threshold = 6
        expected = {"a": 5, "b": 6}
        assert_filter_dict(d, threshold, expected)

@pytest.mark.skipif(current_env != "dev", reason="only works on dev environment")
class TestFilterDictNegative(unittest.TestCase):
    def test_filter_dict_positive(self):
        d = {"a": 5, "b": 6, "c": 4}
        thread = '4'
        with self.assertRaises(TypeError):
            filter_dict(d, thread)
