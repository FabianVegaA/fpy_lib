from typing import Callable
from src.functors.functor import Functor, T, S


class Monad(Functor):
    def unit(self, value: T) -> "Monad[T]":
        return Monad(value)

    def bind(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return Monad(func(self.get()))

    def fmap(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return self.bind(func)

    def __rshift__(self, func: Callable[[[T]], S]) -> "Monad[S]":
        return self.bind(func)


def unit(m: "Monad", value: T) -> "Monad[T]":
    return m.unit(m, value)
