import uuid

from constants import none_type
from typing import Any


# сначала написала none_type|str, потому что хотела избежать Any
def stringify(value: Any) -> str:
    pass


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
