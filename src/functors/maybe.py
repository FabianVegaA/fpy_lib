from typing import Callable, Optional
from src.functors.functor import T, S
from src.functors.monad import Monad


class Maybe(Monad):
    def unit(self, value: T) -> "Maybe[T]":
        if value is not None:
            return Just(value)
        return Nothing()

    def bind(self, func: Callable[[T], S]) -> "Maybe[S]":
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
    def __init__(self, *failure: Optional[Exception]) -> None:
        """
        This does nothing.
        """
        object.__setattr__(
            self, "_Nothing__failure", filter(lambda fail: fail is not None, failure)
        )

    def __str__(self) -> str:
        return "Nothing"

    def __repr__(self) -> str:
        return f"{self.__str__()} {list(self.__failure)}"
