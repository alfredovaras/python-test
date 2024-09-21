import unittest, os
from faker import Faker
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale='es')
        self.user = User(name=self.faker.name(), email=self.faker.email())


    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name_generated, email_generated)
        #print(user.name, user.email)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)

    def test_user_with_multiple_accounts(self):
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=1000, max=10000, step=1000),
                log_file=self.faker.file_name(extension="txt")
            )
            self.user.add_account(account=bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)

        self.assertEqual(value, expected_value)

    def tearDown(self) -> None:
        for account in self.user.accounts:
            if os.path.exists(account.log_file):
                os.remove(account.log_file)
