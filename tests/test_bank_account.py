import unittest, os
from unittest.mock import patch

from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError

class BankAccountTests(unittest.TestCase):

        def setUp(self) -> None:
            self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

        def tearDown(self) -> None:
            if os.path.exists(self.account.log_file):
                os.remove(self.account.log_file)

        def _count_lines(self, filename):
            with open(filename, "r") as f:
                return len(f.readlines())

        def test_deposit(self):
            new_balance = self.account.deposit(500)
            self.assertEqual(new_balance, 1500, "El balance no es igual")

        @patch("src.bank_account.datetime")
        def test_withdraw(self, mock_datetime):
            mock_datetime.now.return_value.hour = 10
            new_balance = self.account.withdraw(200)
            self.assertEqual(new_balance, 800, "El balance no es igual")

        def test_get_balance(self):
            self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual") # self.account.get_balance() == 1000

        @patch("src.bank_account.datetime")
        def test_transfer(self, mock_datetime):
            mock_datetime.now.return_value.hour = 10
            new_balance = self.account.transfer(200)
            assert new_balance == 800

        @patch("src.bank_account.datetime")
        def test_transfer_no_funds(self, mock_datetime):
            mock_datetime.now.return_value.hour = 10
            with self.assertRaises(ValueError):
                new_balance = self.account.transfer(2000)


        def test_transaction_log(self):
            self.account.deposit(500)
            self.assertTrue(os.path.exists("transaction_log.txt"))

        def test_count_transactions(self):
            assert self._count_lines(self.account.log_file) == 1
            self.account.deposit(500)
            assert self._count_lines(self.account.log_file) == 2

        @patch("src.bank_account.datetime")
        def test_withdraw_raise_error_when_insufficient_funds(self, mock_datetime):
            mock_datetime.now.return_value.hour = 10
            with self.assertRaises(InsufficientFundsError):
                self.account.withdraw(1200)

        @patch("src.bank_account.datetime")
        def test_withdraw_during_business_hours(self, mock_datetime):
            mock_datetime.now.return_value.hour = 10
            new_balance = self.account.withdraw(200)
            self.assertEqual(new_balance, 800)

        @patch("src.bank_account.datetime")
        def test_withdraw_raises_before_business_hours(self, mock_datetime):
            mock_datetime.now.return_value.hour = 7
            with self.assertRaises(WithdrawalTimeRestrictionError):
                new_balance = self.account.withdraw(200)

        @patch("src.bank_account.datetime")
        def test_withdraw_raises_after_business_hours(self, mock_datetime):
            mock_datetime.now.return_value.hour = 19
            with self.assertRaises(WithdrawalTimeRestrictionError):
                new_balance = self.account.withdraw(200)

        @patch("src.bank_account.datetime")
        def test_withdraw_during_business_days(self, mock_datetime):
            mock_datetime.now.return_value.weekday.return_value = 0 #Monday
            mock_datetime.now.return_value.hour = 10
            new_balance = self.account.withdraw(200)
            self.assertEqual(new_balance, 800)

        @patch("src.bank_account.datetime")
        def test_withdraw_out_of_business_days(self, mock_datetime):
            mock_datetime.now.return_value.weekday.return_value = 6 #Sunday
            mock_datetime.now.return_value.hour = 1
            with self.assertRaises(WithdrawalDayRestrictionError):
                new_balance = self.account.withdraw(200)

        def test_deposit_various_values(self):
            test_cases = [
                {"amount": 100, "expected": 1100},
                {"amount": 500, "expected": 1500},
                {"amount": 200, "expected": 1200},
                {"amount": 0, "expected": 1000},
            ]

            for case in test_cases:
                with self.subTest(case=case):
                    self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
                    new_balance = self.account.deposit(case["amount"])
                    self.assertEqual(new_balance, case["expected"])
