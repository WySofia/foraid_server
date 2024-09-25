from typing import Generic, TypeVar, Callable, Any

from src.errors.custom_error import CustomError, ErrorTag, handle_error

T = TypeVar("T")
E = TypeVar("E", bound=CustomError)


class Result(Generic[T, E]):
    pass


class Ok(Result[T, E]):
    def __init__(self, value: T):
        self.value = value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"Ok({self.value})"


class Err(Result[T, E]):
    def __init__(self, error: E):
        self.error = error

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def unwrap_err(self) -> E:
        return self.error

    def __repr__(self) -> str:
        return f"Err({self.error})"


def ok(value: T) -> Ok[T, Any]:
    return Ok(value)


def err(error: E) -> Err[Any, E]:
    return Err(error)


def map_result(result: Result[T, E], func: Callable[[T], Any]) -> Result[Any, E]:
    if isinstance(result, Ok):
        try:
            return Ok(func(result.value))
        except Exception as e:
            return Err(handle_error(ErrorTag.LOGIC_ERROR, e))
    else:
        return result


def map_err_result(result: Result[T, E], func: Callable[[E], Any]) -> Result[T, Any]:
    if isinstance(result, Err):
        try:
            return Err(func(result.error))
        except Exception as e:
            return Err(handle_error(ErrorTag.LOGIC_ERROR, e))
    else:
        return result
