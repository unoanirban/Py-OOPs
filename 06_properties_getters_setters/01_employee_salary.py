"""
## Problem 1 — Employee Salary with Validation

### What you'll learn
- How to write a property getter and setter
- Using @property to validate a value before storing it

### Context
An HR system has an Employee class. The salary cannot be negative.
Using @property, we can validate the salary every time someone tries to set it.

### Requirements
Create an Employee class:

1. Constructor (__init__):
   - Parameters: name, salary
   - Write self.salary = salary — this will call the setter automatically.

2. Property salary:
   - Getter: returns self._salary
   - Setter: if value < 0, print "Salary cannot be negative." and set self._salary = 0.
             Otherwise set self._salary = value.

3. Method:
   - get_info(): Returns "<name> earns $<salary> per month"

### Sample Run
emp = Employee("Rahul", 5000)
print(emp.salary)        # 5000
print(emp.get_info())    # Rahul earns $5000 per month

emp.salary = 7000        # updates via setter
print(emp.salary)        # 7000

emp.salary = -500        # Salary cannot be negative.
print(emp.salary)        # 0 (fallback)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

