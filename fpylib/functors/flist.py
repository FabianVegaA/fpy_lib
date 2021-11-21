from typing import Callable, Generic, Iterable, List, Optional, Tuple
from fpylib.functors.applicative import Applicative
from fpylib.functors.functor import T, S
from fpylib.functors.monad import Monad
from fpylib.functors.maybe import Just, Maybe, Nothing

from functools import reduce


class FList(Applicative, Monad, Generic[T]):
    def __init__(self, value: Optional[Iterable[T]] = None) -> None:
        if value is not None:
            super().__init__(value=list(value))

    def unit(self, value: Optional[Iterable[T]] = None) -> "FList[T]":
        if value is None:
            return EmptyFList()
        if not isinstance(value, Iterable):
            return FList([value])
        elems = list(filter(lambda x: x is not None, value))
        if not elems:
            return EmptyFList()
        return FList(elems)

    def bind(self, func: Callable[[T], S]) -> "FList[S]":
        if isinstance(self, EmptyFList):
            return EmptyFList()
        return FList(map(func, self))

    def fmap(self, func: Callable[[T], S]) -> "FList[S]":
        return self.bind(func)

    def apply(self, lfunc: "FList[Callable[[T], S]]") -> "FList[S]":
        return FList(
            reduce(lambda l1, l2: l1 + l2, (self.bind(func) for func in lfunc))
        )

    def get(self) -> List[T]:
        return list(super().get())

    def __add__(self, other: "FList[T]") -> "FList[T]":
        return FList(self.get() + other.get())

    def __iter__(self) -> Iterable[T]:
        return self.get().__iter__()

    def __next__(self) -> T:
        return next(self.get())

    def __getitem__(self, __s: slice) -> "FList[T]":
        return self.unit(self.get().__getitem__(__s))

    def __len__(self) -> int:
        return len(self.get())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FList):
            return False
        return self.get() == other.get()

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __contains__(self, item: T) -> bool:
        return item in self.get()

    def __bool__(self) -> bool:
        return not isinstance(self, EmptyFList)

    def __str__(self) -> str:
        return f"FList {self.get()}"

    def __repr__(self) -> str:
        return f"FList {list(set(map(type, self.get())))}"


class EmptyFList(FList):
    def __init__(self):
        super().__init__(None)

    def get(self) -> List[T]:
        return []

    def __str__(self) -> str:
        return "EmptyFList"

    def __repr__(self) -> str:
        return self.__str__()


def concat(*ls: "FList[T]") -> "FList[T]":
    """
    Concatenate two or more FList.

    :param ls: FList to concatenate
    :return: FList
    """
    return FList(sum(ls, EmptyFList()))


def head(l: "FList[T]") -> T:
    """
    Get the first element of a FList.

    :param l: FList
    :return: First element of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("head: empty list")
    return l.get()[0]


def last(l: "FList[T]") -> T:
    """
    Get the last element of a FList.

    :param l: FList
    :return: Last element of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("last: empty list")
    return l.get()[-1]


def tail(l: "FList[T]") -> "FList[T]":
    """
    Get the all elements of a FList except the first one.

    :param l: FList
    :return: Tail of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("tail: empty list")
    return FList(l.get()[1:])


def init(l: "FList[T]") -> "FList[T]":
    """
    Get all elements of a FList except the last one.

    :param l: FList
    :return: Tail of FList
    """
    if isinstance(l, EmptyFList):
        raise ValueError("init: empty list")
    return FList(l.get()[:-1])


def uncons(l: "FList[T]") -> "Maybe[Tuple[T, 'FList[T]']]":
    """
    Get the first element of a FList and the rest of the FList.

    :param l: FList
    :return: First element of FList and the rest of the FList
    """
    if isinstance(l, EmptyFList):
        raise Nothing()
    return Just(l.get()[0], FList(l.get()[1:]))


def singleton(x: T) -> "FList[T]":
    """
    Create a FList with a single element.

    :param x: Element
    :return: FList
    """
    return FList([x])


def null(l: "FList[T]") -> bool:
    """
    Verify if a FList is empty.

    :param l: FList
    :return: True if FList is empty, False otherwise
    """
    if not isinstance(l, FList):
        raise TypeError(f"null: {l} is not a FList")
    return isinstance(l, EmptyFList)


def length(l: "FList[T]") -> int:
    """
    Get the length of a FList.

    :param l: FList
    :return: Length of FList
    """
    return len(l.get())


def reverse(l: "FList[T]") -> "FList[T]":
    """
    Reverse a FList.

    :param l: FList
    :return: Reversed FList
    """
    return FList(reversed(l.get()))
