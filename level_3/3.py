from constants import ___
from types import FunctionType

# Полагаюсь на это:
#  types.FunctionType The type of user-defined functions and functions created by lambda expressions.
def create_user(user_name: str, user_age: int, after_created: FunctionType) -> None:
    pass

 
def send_test_email(user_id: int) -> None:
    pass


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None
