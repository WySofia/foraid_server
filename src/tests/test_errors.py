from typing import Any
from src.errors.custom_error import (
    ApiError,
    DataError,
    ErrorTag,
    LogicError,
    ValidationError,
    create_error,
    handle_error,
)
from src.errors.result import Err, Ok, Result, err, map_err_result, map_result, ok
from src.main import safe_div, safe_sqrt
import math


def test_create_error_validation_error():
    message = "Invalid input data"
    error = create_error(ErrorTag.VALIDATION_ERROR, message)
    assert isinstance(error, ValidationError)
    assert error.tag == ErrorTag.VALIDATION_ERROR
    assert error.message == message


def test_create_error_logic_error():
    message = "Logical inconsistency detected"
    error = create_error(ErrorTag.LOGIC_ERROR, message)
    assert isinstance(error, LogicError)
    assert error.tag == ErrorTag.LOGIC_ERROR
    assert error.message == message


def test_create_error_data_error():
    message = "Data processing failed"
    error = create_error(ErrorTag.DATA_ERROR, message)
    assert isinstance(error, DataError)
    assert error.tag == ErrorTag.DATA_ERROR
    assert error.message == message


def test_create_error_api_error():
    message = "API endpoint not reachable"
    error = create_error(ErrorTag.API_ERROR, message)
    assert isinstance(error, ApiError)
    assert error.tag == ErrorTag.API_ERROR
    assert error.message == message


def test_handle_error_validation_error():
    error_message = "Missing required fields"
    error = handle_error(ErrorTag.VALIDATION_ERROR, error_message)
    assert isinstance(error, ValidationError)
    assert error.message == f"Error validating fields types with Zod: {error_message}"


def test_handle_error_logic_error():
    error_message = "No se puede dividir por cero"
    error = handle_error(ErrorTag.LOGIC_ERROR, error_message)
    assert isinstance(error, LogicError)
    assert error.message == f"Error in logical operations: {error_message}"


def test_handle_error_unknown_error():
    error_message = "Unknown error type"
    error = handle_error(ErrorTag.DATA_ERROR, error_message)
    assert isinstance(error, DataError)
    assert error.message == f"Error in data processing: {error_message}"


def test_result_ok():
    value = 42
    result: Result[int, Any] = ok(value)
    assert isinstance(result, Ok)
    assert result.is_ok()
    assert not result.is_err()
    assert result.unwrap() == value


def test_result_err():
    from src.errors import DataError

    error = DataError(message="Data not found")
    result: Result[Any, DataError] = err(error)
    assert isinstance(result, Err)
    assert result.is_err()
    assert not result.is_ok()
    assert result.unwrap_err() == error


def test_map_result_success():
    result = ok(10)
    mapped_result = map_result(result, lambda x: x * 2)
    assert isinstance(mapped_result, Ok)
    assert mapped_result.unwrap() == 20


def test_map_result_failure():
    result: Result[int, Any] = err(LogicError(message="Initial logic error"))
    mapped_result = map_result(result, lambda x: x * 2)
    assert isinstance(mapped_result, Err)
    assert mapped_result.unwrap_err().message == "Initial logic error"


def test_map_result_exception():
    def faulty_func(x):
        raise ValueError("Faulty function error")

    result = ok(5)
    mapped_result = map_result(result, faulty_func)
    assert isinstance(mapped_result, Err)
    assert isinstance(mapped_result.unwrap_err(), LogicError)
    assert "Faulty function error" in mapped_result.unwrap_err().message


def test_map_err_result_success():
    error = DataError(message="Initial data error")
    result: Result[Any, DataError] = err(error)

    def transform_error(e):
        return handle_error(ErrorTag.DATA_ERROR, "Transformed error message")

    mapped_result = map_err_result(result, transform_error)
    assert isinstance(mapped_result, Err)
    assert isinstance(mapped_result.unwrap_err(), DataError)
    assert (
        mapped_result.unwrap_err().message
        == "Error in data processing: Transformed error message"
    )


def test_map_err_result_exception():
    error = DataError(message="Initial data error")
    result: Result[Any, DataError] = err(error)

    def faulty_transform(e):
        raise RuntimeError("Faulty transform")

    mapped_result = map_err_result(result, faulty_transform)
    assert isinstance(mapped_result, Err)
    assert isinstance(mapped_result.unwrap_err(), LogicError)
    assert "Faulty transform" in mapped_result.unwrap_err().message


def test_safe_div():
    result = safe_div(10, 2)
    assert isinstance(result, Ok)
    assert math.isclose(result.unwrap(), 5.0, rel_tol=1e-9)


def test_dividir_por_cero():
    result = safe_div(10, 0)
    assert isinstance(result, Err)
    assert isinstance(result.unwrap_err(), LogicError)
    assert "No se puede dividir por cero" in result.unwrap_err().message


def test_raiz_cuadrada_exitosa():
    result = safe_sqrt(16)
    assert isinstance(result, Ok)
    assert math.isclose(result.unwrap(), 4.0, rel_tol=1e-9)


def test_raiz_cuadrada_negativa():
    result = safe_sqrt(-4)
    assert isinstance(result, Err)
    assert isinstance(result.unwrap_err(), ValidationError)
    assert "Raíz cuadrada de número negativo" in result.unwrap_err().message
