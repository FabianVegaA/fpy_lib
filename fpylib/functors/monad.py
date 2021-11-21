from typing import Any, Callable, Generic, Optional
from fpylib.functors.functor import T, S
from fpylib.lazyness import lazy_eval


class Monad(Generic[T]):
    def __init__(self, value: Optional[T] = None) -> None:
        object.__setattr__(self, "_Monad__value", value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError("This object is not modifiable")

    def get(self) -> T:
        return self.__value

    def unit(self, value: T) -> "Monad[T]":
        return Monad(value)

    def bind(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return Monad(func(self.get()))

    def __rshift__(self, func: Callable[[[T]], S]) -> "Monad[S]":
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
