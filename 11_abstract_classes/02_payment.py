"""
## Problem 2 — Payment Gateway

### Requirements

Abstract base class PaymentGateway (inherits from ABC):
   @abstractmethod process_payment(amount): Returns True/False.
   @abstractmethod get_transaction_id(): Returns a string transaction ID.
   Regular method print_receipt(amount):
       If payment succeeds: "Payment of $<amount> successful! TXN: <txn_id>"
       If it fails: "Payment failed."

Class RazorpayGateway(PaymentGateway):
   __init__(self, api_key)
   process_payment(amount): Set self._txn_id = f"RPY_{amount}", return True.
   get_transaction_id(): Returns self._txn_id

Class PayPalGateway(PaymentGateway):
   __init__(self, email)
   process_payment(amount): Succeeds only if amount <= 10000.
   get_transaction_id(): Returns self._txn_id

### Sample Run
razorpay = RazorpayGateway("key_test_abc123")
razorpay.print_receipt(500)    # Payment of $500 successful! TXN: RPY_500

paypal = PayPalGateway("user@paypal.com")
paypal.print_receipt(8000)     # Payment of $8000 successful! TXN: PPL_8000
paypal.print_receipt(15000)    # Payment failed.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

from abc import ABC, abstractmethod

# Write your solution here:

