from functools import partial, wraps
from inspect import getmembers, isfunction, signature
from typing import Any, Callable, Union


def lazy_eval(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to make a function lazy.

    :func: The function to be lazy.
    :return: A function that returns the result of the function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[Callable[..., Any], Any]:
        if len(signature(func).parameters) == len(args) + len(kwargs):
            return func(*args, **kwargs)
        elif len(signature(func).parameters) > len(args) + len(kwargs):
            return lazy_eval(partial(func, *args, **kwargs))
        raise ValueError("Too many arguments")

    try:
        wrapper.__annotations__ = func.__annotations__
    finally:
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
    return wrapper


def lazy_class(cls: object) -> object:
    """
    Decorator to make a class lazy.

    :cls: The class to be lazy.
    :return: A class with all the methods lazies.
    """

    def wrapper(cls: object) -> object:
        for name, method in getmembers(cls, predicate=isfunction):
            setattr(cls, name, lazy_eval(method))
        return cls

    return wrapper(cls)
