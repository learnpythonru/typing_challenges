# from constants import ___  # какой в этом смысл? не понятно зачем...  # noqa: ERA001


def is_user_banned(user_id: int) -> bool:
    return bool(user_id)


if __name__ == "__main__":
    assert is_user_banned(user_id=32) is True  # noqa: S101
