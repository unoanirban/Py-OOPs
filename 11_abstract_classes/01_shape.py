"""
## Problem 1 — Shapes with Enforced Area

### What you'll learn
- How to create an abstract class with ABC
- How @abstractmethod forces subclasses to implement specific methods

### Requirements

Abstract base class Shape (inherits from ABC):
   @abstractmethod area(): No body — subclasses must implement.
   @abstractmethod perimeter(): Same.
   Regular method describe(): Prints "Shape area: <area>, Perimeter: <perimeter>"

Class Circle(Shape):
   __init__(self, radius)
   area(): Returns 3.14 * radius * radius
   perimeter(): Returns 2 * 3.14 * radius

Class Rectangle(Shape):
   __init__(self, length, width)
   area(): Returns length * width
   perimeter(): Returns 2 * (length + width)

### Sample Run
# Shape()    # ← Raises TypeError — try it!

c = Circle(7)
print(c.area())         # 153.86
print(c.perimeter())    # 43.96
c.describe()            # Shape area: 153.86, Perimeter: 43.96

r = Rectangle(5, 3)
r.describe()            # Shape area: 15, Perimeter: 16

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

from abc import ABC, abstractmethod

# Write your solution here:

