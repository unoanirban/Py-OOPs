"""
## Problem 3 — Shapes with Area

### What you'll learn
- Multiple subclasses each overriding the same method differently
- Using a common interface (area()) across different shapes

### Requirements

Base class Shape:
   __init__(self, color)
   area(): Returns 0 (placeholder)
   describe(): Prints "I am a <color> shape with area <area>"
               (calls self.area() so it uses the overridden version!)

Subclass Circle(Shape):
   __init__(self, color, radius)
   area(): Returns 3.14 * radius * radius

Subclass Rectangle(Shape):
   __init__(self, color, length, width)
   area(): Returns length * width

Subclass Triangle(Shape):
   __init__(self, color, base, height)
   area(): Returns 0.5 * base * height

### Sample Run
c = Circle("red", 5)
print(c.area())   # 78.5
c.describe()      # I am a red shape with area 78.5

r = Rectangle("blue", 4, 6)
print(r.area())   # 24
r.describe()      # I am a blue shape with area 24

t = Triangle("green", 3, 8)
print(t.area())   # 12.0
t.describe()      # I am a green shape with area 12.0

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

