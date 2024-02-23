from typing import Any


def stringify(value: Any) -> str:  # 5:22 ANN401 Dynamically typed expressions (typing.Any) are disallowed in `value`
    # либо тут может быть str | int | flat | None
    return str(value)


if __name__ == "__main__":
    assert stringify(value="12") == "12"  # noqa: S101, S101
    assert stringify(value=15) == "15"  # noqa: S101
    assert stringify(value=.5) == "0.5"  # noqa: S101, S101
    assert stringify(value=None) == "None"  # noqa: S101
