""" 1.  Банковский счёт и 2. История операций """


class WithdrawError(ValueError):
    """ Raised when withdrawal amount exceeds balance. """
    pass

class DepositError(ValueError):
    """ Raised when deposit amount is invalid. """
    pass

class BankAccount:
    def __init__(self, owner_name, balance=0):
        self._name = owner_name
        self.__balance = balance
        self._history = list()
    
    def deposit(self, amount):
        if amount <= 0:
            raise DepositError("Deposit amount must be positive.")
        self.__balance += amount
        self._add_history("Deposit", amount)
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise WithdrawError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise WithdrawError("Not enough funds.")
        self.__balance -= amount
        self._add_history("Withdraw", amount)
        return self.__balance

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    def _add_history(self, operation, amount):
        self._history.append(f"{operation}: {amount}")


    @property
    def history(self):
        return self._history

wallet = BankAccount('Ruslan', 1000000)

try:
    wallet.show_balance()
    wallet.deposit(-5000)
except DepositError as e:
    print(f"Error: {e}")

try:
    wallet.show_balance()
    wallet.withdraw(1000005)
except WithdrawError as e:
    print(f"Error: {e}")


wallet.deposit(5500)
wallet.show_balance()
wallet.withdraw(50000)
wallet.show_balance()
wallet.__balance = 1231231231
wallet.show_balance()




print(f"Operation history")
for record in wallet.history:
    print(f"\t{record}")


# print(wallet.__dict__)