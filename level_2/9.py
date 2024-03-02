import datetime
from typing import TypeAlias

from constants import ___

type Position = tuple[str, int, float]
# Position: TypeAlias = tuple[str, int, float]  # for lower 3.12


def parse_receipt(raw_receipt: str) -> tuple[int, datetime.date, list[Position]]:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
