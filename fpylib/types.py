from typing import Any, TypeVar

_T = TypeVar("_T")
_S = TypeVar("_S")


def is_number(val: Any) -> bool:
    """
    Check if a value is a number.
    """
    return isinstance(val, (int, float, complex))


number = TypeVar("number", int, float, complex)
number.__doc__ = "It is type variable, and it can be int, float or a complex"
