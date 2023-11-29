from typing import Set, Tuple, Mapping


def calculate_total_spent_for_users(users_ids: Set[int],
                                    users_ids_to_users_map: Mapping[int, Tuple[str, int, list[int]]]) -> int | None:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_users(
        users_ids={3, 6, 12, 15},
        users_ids_to_users_map={
            3: ("Ilya", 32, [102, 15, 63, 12]),
        },
    ) == 192
