from typing import Any, Callable, List, Tuple
import pytest


from src.composer import compose, paralalize

test_case_compose: Tuple[List[Callable], List[Any], Any] = [
    ([int, (lambda x: -5 * x), (lambda x: x + 1), (lambda x: x * 2)], ["1"], -8),
    ([(lambda x: x ** 3), (lambda x: -x), (lambda x: x * 2)], [2], -16),
    (
        [(lambda x: list(range(x))), (lambda x: x[::-1]), (lambda x: x[::2])],
        [5],
        [4, 2, 0],
    ),
    ([(lambda *xs: sum(xs)), (lambda x: x * 2), (lambda x: x + 1)], [1, 2, 3, 4], 21),
]


@pytest.mark.parametrize("funcs, arg, expected", test_case_compose)
def test_compose(funcs: List[Callable], arg: List[Any], expected: Any):
    assert compose(*funcs)(*arg) == expected


test_case_paralalize: Tuple[List[Callable], List[Any], bool, Any] = [
    ([(lambda x: x ** 3), (lambda x: -x), (lambda x: x * 2)], [2], True, (8, -2, 4)),
    (
        [
            compose(
                (lambda x: list(range(x))), (lambda x: x[::-1]), (lambda x: x[::2])
            ),
            compose((lambda x: x ** 3), (lambda x: -x), (lambda x: x * 2)),
            (lambda x: x + 1),
        ],
        [5, 2, 1],
        False,
        ([4, 2, 0], -16, 2),
    ),
]


@pytest.mark.parametrize("funcs, arg, uniqui_intput, expected", test_case_paralalize)
def test_paralalize(
    funcs: List[Callable], arg: List[Any], uniqui_intput: bool, expected: Any
):
    assert paralalize(*funcs)(*arg, uniqui_intput=uniqui_intput) == expected
