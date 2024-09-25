import pytest
from src.errors.custom_error import (
    ErrorTag,
    LogicError,
    DataError,
    UnknownError,
    create_error,
    handle_error,
)


def test_create_logic_error():
    message = "Logical inconsistency detected"
    error = create_error(ErrorTag.LOGIC_ERROR, message)
    assert isinstance(error, LogicError)
    assert error.tag == ErrorTag.LOGIC_ERROR
    assert error.message == message


def test_create_data_error():
    message = "Data processing failed"
    error = create_error(ErrorTag.DATA_ERROR, message)
    assert isinstance(error, DataError)
    assert error.tag == ErrorTag.DATA_ERROR
    assert error.message == message


def test_create_unknown_error():
    message = "An unexpected error occurred"
    error = create_error(ErrorTag.UNKNOWN_ERROR, message)
    assert isinstance(error, UnknownError)
    assert error.tag == ErrorTag.UNKNOWN_ERROR
    assert error.message == message


def test_handle_error_logic_error():
    error_input = ValueError("Division by zero")
    error = handle_error(ErrorTag.LOGIC_ERROR, error_input)
    assert isinstance(error, LogicError)
    assert error.message == f"Error in logical operations: {error_input}"


def test_handle_error_data_error():
    error_input = ValueError("Empty data list")
    error = handle_error(ErrorTag.DATA_ERROR, error_input)
    assert isinstance(error, DataError)
    assert error.message == f"Error in data processing: {error_input}"


def test_handle_error_unknown_error_with_exception():
    error_input = ValueError("Invalid value")
    error = handle_error(ErrorTag.UNKNOWN_ERROR, error_input)
    assert isinstance(error, UnknownError)
    assert error.message == f"Unknown error: {str(error_input)}"


def test_handle_error_unknown_error_with_non_exception():
    error_input = {"error": "Something went wrong"}
    error = handle_error(ErrorTag.UNKNOWN_ERROR, error_input)
    assert isinstance(error, UnknownError)
    assert error.message == "Unknown error: An unknown error occurred."
