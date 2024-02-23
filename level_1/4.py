import datetime

# from constants import ___


def calculate_age(date_of_birth: datetime.date) -> int:
    today = datetime.date.today()
    return (today.year - datetime.date(1965, 6, 2).year -
            ((today.month, today.day) < (date_of_birth.month, date_of_birth.day)))


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 58
