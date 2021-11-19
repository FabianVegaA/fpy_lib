from typing import Callable
from src.functors.functor import Functor, T, S, fmap
from src.lazyness import lazy_eval


@lazy_eval
def apply(func: Functor[Callable[[T], S]], value: Functor[T]) -> Functor[S]:
    return fmap(func.get(), value)
