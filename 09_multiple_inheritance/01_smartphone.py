"""
## Problem 1 — Smartphone (Phone + Camera)

### Requirements

Class Phone:
   __init__(self, brand, phone_number)
   call(number): Prints "Calling <number> from <phone_number>..."
   send_sms(number, message): Prints "SMS to <number>: <message>"

Class Camera:
   __init__(self, megapixels)
   take_photo(): Prints "Photo taken with <megapixels> MP camera!"
   record_video(seconds): Prints "Recording <seconds>s video..."

Class Smartphone(Phone, Camera):
   __init__(self, brand, phone_number, megapixels, model)
       Call Phone.__init__ and Camera.__init__ separately.
   get_info(): Returns "<brand> <model> | <megapixels> MP | <phone_number>"

### Sample Run
phone = Smartphone("Samsung", "+91-9876543210", 108, "Galaxy S24")
print(phone.get_info())
phone.call("+91-9123456789")
phone.take_photo()
phone.record_video(30)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

