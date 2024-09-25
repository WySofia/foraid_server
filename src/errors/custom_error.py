from dataclasses import dataclass
from typing import Union
from typing import Any
from enum import Enum


class ErrorTag(Enum):
    LOGIC_ERROR = "LogicError"
    DATA_ERROR = "DataError"
    UNKNOWN_ERROR = "UnknownError"


@dataclass
class LogicError:
    tag: ErrorTag = ErrorTag.LOGIC_ERROR
    message: str = "Error in logical operations"


@dataclass
class DataError:
    tag: ErrorTag = ErrorTag.DATA_ERROR
    message: str = "Error in data processing"


@dataclass
class UnknownError:
    tag: ErrorTag = ErrorTag.UNKNOWN_ERROR
    message: str = "Unknown error"


CustomError = Union[LogicError, DataError, UnknownError]


def create_error(tag: ErrorTag, message: str) -> CustomError:
    error_classes = {
        ErrorTag.LOGIC_ERROR: LogicError,
        ErrorTag.DATA_ERROR: DataError,
        ErrorTag.UNKNOWN_ERROR: UnknownError,
    }

    error_class = error_classes.get(tag, UnknownError)
    return error_class(message=message)


def handle_error(tag: ErrorTag, error: Any) -> CustomError:
    message = get_error_message(error)

    error_messages = {
        ErrorTag.LOGIC_ERROR: f"Error in logical operations: {message}",
        ErrorTag.DATA_ERROR: f"Error in data processing: {message}",
        ErrorTag.UNKNOWN_ERROR: f"Unknown error: {message}",
    }

    error_message = error_messages.get(tag, f"Unknown error: {message}")
    return create_error(tag, error_message)


def get_error_message(error: Any) -> str:
    if isinstance(error, Exception):
        return str(error)
    elif isinstance(error, str):
        return error
    else:
        return "An unknown error occurred."
