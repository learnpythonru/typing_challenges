from constants import ___
from typing import TypeAlias

type Point = tuple[int, int]
# Point: TypeAlias = tuple[int, int]  # for lower Python 3.12


def is_point_in_square(point: Point, left_upper_corner: Point, right_bottom_corner: Point) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
