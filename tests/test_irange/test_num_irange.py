from numbers import Number
from typing import Any, Iterable, List, Optional, Tuple
import pytest

from fpylib.irange.num_irange import num_irange


test_cases_finite_num_irange: Tuple[Number, Any, Any, Iterable] = [
    (0, ..., 10, False, range(10)),
    (0, ..., 10, True, range(11)),
    (0, 2, 10, False, range(0, 10, 2)),
    (1, 3, 10, False, range(1, 10, 2)),
    (0.1, 0.6, 1.2, False, [0.1, 0.6, 1.1]),
]


@pytest.mark.parametrize(
    "first, second, final, include_final, expected", test_cases_finite_num_irange
)
def test_finite_num_irange(
    first: Number, second: Any, final: Any, include_final: bool, expected: Iterable
):
    assert list(num_irange(first, second, final, include_final)) == list(expected)


test_cases_infinite_num_irange: Tuple[Number, Any] = [
    (0, ...),
    (0, 2),
    (1, ...),
]


@pytest.mark.parametrize("first, second", test_cases_infinite_num_irange)
def test_infinite_num_irange(first: Number, second: Any):
    LIMIT = 1000

    def _range(first: Number, second: Optional[Number], limit: int) -> List[Number]:
        return [v for _, v in zip(range(limit), num_irange(first, second, None))]

    if second in [None, Ellipsis]:
        assert _range(first, None, LIMIT) == list(range(first, first + LIMIT))
    else:
        assert _range(first, second, LIMIT) == list(
            range(first, LIMIT * (second - first), second - first)
        )
