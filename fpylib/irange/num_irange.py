from typing import Iterator, Optional
from numbers import Number


def _number_generator(
    start: Number, final: Optional[Number] = None, step: Number = 1
) -> Iterator[Number]:
    current = start
    while True if final is None else current < final:
        yield current
        current += step


def _generate_finite_num_range(
    first: Number,
    second: Optional[Number],
    final: Optional[Number],
    final_include: bool,
) -> Iterator[Number]:
    if second in [None, Ellipsis]:
        yield from _number_generator(first, final + final_include)
    elif isinstance(second, Number):
        yield from _number_generator(first, final + final_include, second - first)
    else:
        raise TypeError("Second argument must be an integer")


def _generate_infinite_num_range(
    first: Number, second: Optional[Number]
) -> Iterator[Number]:
    if second in [None, Ellipsis]:
        yield from _number_generator(first)
    elif "__sub__" in dir(second):
        yield from _number_generator(first, step=second - first)
    else:
        raise TypeError(f"{type(first)} argument must have __sub__")


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
        yield from _generate_finite_num_range(first, second, final, final_include)
    elif final in [None, Ellipsis]:
        yield from _generate_infinite_num_range(first, second)
    else:
        raise TypeError("Final argument must be an integer")
