import decimal
import uuid
from uuid import UUID
from constants import ___


def get_user_balance(user_id: UUID) -> ___:
    pass


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
