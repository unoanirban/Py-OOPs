"""
## Problem 2 — Employee Types

### What you'll learn
- Overriding a method AND using super() to keep the parent's behaviour too
- Adding to the parent's method rather than replacing it entirely

### Requirements

Base class Employee:
   __init__(self, name, salary)
   get_description(): Returns "Employee: <name>, Salary: $<salary>"
   apply_raise(percent): Increases salary by percent. Prints "Salary updated to $<new_salary>"

Subclass Manager(Employee):
   __init__(self, name, salary, team_size) — call super().__init__(name, salary)
   Overrides get_description():
       Call super().get_description() for the base part.
       Return that + ", Team Size: <team_size>"
   Overrides apply_raise(percent):
       Managers get extra 5% — call super().apply_raise(percent + 5)

### Sample Run
emp = Employee("Ravi", 50000)
print(emp.get_description())   # Employee: Ravi, Salary: $50000
emp.apply_raise(10)            # Salary updated to $55000.0

mgr = Manager("Anita", 80000, 8)
print(mgr.get_description())   # Employee: Anita, Salary: $80000, Team Size: 8
mgr.apply_raise(10)            # Salary updated to $92000.0  (10% + 5% bonus = 15%)

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

