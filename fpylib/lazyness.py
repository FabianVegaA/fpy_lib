from functools import partial, wraps
from typing import Callable, Union, Any
from inspect import getmembers, isfunction, signature


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

    return wrapper


def lazy_class(cls: object) -> object:
    """
    Decorator to make a class lazy.

    :cls: The class to be lazy.
    :return: A class with all the methods lazies.
    """

    @wraps(cls)
    def wrapper(cls: object) -> Callable[[object], object]:
        for name, method in getmembers(cls, predicate=isfunction):
            setattr(cls, name, lazy_eval(method))
        return cls

    return wrapper(cls)
