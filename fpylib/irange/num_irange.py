from typing import Iterator, Optional

from fpylib.types import is_number, number


def _number_generator(
    start: number, final: Optional[number] = None, step: number = 1
) -> Iterator[number]:
    current = start
    while True if final is None else current < final:
        yield current
        current += step


def _generate_finite_num_range(
    first: number,
    second: Optional[number],
    final: number,
    final_include: bool,
) -> Iterator[number]:

    if second in [None, Ellipsis]:
        yield from _number_generator(first, final + final_include)
    elif is_number(second):
        yield from _number_generator(first, final + final_include, second - first)
    else:
        raise TypeError("Second argument must be an number")


def _generate_infinite_num_range(
    first: number, second: Optional[number]
) -> Iterator[number]:
    if second in [None, Ellipsis]:
        yield from _number_generator(first)
    elif is_number(second):
        yield from _number_generator(first, step=second - first)
    else:
        raise TypeError(f"Second {second} argument must be an number or None")


def num_irange(
    first: number,
    second: Optional[number] = None,
    final: Optional[number] = None,
    final_include: bool = False,
) -> Iterator[number]:
    """
    Intelligen range function that can be used \
    with infinite or finite ranges of integers.

    :first: The first character of the range.
    :second: The second character of the range.
    :final: The final character of the range.
    :return: A generator of the range.
    """

    if is_number(final):
        yield from _generate_finite_num_range(first, second, final, final_include)
    elif final in [None, Ellipsis]:
        yield from _generate_infinite_num_range(first, second)
    else:
        raise TypeError("Final argument must be an integer")
