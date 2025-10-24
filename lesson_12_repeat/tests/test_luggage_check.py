import random
import sys
import pathlib
import pytest

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from lesson_12_repeat.lesson_12 import luggage_check


# SMOKE TESTS
@pytest.mark.luggage_check_smoketest
def test_luggage_check_smoke_random_datat():
    data = [
        {'number_of_items': random.choice([1, 2, 3, 88, 999]), 'total_weight': random.randint(0, 50)}
        for _ in range(100)
    ]
    result = luggage_check(data)
    assert isinstance(result, tuple)
    assert len(result) == 3


# POSITIVE TESTS
@pytest.mark.luggage_check_positivetests
@pytest.mark.parametrize('data, expected', [
    ([
         {'number_of_items': 1, 'total_weight': 25},
         {'number_of_items': 1, 'total_weight': 24},
         {'number_of_items': 1, 'total_weight': 26},
         {'number_of_items': 2, 'total_weight': 30},
         {'number_of_items': 3, 'total_weight': 35},
         {'number_of_items': 0, 'total_weight': 35}
     ], (1, True, 2)),
    ([
         {'number_of_items': 1, 'total_weight': 25},
         {'number_of_items': 3, 'total_weight': 24},
         {'number_of_items': 1, 'total_weight': 26},
         {'number_of_items': 2, 'total_weight': 30},
         {'number_of_items': 3, 'total_weight': 35},
         {'number_of_items': 0, 'total_weight': 35}
     ], (2, False, 3)),

    ([
         {'number_of_items': 0, 'total_weight': 25},
         {'number_of_items': 0, 'total_weight': 24},
         {'number_of_items': 0, 'total_weight': 26},
         {'number_of_items': 0, 'total_weight': 30},
         {'number_of_items': 0, 'total_weight': 35},
         {'number_of_items': 0, 'total_weight': 35}
     ], (0, False, 0)),
    ([
         {'number_of_items': 9000, 'total_weight': 25},

     ], (1, False, 0)),

])
def test_luggage_check_returns_filtered_tuples(data, expected):
    actual = luggage_check(data)
    assert actual == expected


# EDGE TESTS (Boundary or minimal values)
# ============================================================

@pytest.mark.luggage_check_edgetests
@pytest.mark.parametrize("data, expected", [
    ([{'number_of_items': 0, 'total_weight': 25},
      {'number_of_items': 0, 'total_weight': 24},
      {'number_of_items': 0, 'total_weight': 26},
      ],
     (0, False, 0)),

    (
            [{'number_of_items': 99999, 'total_weight': 25}],
            (1, False, 0)
    ),
])
def test_luggage_check_handles_edge_cases(data, expected):
    """Tests extreme but valid inputs (zeros, very large numbers)."""
    actual = luggage_check(data)
    assert actual == expected


#  NEGATIVE TESTS
@pytest.mark.luggage_check_negativetests
def test_luggage_check_raises_type_error_for_non_list_input():
    data = {'number_of_items': 99, 'total_weight': 25}
    with pytest.raises(TypeError):
        luggage_check(data)


@pytest.mark.parametrize('data', [
    ([{'number_of_items': None, 'total_weight': 25}]),
    ([{'number_of_items': '77', 'total_weight': 25}]),
    ([{'total_weight': 25}]),
    ([{}]),
    ([]),
    ([{'number_of_items': '77', 'total_weight': '25'}])
])
def test_luggage_check_handles_invalid_entries(data):
    with pytest.raises(ValueError):
        luggage_check(data)
