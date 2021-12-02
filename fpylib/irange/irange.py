from typing import Iterator, Optional, Union

from fpylib.irange.char_irange import char_irange
from fpylib.irange.num_irange import num_irange
from fpylib.types import is_number, number


def irange(
    first: Union[number, str],
    second: Optional[Union[number, str]] = None,
    final: Optional[Union[number, str]] = None,
    final_include: bool = False,
) -> Iterator[Union[number, str]]:
    """
    Intelligen range function that can be used with infinite or finite ranges.

    :first: The first number of the range.
    :second: The second number of the range.
    :final: The final number of the range.
    :return: A generator of the range.
    """

    if is_number(first):
        assert (
            second is Optional[number] and final is Optional[number]
        ), "Invalid range."
        yield from num_irange(first, second, final, final_include)
    elif first is str:
        assert second is Optional[str] and final is Optional[str], "Invalid range."
        yield from char_irange(first, second, final, final_include)
    else:
        raise TypeError(f"Invalid type of {first}")
