import decimal
import uuid

from constants import none_type


def get_user_balance(user_id: uuid.UUID) -> decimal.Decimal|none_type:
    pass


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
