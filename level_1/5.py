from constants import none_type


def is_correct_email(raw_email: str|none_type) -> bool:
    pass


if __name__ == "__main__":
    assert is_correct_email(raw_email="test@gmail.co") is False
