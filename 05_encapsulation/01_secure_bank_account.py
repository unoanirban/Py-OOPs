"""
## Problem 1 — Bank Account with a Hidden Balance

### What you'll learn
- Using self.__attribute to make an attribute private
- Exposing it safely through methods

### Context
A bank account's balance should not be directly changeable from outside.
You must deposit or withdraw to change it. The balance itself is hidden (private).

### Requirements
Create a BankAccount class:

1. Constructor (__init__):
   - Parameters: holder, initial_balance (default = 0)
   - Store balance as a PRIVATE attribute: self.__balance
   - If initial_balance < 0, set to 0 and print "Balance cannot be negative, set to 0."

2. Methods:
   - deposit(amount):
       If amount <= 0, print "Deposit must be positive." and return.
       Add amount to self.__balance.
       Print "Deposited $<amount>. New balance: $<balance>"

   - withdraw(amount):
       If amount <= 0, print "Withdrawal must be positive." and return.
       If amount > self.__balance, print "Insufficient funds." and return.
       Subtract amount.
       Print "Withdrew $<amount>. New balance: $<balance>"

   - get_balance():
       Returns self.__balance.

### Sample Run
acc = BankAccount("Vikram", 1000)
print(acc.get_balance())   # 1000
acc.deposit(500)           # Deposited $500. New balance: $1500
acc.withdraw(200)          # Withdrew $200. New balance: $1300
print(acc.get_balance())   # 1300
# print(acc.__balance)     # This would cause an error!

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

