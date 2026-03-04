class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")


s1 = SavingsAccount(1000)
c1 = CurrentAccount(2000)

accounts = [s1, c1]
for acc in accounts:
    acc.account_type()