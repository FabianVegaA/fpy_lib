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


func_parallelized = parallelize(
    sorted,
    sum,
    max,
    min,
)

list_1 = [1, 4, 2, 3, 4, 1, 2, 3, 4, 10]
list_2 = [5, 6, 7, 8, 9, 10]
list_3 = [-1, -5, 100, 19, 99]

print(func_parallelized(list_1, list_2, list_3, list_3, uniqui_intput=False))
