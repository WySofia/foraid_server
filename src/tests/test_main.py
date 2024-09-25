import pytest

from src.main import add, is_even


@pytest.mark.parametrize("input_x, input_y, expected", [(1, 2, 3)])
def test_add(input_x, input_y, expected):
    assert add(input_x, input_y) == expected


@pytest.mark.parametrize("input_x, expected", [(1, False), (2, True)])
def test_is_even(input_x, expected):
    assert is_even(input_x) == expected
