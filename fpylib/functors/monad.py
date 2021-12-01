from typing import Any, Callable, Generic, Optional
from fpylib.functors.functor import T, S
from fpylib.lazyness import lazy_eval


class Monad(Generic[T]):
    """
    This is a implementation of the Monad law:
    - Unit or Return .
    - Bind (>>=) or (>>) here.
    """

    def __init__(self, value: Optional[T] = None) -> None:
        """
        Initialize the Monad with a value.

        :param value: The value to initialize the Monad with.
        :return: None
        """
        object.__setattr__(self, "_Monad__value", value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError("This object is not modifiable")

    def get(self) -> T:
        """
        Get the value of the Monad.

        :return: The value of the Monad.
        """
        return self.__value

    def unit(self, value: T) -> "Monad[T]":
        """
        Return a Monad with the given value.

        :param value: The value to return.
        :return: A Monad with the given value.
        """
        return Monad(value)

    def bind(self, func: Callable[[T], S]) -> "Monad[S]":
        """
        Return a Monad with the result of the given function evaluated with the value of the Monad.

        :param func: The function to evaluate with the value of the Monad.
        :return: A Monad with the result of the given function evaluated with the value of the Monad.
        """
        return Monad(func(self.get()))

    def __rshift__(self, func: Callable[[[T]], S]) -> "Monad[S]":
        """
        Use the >> operator to bind the given function to the value of the Monad.

        For example:
        >>> m = Monad(1) >> (lambda x: x + 1)
        >>> m.get()
        2

        :param func: The function to bind to the value of the Monad.
        :return: A Monad with the result of the given function evaluated with the value of the Monad.
        """
        return self.bind(func)


@lazy_eval
def unit(m: "Monad", value: T) -> "Monad[T]":
    """
    The unit function for the Monad.

    :param m: The Monad.
    :param value: The value to be wrapped in the Monad.
    :return: The Monad with the value.
    """
    return m.unit(m, value)


def unitifier(
    m: "Monad",
    conditioner: Optional[
        Callable[[Callable[..., T]], Callable[..., "Monad[T]"]]
    ] = None,
) -> Callable[[Callable[..., T]], Callable[..., "Monad[T]"]]:
    """
    Return a decorator that wraps the given function in a Monad.
    :param m: The Monad.
    :type m: Monad
    :param conditioner: A function that takes a function and returns a function that return a Monad.
    :type conditioner: Callable[[Callable[..., T]], Callable[..., "Monad[T]"]]
    :return: A decorator that wraps the given function in a Monad.
    :rtype: Callable[[Callable[..., T]], Callable[..., "Monad[T]"]]
    """

    def decorator(func: Callable[..., T]) -> Callable[..., "Monad[T]"]:
        """
        Decorator to wrap the result of a function in a Monad.

        :param func: The function to wrap in a Monad.
        :type func: Callable[..., T]
        :return: The wrapped function.
        :rtype: Callable[..., Monad[T]]
        """

        def wrapper(*arg, **kwargs) -> "Monad[T]":
            if conditioner:
                return conditioner(func)(*arg, **kwargs)
            return unit(m, func(*arg, **kwargs))

        try:
            wrapper.__annotations__ = func.__annotations__
        finally:
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator
