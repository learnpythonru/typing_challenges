import uuid
from typing import Optional

from constants import ___


def stringify(value: Optional[str | int | float]) -> ___:
    pass


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
