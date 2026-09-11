"""
## Problem 3 — Creating Objects from Different Data Formats

### What you'll learn
- Using @classmethod as an alternative constructor (factory method)
- This lets you create objects from different input formats

### Context
A book catalog receives book data in two formats: sometimes as a
comma-separated string, and sometimes as a dictionary.

### Requirements
Create a Book class:

1. Constructor (__init__):
   - Parameters: title, author, price

2. Class methods (alternative constructors):
   - from_csv(csv_string):
       Input: "Clean Code,Robert Martin,45.0"
       Split by comma, create and return a Book object.

   - from_dict(data_dict):
       Input: {"title": "Clean Code", "author": "Robert Martin", "price": 45.0}
       Pull values from the dict and return a Book object.

3. Instance method:
   - get_details(): Returns "'<title>' by <author> — $<price>"

### Sample Run
b1 = Book("Python Tricks", "Dan Bader", 35.0)
b2 = Book.from_csv("Clean Code,Robert Martin,45.0")
b3 = Book.from_dict({"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "price": 50.0})

print(b1.get_details())  # 'Python Tricks' by Dan Bader — $35.0
print(b2.get_details())  # 'Clean Code' by Robert Martin — $45.0
print(b3.get_details())  # 'The Pragmatic Programmer' by Hunt & Thomas — $50.0

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

