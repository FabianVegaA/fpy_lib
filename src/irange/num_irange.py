from typing import Iterator, Optional
from numbers import Number


def _number_generator(
    start: Number, final: Optional[Number] = None, step: Number = 1
) -> Iterator[Number]:
    current = start
    while True if final is None else current < final:
        yield current
        current += step


def num_irange(
    first: Number,
    second: Optional[Number] = None,
    final: Optional[Number] = None,
    final_include: bool = False,
) -> Iterator[Number]:
    """
    Intelligen range function that can be used \
    with infinite or finite ranges of integers.

    :first: The first character of the range.
    :second: The second character of the range.
    :final: The final character of the range.
    :return: A generator of the range.
    """

    if isinstance(final, Number):
        if second in [None, Ellipsis]:
            yield from _number_generator(first, final + final_include)
        elif isinstance(second, Number):
            yield from _number_generator(first, final + final_include, second - first)
        else:
            raise TypeError("Second argument must be an integer")
    elif final in [None, Ellipsis]:
        if second in [None, Ellipsis]:
            yield from _number_generator(first)
        elif "__sub__" in dir(second):
            yield from _number_generator(first, second - first)
        else:
            raise TypeError(f"{type(first)} argument must have __sub__")

    else:
        raise TypeError("Final argument must be an integer")
