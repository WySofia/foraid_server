from typing import Any
from src.errors.custom_error import LogicError, DataError, ErrorTag, handle_error
from src.errors.result import Result, Ok, Err, ok, err, map_result, map_err_result


def test_ok_creation():
    value = 100
    result: Result[int, LogicError] = ok(value)
    assert isinstance(result, Ok)
    assert result.is_ok() is True
    assert result.is_err() is False
    assert result.unwrap() == value
    assert repr(result) == f"Ok({value})"


def test_err_creation():
    error = LogicError(message="Invalid operation")
    result: Result[Any, LogicError] = err(error)
    assert isinstance(result, Err)
    assert result.is_err() is True
    assert result.is_ok() is False
    assert result.unwrap_err() == error
    assert repr(result) == f"Err({error})"


def test_map_result_success():
    original = ok(25)
    mapped = map_result(original, lambda x: x * 2)
    assert isinstance(mapped, Ok)
    assert mapped.unwrap() == 50


def test_map_result_failure():
    original_error = LogicError(message="Original error")
    original = err(original_error)
    mapped = map_result(original, lambda x: x * 2)
    assert isinstance(mapped, Err)
    assert mapped.unwrap_err() == original_error


def test_map_result_exception_handling():
    def faulty_function(x):
        raise ValueError("Function failed")

    original = ok(10)
    mapped = map_result(original, faulty_function)
    assert isinstance(mapped, Err)
    assert isinstance(mapped.unwrap_err(), LogicError)
    assert "Function failed" in mapped.unwrap_err().message


def test_map_err_result_success():
    original_error = DataError(message="Initial data error")
    original = err(original_error)

    def transform_error(e):
        return handle_error(
            ErrorTag.DATA_ERROR, ValueError("Transformed error message")
        )

    mapped = map_err_result(original, transform_error)
    assert isinstance(mapped, Err)
    assert isinstance(mapped.unwrap_err(), DataError)
    assert (
        mapped.unwrap_err().message
        == "Error in data processing: Transformed error message"
    )


def test_map_err_result_exception_handling():
    original_error = DataError(message="Initial data error")
    original = err(original_error)

    def faulty_transform(e):
        raise RuntimeError("Transformation failed")

    mapped = map_err_result(original, faulty_transform)
    assert isinstance(mapped, Err)
    assert isinstance(mapped.unwrap_err(), LogicError)
    assert "Transformation failed" in mapped.unwrap_err().message


def test_map_result_preserves_error():
    original_error = LogicError(message="Sample logic error")
    original = err(original_error)
    mapped = map_result(original, lambda x: x + 1)
    assert isinstance(mapped, Err)
    assert mapped.unwrap_err() == original_error


def test_map_err_result_preserves_ok():
    original = ok(42)

    def transform_error(e):
        return handle_error(ErrorTag.DATA_ERROR, "This should not be called")

    mapped = map_err_result(original, transform_error)
    assert isinstance(mapped, Ok)
    assert mapped.unwrap() == 42
