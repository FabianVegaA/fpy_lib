from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, Optional, TypeVar


T = TypeVar("T")
S = TypeVar("S")


class Functor(Generic[T]):
    def get(self) -> T:
        return self.__value

    def __init__(self, value: Optional[T] = None) -> None:
        object.__setattr__(self, "_Functor__value", value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError("This object is not modifiable")

    @abstractmethod
    def fmap(self, func: Callable[["Functor[T]"], "Functor[S]"]) -> "Functor[S]":
        pass


def fmap(func: Callable[[Functor[T]], Functor[S]], fa: Functor[T]) -> Functor[S]:
    return fa.fmap(func)
