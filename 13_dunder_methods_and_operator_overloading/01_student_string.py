"""
## Problem 1 — Student Profile with __str__, __repr__, __bool__

### Requirements

Class Student:
   __init__(self, name, student_id, gpa)
   __str__: Returns "Student: <name> (ID: <student_id>) | GPA: <gpa>"
   __repr__: Returns "Student('<name>', '<student_id>', <gpa>)"
   __bool__: Returns True if gpa >= 2.0, False otherwise

### Sample Run
s1 = Student("Aarav Patel", "S4001", 3.85)
print(s1)           # Student: Aarav Patel (ID: S4001) | GPA: 3.85
print(repr(s1))     # Student('Aarav Patel', 'S4001', 3.85)
print(bool(s1))     # True

s2 = Student("Rohan", "S4002", 1.5)
print(bool(s2))     # False

if s1:
    print(f"{s1.name} is in good standing.")

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

