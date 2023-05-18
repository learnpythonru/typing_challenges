import datetime

from constants import none_type


def calculate_age(date_of_birth: datetime.date|none_type) -> int:
    pass


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 57
