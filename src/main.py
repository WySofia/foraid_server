import math
from typing import List

from src.errors.custom_error import CustomError, ErrorTag, handle_error
from src.errors.result import Err, Ok, Result, map_result


def add(x: int, y: int) -> int:
    return x + y


def is_even(x: int) -> bool:
    return x % 2 == 0


def safe_div(a: float, b: float) -> Result[float, CustomError]:
    if b == 0:
        return Err(handle_error(ErrorTag.LOGIC_ERROR, "No division by zero"))
    return Ok(a / b)
