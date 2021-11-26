from typing import Any, Callable, Generic, Optional, TypeVar
from fpylib.lazyness import lazy_eval

T = TypeVar("T")
S = TypeVar("S")


class Functor(Generic[T]):
    """
    Class Functor is a generic class that implements the Functor type class.


    :param value: The value of the functor.
    :type value: T
    :return: A functor with the given value.
    """

    def __init__(self, value: Optional[T] = None) -> None:
        """
        Initialize a functor with the given value.

        :param value: The value of the functor.
        :type value: Optional[T]
        :return: A functor with the given value.
        """

        def frozen_setattr(cls, __name: str, __value: Any) -> None:
            raise AttributeError("This object is not modifiable")

        object.__setattr__(self, "_Functor__value", value)
        object.__setattr__(self, "__setattr__", frozen_setattr)

    def get(self) -> T:
        """
        Get the value of the functor.

        :return: The value of the functor.
        """
        return self.__value

    def fmap(self, func: Callable[["Functor[T]"], "Functor[S]"]) -> "Functor[S]":
        """
        Apply a function to the value of the functor.

        :param func: The function to apply.
        :type func: Callable[["Functor[T]"], "Functor[S]"]
        :return: A functor with the value of the functor after applying the function.
        """
        return Functor(func(self.get()))


@lazy_eval
def fmap(func: Callable[[Functor[T]], Functor[S]], ft: Functor[T]) -> Functor[S]:
    """
    This function is a functor's fmap function.

    :param func: Callable[[Functor[T]], Functor[S]]
    :param ft: Functor[T]
    :return: Functor[S]
    """
    return ft.fmap(func)
