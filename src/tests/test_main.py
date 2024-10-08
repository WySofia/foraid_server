import pytest
from src.errors.custom_error import LogicError
from src.errors.result import Err, Ok
from src.main import add, is_even, safe_div


@pytest.mark.parametrize("input_x, input_y, expected", [(1, 2, 3)])
def test_add(input_x, input_y, expected):
    assert add(input_x, input_y) == expected


@pytest.mark.parametrize("input_x, expected", [(1, False), (2, True)])
def test_is_even(input_x, expected):
    assert is_even(input_x) == expected


def test_safe_div_success():
    result = safe_div(10, 2)
    assert isinstance(result, Ok)
    assert result.unwrap() == 5.0


def test_safe_div_division_by_zero():
    result = safe_div(10, 0)
    assert isinstance(result, Err)
    assert isinstance(result.unwrap_err(), LogicError)
    assert "No division by zero" in result.unwrap_err().message
