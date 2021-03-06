from functools import reduce
from typing import Any, Callable, Generic, Iterable, List, Optional, Tuple

from fpylib.functors.applicative import Applicative
from fpylib.functors.functor import _S, _T, Functor
from fpylib.functors.maybe import Just, Maybe, Nothing
from fpylib.functors.monad import Monad


class FList(Applicative, Monad, Generic[_T]):
    def __new__(cls, value: Optional[_T] = None) -> "FList[_T]":
        if value is None:
            return EmptyFList()
        if not isinstance(value, Iterable):
            value = [value]

        elems = list(filter(lambda x: x is not None, value))

        if not elems:
            return EmptyFList()

        obj = super().__new__(cls)
        object.__setattr__(obj, "_Functor__value", elems)
        return obj

    def __init__(self, value: Optional[_T] = None) -> None:
        def frozen_setattr(cls, __name: str, __value: Any) -> None:
            raise AttributeError("This object is not modifiable")

        object.__setattr__(self, "__setattr__", frozen_setattr)

    def unit(self, value: Optional[Iterable[_T]] = None) -> "FList[_T]":
        return FList(value)

    def bind(self, func: Callable[[_T], _S]) -> "FList[_S]":
        if isinstance(self, EmptyFList):
            return EmptyFList()
        return FList(list(map(func, self)))

    def fmap(self, func: Callable[[_T], _S]) -> "FList[_S]":
        return self.bind(func)

    def apply(self, lfunc: "FList[Callable[[_T], _S]]") -> "FList[_S]":
        return reduce(lambda l1, l2: l1 + l2, [self.bind(func) for func in lfunc])

    def __add__(self, other: "FList[_T]") -> "FList[_T]":
        return FList(list(self.get()) + list(other.get()))

    def __iter__(self) -> Iterable[_T]:
        return self.get().__iter__()

    def __next__(self) -> _T:
        return next(self.get())

    def __getitem__(self, __s: slice) -> "FList[_T]":
        return self.unit(self.get().__getitem__(__s))

    def __len__(self) -> int:
        return len(self.get())

    def __eq__(self, other: object) -> bool:
        return False if not isinstance(other, FList) else self.get() == other.get()

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __contains__(self, item: _T) -> bool:
        return item in self.get()

    def __bool__(self) -> bool:
        return not isinstance(self, EmptyFList)

    def __str__(self) -> str:
        return f"FList {self.get()}"

    def __repr__(self) -> str:
        return f"FList {list(set(map(type, self.get())))}"


class EmptyFList(FList):
    def __new__(cls) -> "EmptyFList":
        return Functor.__new__(cls)

    def get(self) -> List[_T]:
        return []

    def __str__(self) -> str:
        return "EmptyFList"

    def __repr__(self) -> str:
        return self.__str__()


def concat(*ls: FList[_T]) -> FList[_T]:
    """
    Concatenate two or more FList.

    :param ls: FList to concatenate
    :return: FList
    """
    return FList(sum(ls, EmptyFList()))


def head(l: FList[_T]) -> _T:
    """
    Get the first element of a FList.

    :param l: FList
    :return: First element of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("head: empty list")
    return l.get()[0]


def last(l: FList[_T]) -> _T:
    """
    Get the last element of a FList.

    :param l: FList
    :return: Last element of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("last: empty list")
    return l.get()[-1]


def tail(l: "FList[_T]") -> FList[_T]:
    """
    Get the all elements of a FList except the first one.

    :param l: FList
    :return: Tail of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("tail: empty list")
    return FList(l.get()[1:])


def init(l: FList[_T]) -> FList[_T]:
    """
    Get all elements of a FList except the last one.

    :param l: FList
    :return: Tail of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("init: empty list")
    return FList(l.get()[:-1])


def uncons(l: FList[_T]) -> "Maybe[Tuple[_T, 'FList[_T]']]":
    """
    Get the first element of a FList and the rest of the FList.

    :param l: FList
    :return: First element of FList and the rest of the FList
    """
    if isinstance(l, EmptyFList):
        raise Nothing()
    return Just(l.get()[0], FList(l.get()[1:]))


def singleton(x: _T) -> FList[_T]:
    """
    Create a FList with a single element.

    :param x: Element
    :return: FList
    """
    return FList([x])


def null(l: FList[_T]) -> bool:
    """
    Verify if a FList is empty.

    :param l: FList
    :return: True if FList is empty, False otherwise
    """
    if not isinstance(l, FList):
        raise TypeError(f"null: {l} is not a FList")
    return isinstance(l, EmptyFList)


def length(l: FList[_T]) -> int:
    """
    Get the length of a FList.

    :param l: FList
    :return: Length of FList
    """
    return len(l.get())


def reverse(l: FList[_T]) -> FList[_T]:
    """
    Reverse a FList.

    :param l: FList
    :return: Reversed FList
    """
    return FList(reversed(l.get()))
