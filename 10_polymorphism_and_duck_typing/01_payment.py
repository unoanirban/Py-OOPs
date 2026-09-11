"""
## Problem 1 — Payment Methods

### Requirements

Class CreditCard:
   __init__(self, card_number, holder_name)
   pay(amount): Prints "Paid $<amount> via Credit Card ending in <last 4 digits>."

Class UPI:
   __init__(self, upi_id)
   pay(amount): Prints "Paid $<amount> via UPI (<upi_id>)."

Class Cash:
   pay(amount): Prints "Paid $<amount> in cash."

Function process_payment(payment_method, amount):
   Just calls payment_method.pay(amount)

### Sample Run
cc = CreditCard("4111222233334444", "Rahul")
upi = UPI("rahul@okaxis")
cash = Cash()

process_payment(cc, 1500)    # Paid $1500 via Credit Card ending in 4444.
process_payment(upi, 800)    # Paid $800 via UPI (rahul@okaxis).
process_payment(cash, 200)   # Paid $200 in cash.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

