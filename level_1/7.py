from constants import VAR_NONE


def send_email(header: str, text_content: str, send_to: str) -> None:
    return VAR_NONE


if __name__ == "__main__":
    assert send_email(header="Test email", text_content="This is a test email", send_to="test@gmail.com") is None
    #  mypy error: "send_email" does not return a value (it only ever returns None)  [func-returns-value]
