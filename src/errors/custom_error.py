from dataclasses import dataclass
from typing import Union
from typing import Any
from enum import Enum


class ErrorTag(Enum):
    VALIDATION_ERROR = "ValidationError"
    LOGIC_ERROR = "LogicError"
    DATA_ERROR = "DataError"
    API_ERROR = "ApiError"
    UNKNOWN_ERROR = "UnknownError"


@dataclass
class ValidationError:
    tag: ErrorTag = ErrorTag.VALIDATION_ERROR
    message: str = "Error validating fields types"


@dataclass
class LogicError:
    tag: ErrorTag = ErrorTag.LOGIC_ERROR
    message: str = "Error in logical operations"


@dataclass
class DataError:
    tag: ErrorTag = ErrorTag.DATA_ERROR
    message: str = "Error in data processing"


@dataclass
class ApiError:
    tag: ErrorTag = ErrorTag.API_ERROR
    message: str = "Error fetching data"


@dataclass
class UnknownError:
    tag: ErrorTag = ErrorTag.UNKNOWN_ERROR
    message: str = "Unknown error"


CustomError = Union[ValidationError, LogicError, DataError, ApiError, UnknownError]


def create_error(tag: ErrorTag, message: str) -> CustomError:
    error_classes = {
        ErrorTag.VALIDATION_ERROR: ValidationError,
        ErrorTag.LOGIC_ERROR: LogicError,
        ErrorTag.DATA_ERROR: DataError,
        ErrorTag.API_ERROR: ApiError,
        ErrorTag.UNKNOWN_ERROR: UnknownError,
    }

    error_class = error_classes.get(tag, UnknownError)
    return error_class(message=message)


def handle_error(tag: ErrorTag, error: Any) -> CustomError:
    message = get_error_message(error)

    error_messages = {
        ErrorTag.VALIDATION_ERROR: f"Error validating fields types: {message}",
        ErrorTag.LOGIC_ERROR: f"Error in logical operations: {message}",
        ErrorTag.DATA_ERROR: f"Error in data processing: {message}",
        ErrorTag.API_ERROR: f"Error fetching data: {message}",
        ErrorTag.UNKNOWN_ERROR: f"Unknown error: {message}",
    }

    error_message = error_messages.get(tag, f"Unknown error: {message}")
    return create_error(tag, error_message)


def get_error_message(error: Any) -> str:
    return str(error) if isinstance(error, Exception) else "An unknown error occurred."
