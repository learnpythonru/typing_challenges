import datetime
from constants import ___

# Вопрос: в тупле  [("Молоко", 1, 32.2)]) последний элемент - 32.2, 
# даже type(32.2) выдаёт float, поэтому ящитаю, что убирать его не надо. Добавляю опцию int,
# но чувствую подвох
def parse_receipt(raw_receipt: str) -> tuple[int, datetime.date, list[tuple[str, int, float | int]]]:
    pass

 
if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
