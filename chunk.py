"""Задание 1: разбиение списка на части."""

from typing import TypeVar

T = TypeVar("T")


def chunk(items: list[T], size: int) -> list[list[T]]:
    """Разбить список на подсписки длиной не более size."""
    if size < 1:
        raise ValueError("size должен быть не меньше 1")

    result: list[list[T]] = []
    for i in range(0, len(items), size):
        result.append(items[i:i + size])
    return result
