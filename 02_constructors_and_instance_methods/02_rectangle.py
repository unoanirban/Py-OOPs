"""
## Problem 2 — Rectangle Calculator

### What you'll learn
- Validating constructor arguments
- Simple computed methods

### Context
A geometry app needs a Rectangle class. A rectangle can't have zero or
negative dimensions, so we validate in __init__.

### Requirements
Create a Rectangle class:

1. Constructor (__init__):
   - Parameters: length, width
   - If either is <= 0, print "Length and width must be greater than zero."
     and set them to 1 as a fallback.

2. Methods:
   - area(): Returns length * width.
   - perimeter(): Returns 2 * (length + width).
   - is_square(): Returns True if length == width, else False.
   - scale(factor):
       If factor <= 0, print "Scale factor must be positive." and do nothing.
       Otherwise, multiply both length and width by factor.

### Sample Run
r = Rectangle(10, 5)
print(r.area())       # 50
print(r.perimeter())  # 30
print(r.is_square())  # False

r.scale(2)
print(r.length)  # 20
print(r.width)   # 10
print(r.area())  # 200

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

