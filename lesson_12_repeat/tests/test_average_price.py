import sys
import pathlib

import pytest

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from lesson_12_repeat.lesson_12 import average_price



@pytest.mark.parametrize("data, expected_price", [
    ([{"name": "Space", "volume": 20000, "price": 10},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Fortune", "volume": 9999, "price": 17.99},
    {"name": "Vouge", "volume": 25000, "price": 12.99}], 11.5),

    ([{"name": "Space", "volume": 20000, "price": 0}], 0.0),
    ([{"name": "Space", "volume": 20000, "price": 0},
      {"name": "SeaSide", "volume": 5000, "price": 0},
      {"name": "Fortune", "volume": 9999, "price": 0},
      {"name": "Vouge", "volume": 10001, "price": 12.99}], 6.5)
])
def test_average_price_filters_and_returns_valid_value(data, expected_price):
    actual = average_price(data)
    assert actual == expected_price

def test_average_price_with_none_price():
    data = [{"name": "Space", "volume": 20000, "price": None},
    {"name": "SeaSide", "volume": 5000, "price": None},
    {"name": "Fortune", "volume": 9999, "price": 17.99},
    {"name": "Vouge", "volume": 25000, "price": 10.00}]
    actual = average_price(data)
    assert actual == 5.0

def test_average_price_with_missing_price():
    data = [{"name": "Space", "volume": 20000},
    {"name": "SeaSide", "volume": 5000},
    {"name": "Fortune", "volume": 10000, "price": 17.99},
    {"name": "Fortune", "volume": 9999, "price": 17.99},
    {"name": "Vouge", "volume": 10001, "price": 10.00}]
    actual = average_price(data)
    assert actual == 9.33

def test_average_price_with_volume_less_10000():
    data = [{"name": "Space", "volume": 9999, "price": 10000},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Fortune", "volume": 8999, "price": 17.99},
    {"name": "Fortune", "volume": 9999, "price": 17.99},
    {"name": "Vouge", "volume": 8000, "price": 10.00}]
    with pytest.raises(ValueError) as e:
        average_price(data)


def test_average_price_with_empty_data():
    data = []
    with pytest.raises(ValueError):
        average_price(data)

def test_average_price_with_invalid_price():
    data = [{"name": "Space", "volume": 20000, "price": 'p'},
            {"name": "SeaSide", "volume": 5000},
            {"name": "Fortune", "volume": 10000, "price": 17.99},
            {"name": "Fortune", "volume": 9999, "price": 17.99},
            {"name": "Vouge", "volume": 10001, "price": 10.00}]
    with pytest.raises(ValueError):
        average_price(data)