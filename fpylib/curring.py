from functools import partial, wraps
from inspect import getmembers, isfunction, signature
from typing import Any, Callable, Union


def currify(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Currying a function.

    :func: The function to be lazy.
    :return: A function that returns the result of the function.
    
    :Example:
    >>> @currify
    >>> def add(x: int, y: int) -> int:
    >>>    return x + y
    >>> add_one = add(1)
    >>> add_one(2)
    3
    >>> add_one(3)
    4
    >>> add_one_map = currify(map)(operator.add)
    >>> add_one_map([1, 2, 3])
    [2, 3, 4]
    
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[Callable[..., Any], Any]:
        if len(signature(func).parameters) == len(args) + len(kwargs):
            return func(*args, **kwargs)
        elif len(signature(func).parameters) > len(args) + len(kwargs):
            return currify(partial(func, *args, **kwargs))
        raise ValueError("Too many arguments")

    try:
        wrapper.__annotations__ = func.__annotations__
    finally:
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
    return wrapper


def currify_class(cls: object) -> object:
    """
    Decorator to make a class lazy.

    :cls: The class to be lazy.
    :return: A class with all the methods lazies.
    """

    def wrapper(cls: object) -> object:
        for name, method in getmembers(cls, predicate=isfunction):
            setattr(cls, name, currify(method))
        return cls

    return wrapper(cls)
