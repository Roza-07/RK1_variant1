"""Параметризованные тесты функции chunk."""

import pytest

from chunk import chunk


@pytest.mark.parametrize(
    "items, size, expected",
    [
        ([1, 2, 3, 4, 5, 6], 2, [[1, 2], [3, 4], [5, 6]]),
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2], 5, [[1, 2]]),
        ([], 3, []),
    ],
)
def test_chunk(
    items: list[int], size: int, expected: list[list[int]]
) -> None:
    assert chunk(items, size) == expected


def test_chunk_invalid_size() -> None:
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)
