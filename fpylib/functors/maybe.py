from typing import Callable, Generic, Optional
from fpylib.functors.functor import T, S, Functor
from fpylib.functors.monad import Monad
from fpylib.functors.applicative import Applicative


class Maybe(Applicative, Monad, Generic[T]):
    def unit(self, value: T) -> "Maybe[T]":
        if value is not None:
            return Just(value)
        return Nothing()

    def bind(self, func: Callable[[T], S]) -> "Maybe[S]":
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
