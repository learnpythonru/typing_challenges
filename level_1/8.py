import decimal
import uuid

# from constants import ___


def get_user_balance(user_id: uuid.uuid4()) -> decimal.Decimal:  # error: Invalid type comment or annotation  [valid-type]
    return decimal.Decimal("265.2")  # снова не понял, как из uuid получить decimal.Decimal("265.2")


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
