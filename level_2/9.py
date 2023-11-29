from dataclasses import dataclass
import datetime
from typing import List, Tuple


@dataclass(frozen=True, slots=True)
class Receipt_data:
    namber: int
    date: datetime.date
    items: List[Tuple[str, int, float]]


def parse_receipt(raw_receipt: str) -> Receipt_data | None:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
