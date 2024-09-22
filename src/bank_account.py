from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError
from datetime import datetime

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(message + "\n")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("No se puede depositar una cantidad negativa")
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Depósito de {amount}. Nuevo saldo: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        today = now.weekday()
        if today == 5 or today == 6:
            raise WithdrawalDayRestrictionError("No se puede retirar en este día")
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("No se puede retirar en este horario")
        if amount > self.balance:
            raise InsufficientFundsError(f"Saldo insuficiente. Saldo actual: {self.balance}")
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Retiro de {amount}. Nuevo saldo: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Solicitud de saldo. Saldo actual: {self.balance}")
        return self.balance

    def transfer(self, amount):
        if amount > 0 and self.balance >= amount:
            self.withdraw(amount)
            return self.balance
        else:
            self._log_transaction(f"Insufficient funds")
            raise  ValueError("Insufficient funds")
