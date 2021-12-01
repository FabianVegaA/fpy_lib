import pytest

from fpylib.functors.flist import FList, EmptyFList
from fpylib.functors.monad import unit
from fpylib.functors.applicative import apply

_test_flist_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], FList),
    ([], [], EmptyFList),
    (None, [], EmptyFList),
    (1, [1], FList),
]


@pytest.mark.parametrize("l, expected_list, expected_instance", _test_flist_cases)
def test_flist(l, expected_list, expected_instance):
    fl = FList(l)

    assert fl.get() == expected_list
    assert isinstance(fl, expected_instance)


test_flist(*_test_flist_cases[-1])

_test_unit_flist_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], FList),
    ([], [], EmptyFList),
    (None, [], EmptyFList),
    (1, [1], FList),
]


@pytest.mark.parametrize("l, expected_list, expected_instance", _test_unit_flist_cases)
def test_unit_flist(l, expected_list, expected_instance):
    fl = unit(FList, l)

    assert fl.get() == expected_list
    assert isinstance(fl, expected_instance)


_test_bind_flist_cases = [
    ([1, 2, 3, 4, 5], lambda x: x + 1, [2, 3, 4, 5, 6]),
    ([], lambda x: x + 1, []),
    (None, lambda x: x + 1, []),
    (1, lambda x: x + 1, [2]),
]


@pytest.mark.parametrize("l, f, expected_list", _test_bind_flist_cases)
def test_bind_flist(l, f, expected_list):
    fl = FList(l)

    assert fl.bind(f).get() == expected_list


_test_apply_flist_cases = [
    (
        [1, 2, 3],
        [lambda x: x + 1, lambda x: x + 2],
        [2, 3, 4, 3, 4, 5],
    ),
]


@pytest.mark.parametrize("l, fs, expected_list", _test_apply_flist_cases)
def test_apply_flist(l, fs, expected_list):
    fs_fl = FList(fs)
    l_fl = FList(l)

    assert apply(fs_fl, l_fl).get() == expected_list
