from constants import ___
from typing import TypedDict


class User(TypedDict):
    "name": str
    "age": int
    "transactions_sums": list[int]


def calculate_total_spent_for_user(user: User) -> int:
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

# Вопрос:
# допустимо ли в аннотации типов указывать TypeDict следующими способами?
#def calculate_total_spent_for_user(user: TypedDict('User', 'name' = str, 'age' = int, 'transactions_sums' = list[int])) -> int:
#def calculate_total_spent_for_user(user: TypedDict('User', {'name': str, 'age': int, 'transactions_sums': list[int]})) -> int:

# пока на основе документации понимаю, что оба варианта верны, и именно в таком виде, без квадратных скобок