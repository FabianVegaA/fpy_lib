from typing import Callable, Generic, Optional

from fpylib.functors.applicative import Applicative
from fpylib.functors.functor import _S, _T
from fpylib.functors.monad import Monad, unit


class Maybe(Applicative, Monad, Generic[_T]):
    """
    This is a implementation of the Maybe Monad of Haskell. It is a functor, applicative and monad.
    """

    def unit(self, value: _T) -> "Maybe[_T]":
        """
        Return a Just pr Nothing value based on if the value is None or not.

        :param value: The value to be checked.
        :type value: T
        :return: Just value or Nothing
        """
        if value is not None:
            return Just(value)
        return Nothing()

    def bind(self, func: Callable[[_T], _S]) -> "Maybe[_S]":
        """
        Return a Just pr Nothing value based on if occur an error or not.

        :param func: The function to be applied.
        :type func: Callable[[T], S]
        :return: Just value or Nothing
        """
        try:
            value = func(self.get())
            if value is None:
                return Nothing(ValueError("The value is None"))
            return Just(value)
        except Exception as e:
            return Nothing(e)


class Just(Maybe):
    def __str__(self) -> str:
        return f"Just {self.get()}"

    def __repr__(self) -> str:
        return f"Just {type(self.get())}"


class Nothing(Maybe):
    def __init__(self, *failure: Optional[Exception]) -> None:
        """
        This does nothing.
        """
        object.__setattr__(
            self, "_Nothing__failure", filter(lambda fail: fail is not None, failure)
        )

    def fails(self) -> bool:
        return self.__failure

    def __str__(self) -> str:
        return "Nothing"

    def __repr__(self) -> str:
        return f"{self.__str__()} {list(self.__failure)}"


def maybe_conditioner(func: Callable[..., _T]) -> Callable[..., "Maybe[_T]"]:
    """
    Conditioner for Maybe.

    :param func: The function to wrap in a Monad.
    :type func: Callable[..., T]
    :return: The wrapped function.
    :rtype: Callable[..., Monad[T]]
    """

    def wrapper(*arg, **kwargs) -> "Maybe[_T]":
        try:
            return unit(Maybe, func(*arg, **kwargs))
        except Exception as e:
            return Nothing(e)

    return wrapper
