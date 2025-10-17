import sys
import pathlib
print(pathlib.Path(__file__).parent.parent)
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from functions import factorial
import pytest

@pytest.mark.factorial_custom
@pytest.mark.factorial_positive
def test_factorial_positive_simple():
    assert factorial(-1) == 1

