import bank_sys

bank = bank_sys.Bank()
account1 = bank_sys.SavingAccount(12345, "John Doe", 1000.0)
account2 = bank_sys.CurrentAccount(67890, "Jane Smith", 500.0)

bank.add_account(account1)
bank.add_account(account2)

print(bank.get_account_details(12345))
print(bank.get_account_details(67890))
print(bank)