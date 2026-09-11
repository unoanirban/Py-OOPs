"""
## Problem 1 — School with a Shared Name

### What you'll learn
- Defining a class attribute (shared across all instances)
- Using a @classmethod to change it for all instances at once

### Context
All students in a school share the same school name. When the school is
renamed, every student's school name should update automatically.

### Requirements
Create a Student class:

1. Class attribute: school_name = "Sunrise Public School"
   (defined directly in the class body, not in __init__)

2. Constructor (__init__):
   - Parameters: name, roll_no

3. Class method:
   - change_school_name(new_name): Updates school_name for ALL students.

4. Instance method:
   - get_info(): Returns "Rahul [Roll: 101] — School: Sunrise Public School"

### Sample Run
s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)

print(s1.get_info())  # Rahul [Roll: 101] — School: Sunrise Public School
Student.change_school_name("Greenfield Academy")
print(s1.get_info())  # Rahul [Roll: 101] — School: Greenfield Academy
print(s2.get_info())  # Priya [Roll: 102] — School: Greenfield Academy

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

