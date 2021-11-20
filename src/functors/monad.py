from typing import Callable
from src.functors.functor import Functor, T, S
from src.lazyness import lazy_eval


class Monad(Functor):
    def unit(self, value: T) -> "Monad[T]":
        return Monad(value)

    def bind(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return Monad(func(self.get()))

    def apply(self, func: "Monad[Callable[[T], S]]") -> "Monad[S]":
        return self.bind(func.get())

    def fmap(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return self.bind(func)

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
