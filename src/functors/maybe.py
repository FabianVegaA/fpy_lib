from typing import Callable
from src.functors.functor import T, S
from src.functors.monad import Monad


class Maybe(Monad):
    def unit(self, value: T) -> "Maybe[T]":
        if value is not None:
            return Just(value)
        return Nothing()

    def bind(self, func: Callable[[[T]], S]) -> "Maybe[S]":
        try:
            return Just(func(self.get()))
        except Exception:
            return Nothing()


class Just(Maybe):
    def __str__(self) -> str:
        return f"Just {self.get()}"

    def __repr__(self) -> str:
        return f"Just {type(self.get())}"


class Nothing(Maybe):
    def __init__(self) -> None:
        return

    def __str__(self) -> str:
        return "Nothing"

    def __repr__(self) -> str:
        return self.__str__()
