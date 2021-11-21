from typing import Iterator, Optional, Union
from numbers import Number

from fpylib.irange.num_irange import num_irange
from fpylib.irange.char_irange import char_irange


def irange(
    first: Union[Number, str],
    second: Optional[Union[Number, str]] = None,
    final: Optional[Union[Number, str]] = None,
    final_include: bool = False,
) -> Iterator[Union[Number, str]]:
    """
    Intelligen range function that can be used with infinite or finite ranges.

    :first: The first number of the range.
    :second: The second number of the range.
    :final: The final number of the range.
    :return: A generator of the range.
    """

    if isinstance(first, Number):
        yield from num_irange(first, second, final, final_include)
    elif isinstance(first, str):
        yield from char_irange(first, second, final, final_include)
    else:
        raise TypeError(f"Invalid type of {first}")
