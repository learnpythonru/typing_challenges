from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class User:
    name: str
    age: int
    email: str


def get_current_user() -> User | None:
    pass


if __name__ == "__main__":
    assert get_current_user() == ("Ilya Lebedev", 33, "melevir@gmail.com")
