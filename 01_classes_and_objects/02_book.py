"""
## Problem 2 — Bookstore Inventory

### What you'll learn
- Defining methods that change attribute values (state mutation)
- Using simple if/else inside methods

### Context
A small bookstore needs a program to track books. Each book has a title,
author, price, and how many copies are in stock.

### Requirements
Create a Book class:

1. Constructor (__init__):
   - Parameters: title, author, price, stock

2. Methods:
   - apply_discount(percentage):
       Reduces price by the given percentage.
       Example: if price is 100 and percentage is 20, new price = 80.
       If percentage is not between 1 and 100, print "Invalid discount"
       and don't change the price.

   - is_in_stock(): Returns True if there's at least 1 copy, False otherwise.

   - sell(quantity):
       If quantity is available in stock, reduce stock and return True.
       If not enough stock, print "Not enough stock" and return False.

   - get_details(): Returns a string like:
       'Clean Code' by Robert C. Martin - $36.00 (Stock: 2 copies)

### Sample Run
b = Book("Clean Code", "Robert C. Martin", 45.0, 5)

print(b.get_details())   # 'Clean Code' by Robert C. Martin - $45.00 (Stock: 5 copies)
b.apply_discount(20)
print(b.price)           # 36.0
print(b.sell(3))         # True
print(b.sell(5))         # Not enough stock → False
print(b.is_in_stock())   # True (2 copies left)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:
