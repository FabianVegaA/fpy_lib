from typing import Callable
from src.functors.functor import Functor, T, S, fmap
from src.lazyness import lazy_eval


@lazy_eval
def apply(func: Functor[Callable[[T], S]], ft: Functor[T]) -> Functor[S]:
    """
    This the function applicative to a functor that wraps a function and a functor.

    :param func: Functor[Callable[[T], S]]
    :param ft: Functor[T]
    :return: Functor[S]
    """
    return ft.apply(func)


def lift(func: Callable[[T, T], S], f1: Functor[T], f2: Functor[T]) -> Functor[S]:
    """
    This is the version Pythonic to liftA2 from Haskell.

    :param func: Callable[[T, T], S]
    :param f1: Functor[T]
    :param f2: Functor[T]
    :return: Functor[S]
    """
    return apply(fmap(lazy_eval(func), f1), f2)
