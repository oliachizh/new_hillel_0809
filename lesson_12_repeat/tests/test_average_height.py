import pytest
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from lesson_12_repeat.lesson_12 import average_height


@pytest.mark.parametrize("people_data, expected_result", [
    ({
    'person1': {'gender': 'Male', 'height': 175},
    'person2': {'gender': 'Female', 'height': 160},
    'person3': {'gender': 'Male', 'height': 180}

}, 171.67),
({
    'person1': {'gender': 'Male', 'height': 175}

}, 175),
    ({
    'person1': {'gender': 'Male', 'height': '175.6'},
    'person2': {'gender': 'Female', 'height': 160},
    'person3': {'gender': 'Male', 'height': 180}

}, 171.87)
])
def test_average_height_for_valid_input(people_data, expected_result):
    actual_height = average_height(people_data)
    assert actual_height == expected_result

def test_average_height_for_empty_dict():
    result = average_height({})
    assert result is None

def test_average_height_missing_height():
    data = {
        'person1': {'gender': 'Male'},
        'person2': {'gender': 'Female'},
        'person3': {'gender': 'Male'}

    }
    result = average_height(data)
    assert result is None

def test_average_height_for_none():
    height_data = {
        'person1': {'gender': 'Male', 'height': None},
        'person2': {'gender': 'Female', 'height': None},
        'person3': {'gender': 'Male', 'height': None}

    }
    result = average_height(height_data)
    assert result is None

