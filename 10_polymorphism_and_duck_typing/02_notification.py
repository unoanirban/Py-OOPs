"""
## Problem 2 — Notifications

### Requirements

Class EmailNotification:
   __init__(self, email_address)
   send(message): Prints "Email to <email>: <message>"

Class SMSNotification:
   __init__(self, phone_number)
   send(message): Prints "SMS to <phone>: <message>"

Class PushNotification:
   __init__(self, device_token)
   send(message): Prints "Push to <device_token>: <message>"

Function send_all(channels, message):
   Loops through channels and calls .send(message) on each.

### Sample Run
channels = [
    EmailNotification("rahul@gmail.com"),
    SMSNotification("+91-9876543210"),
    PushNotification("device_xyz_789"),
]
send_all(channels, "Your order has been shipped!")

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

