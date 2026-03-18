class Account:

    def __init__(self, account_num: int, holder_name: str, balance: float):
        self.account_num: int = account_num
        self.holder_name: str = holder_name
        self.__balance: float = balance

    def withdraw(self, amount: int):
        if amount > self.balance:
            return "insufficient fund"

        elif amount < 0:
            return "Enter valid amount"

        else:
            self.__balance = self.__balance - amount
            return "amount withdraw successful"

    def deposit(self, amount: int):
        self.__balance += amount
        total_balance: float = self.__balance
        return total_balance

    def account_details(self):

        return [self.account_num, self.holder_name, self.balance]

    @property
    def balance(self):
        return self.__balance


class SavingAccount(Account):
    def withdraw(self, amount: int):

        return super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount: int):
        if amount <= self.balance:
            return super().withdraw(amount)
        else:
            return [super().withdraw(amount),"overdraft occured "]



class Bank:
 ...