from typing import Iterator, Optional, Any

from fpylib.irange.num_irange import (
    _generate_finite_num_range,
    _generate_infinite_num_range,
)


def is_char(*objs: Any, allow_none=False) -> bool:
    """
    Checks if the object is a character.

    :obj: The object to be checked.
    :return: True if the object is a character, False otherwise.
    """
    return all(
        (isinstance(obj, str) and len(obj) == 1)
        or (allow_none and (obj is None or obj is Ellipsis))
        for obj in objs
    )


def char_encode(num: int, is_lower=True) -> str:
    """
    Converts an integer to a character string \
    with elements from a-z or A-Z.

    :num: The integer base 10 to be converted.
    :return: The character base 26.
    """
    buffer = 97 if is_lower else 65
    result = "" if num != 0 else chr(buffer + num % 26)
    while num > 0:
        result = chr(buffer + num % 26) + result
        num //= 26
    return result


def char_decode(string: str) -> int:
    """
    Converts an string base 26 to a number of base 10.

    :string: The string to be converted.
    :return: The number base 10.
    """
    if not all(is_char(char) for char in string):
        raise TypeError("The string must be a character [a-zA-Z]")

    if 97 <= ord(string[0]) <= 122:
        buffer = 97
    elif 65 <= ord(string[0]) <= 90:
        buffer = 65
    else:
        raise ValueError(f"{string} must be characters [a-zA-Z]")

    return sum((ord(char) - buffer) * (26 ** i) for i, char in enumerate(string[::-1]))


def is_lower_char(obj: Any) -> bool:
    """
    Checks if the object is a letter.

    :obj: The object to be checked.
    :return: True if is a lower character, \
    False if is upper character and raises TypeError otherwise.
    """
    if not is_char(obj):
        raise TypeError("The object must be a character [a-zA-Z]")
    elif ord(obj) >= 97 and ord(obj) <= 122:
        return True
    return False


def _generate_infinite_char_range(first: str, second: Optional[str]) -> Iterator[str]:
    """
    Generates an infinite range of characters.

    :first: The first character of the range.
    :second: The second character of the range.
    :return: A generator of the range.
    """
    is_lower = is_lower_char(first)
    _first, _second = (
        char_decode(string) if string else None for string in (first, second)
    )
    yield from (
        char_encode(i, is_lower) for i in _generate_infinite_num_range(_first, _second)
    )


def _generate_finite_char_range(
    first: str, second: Optional[str], final: Optional[str], final_include: bool
) -> Iterator[str]:
    """
    Generates a finite range of characters.

    :first: The first character of the range.
    :second: The second character of the range.
    :final: The final character of the range.
    :final_include: True if the final character is included in the range.
    :return: A generator of the range.
    """
    is_lower = is_lower_char(first)
    _first, _second, _final = (
        char_decode(string) if string else None for string in (first, second, final)
    )

    yield from (
        char_encode(i, is_lower)
        for i in _generate_finite_num_range(_first, _second, _final, final_include)
    )


def char_irange(
    first: str,
    second: Optional[str] = None,
    final: Optional[str] = None,
    final_include: bool = False,
) -> Iterator[str]:
    """
    Intelligen range function that can be used \
    with infinite or finite ranges of characters.

    :first: The first character of the range.
    :second: The second character of the range.
    :final: The final character of the range.
    :return: A generator of the range.
    """

    if isinstance(final, str):
        yield from _generate_finite_char_range(first, second, final, final_include)
    elif final in [None, Ellipsis]:
        yield from _generate_infinite_char_range(first, second)
    else:
        raise TypeError("Final argument must be an character")
