from constants import ___
from typing import TypedDict


def calculate_total_spent_for_user(user: dict['name': str, "age": int, 'transactions_sums': list[int]]) -> int:
    # попробуй тут воспользовать typing.TypedDict
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_user(
        user={
            "name": "Ilya",
            "age": 32,
            "transactions_sums": [102, 15, 63, 12],
        },
    ) == 192
