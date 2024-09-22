import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("amount, expected", [
        (100, 1100),
        (500, 1500),
        (200, 1200),
        (0, 1000),
    ]
)
def test_deposit_various_values(amount, expected):
    account = BankAccount(balance=1000, log_file="transaction_log.txt")
    new_balance = account.deposit(amount)
    assert  new_balance == expected


def test_sum():
    a = 4
    b = 8
    assert a + b == 12

def test_deposit_negative():
    account = BankAccount(balance=1000, log_file="transaction_log.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)
