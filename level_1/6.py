from constants import ___


def is_loan_amount_too_big(loan_amount_usd: int | float, max_loan_amount_for_user_usd: int | float) -> bool:
    pass

# в примере кончено напрашивается int, а не float. однако про олгике банковских тразакций и учитывая центы считаю, что может быть float


if __name__ == "__main__":
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=4000) is False
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=None) is False
