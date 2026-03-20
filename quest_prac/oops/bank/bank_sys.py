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
        return {
            "account_number": self.account_num,
            "holder_name": self.holder_name,
            "balance": self.balance,
        }

    @property
    def balance(self):
        return self.__balance


class SavingAccount(Account):
    def withdraw(self, amount: int):

        return super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount: int):
        if amount < 0:
            return "Enter valid amount"

        if amount <= self.balance:
            return super().withdraw(amount)
        else:
            # Access Account's private balance for overdraft behavior.
            self._Account__balance -= amount
            return "amount withdraw successful with overdraft"


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}

    def add_account(self, account: Account):
        self.accounts[account.account_num] = account

    def get_account_details(self, account_num: int):
        account = self.accounts.get(account_num)
        if account is None:
            return "Account not found"

        return account.account_details()
