"""
## Problem 3 — Bank Account with Transaction History

### What you'll learn
- Storing a list as an attribute
- Appending to the list inside methods to keep a history

### Context
A bank account tracks every deposit and withdrawal. The account starts
with an opening balance, and every transaction is recorded in a list.

### Requirements
Create a BankAccount class:

1. Constructor (__init__):
   - Parameters: holder, account_number, initial_balance (default = 0)
   - If initial_balance < 0, print "Balance cannot be negative." and set to 0.
   - Create a transactions list and add the first entry:
       "Account opened with $<amount>"

2. Methods:
   - deposit(amount):
       If amount <= 0, print "Deposit must be greater than zero." and return False.
       Add amount to balance, record the transaction, return True.

   - withdraw(amount):
       If amount <= 0, print "Withdrawal must be greater than zero." and return False.
       If amount > balance, print "Insufficient funds." and return False.
       Subtract amount, record the transaction, return True.

   - get_statement():
       Prints all transaction entries, one per line.

### Sample Run
acc = BankAccount("Neha Gupta", "ACC12345", 500)
acc.deposit(200)
acc.withdraw(150)
acc.withdraw(1000)   # Insufficient funds.
acc.get_statement()

# Account opened with $500
# Deposited: $200 | Balance: $700
# Withdrew: $150 | Balance: $550

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

