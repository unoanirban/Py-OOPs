"""
## Problem 2 — Counting How Many Objects Exist

### What you'll learn
- Using a class attribute as a counter that increments with every new object
- Accessing the count through a class method

### Context
A hospital system needs to know how many Patient objects have been created
in total, at any point in time.

### Requirements
Create a Patient class:

1. Class attribute: total_patients = 0

2. Constructor (__init__):
   - Parameters: name, age
   - Increment Patient.total_patients by 1 each time a new patient is created.

3. Class method:
   - get_total_patients(): Returns the value of total_patients.

4. Instance method:
   - get_info(): Returns "Patient: <name>, Age: <age>"

### Sample Run
print(Patient.get_total_patients())   # 0

p1 = Patient("Arjun", 30)
p2 = Patient("Deepa", 25)
p3 = Patient("Mohan", 45)

print(Patient.get_total_patients())   # 3
print(p1.get_info())                  # Patient: Arjun, Age: 30

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

