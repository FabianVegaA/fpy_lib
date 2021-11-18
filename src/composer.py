from typing import Callable, Any, Tuple
from functools import wraps


def compose(*funcs: Callable[..., Any]) -> Callable[..., Any]:
    """
    Composes two or more functions.

    :funcs: The functions to be composed.
    :return: The composition of the two functions.
    """
    if not funcs:
        raise ValueError("No functions to compose")
    elif len(funcs) == 1:
        return funcs[0]

    @wraps(funcs)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = funcs[0](*args, **kwargs)
        for func in funcs[1:]:
            result = func(result)
        return result

    return wrapper


def parallelize(*funcs: Callable[..., Any]) -> Callable[..., Tuple]:
    """
    Decorator to make a function parallelizable.

    :func: The function to be parallelizable.
    :return: A function that returns the result of the function.
    """

    @wraps(funcs)
    def wrapper(*args: Any, uniqui_intput: bool = True) -> Tuple:
        if not uniqui_intput:
            return tuple(func(arg) for arg, func in zip(args, funcs))
        return tuple(func(*args) for func in funcs)

    return wrapper
