from typing import Callable, Generic

from fpylib.functors.functor import _S, _T, Functor, fmap
from fpylib.lazyness import lazy_eval


class Applicative(Functor, Generic[_T]):
    def apply(self, func: "Functor[Callable[[_T], _S]]") -> "Functor[_S]":
        """
        Apply a wrapped function to a wrapped value of the functor.

        :param func: A wrapped function.
        :return: A wrapped value of the functor.
        """
        return self.bind(func.get())


@lazy_eval
def apply(func: Functor[Callable[[_T], _S]], ft: Functor[_T]) -> Functor[_S]:
    """
    This the function applicative to a functor that wraps a function and a functor.

    :param func: Functor[Callable[[T], S]]
    :param ft: Functor[T]
    :return: Functor[S]
    """
    return ft.apply(func)


def lift_a2(
    func: Callable[[_T, _T], _S], f1: Functor[_T], f2: Functor[_T]
) -> Functor[_S]:
    """
    This is the version Pythonic to liftA2 from Haskell.

    :param func: Callable[[T, T], S]
    :param f1: Functor[T]
    :param f2: Functor[T]
    :return: Functor[S]
    """
    return apply(fmap(lazy_eval(func), f1), f2)
