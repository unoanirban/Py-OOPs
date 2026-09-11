"""
## Problem 2 — Person with a Computed Full Name

### What you'll learn
- Read-only computed properties (no setter)
- Properties that combine multiple attributes

### Context
A registry stores a person's first name and last name separately,
but we want to read the full name as person.full_name — a computed value.

### Requirements
Create a Person class:

1. Constructor (__init__):
   - Parameters: first_name, last_name, age
   - Store each as self.first_name, self.last_name, self.age (age uses setter)

2. Property full_name (read-only — no setter):
   - Getter: Returns f"{self.first_name} {self.last_name}"

3. Property age:
   - Getter: returns self._age
   - Setter: if value < 0 or value > 120, print "Invalid age." and do nothing.
             Otherwise update self._age.

4. Method:
   - get_info(): Returns "<full_name>, Age: <age>"

### Sample Run
p = Person("Rahul", "Dravid", 45)
print(p.full_name)    # Rahul Dravid
print(p.get_info())   # Rahul Dravid, Age: 45

p.age = 50
print(p.age)          # 50

p.age = -5            # Invalid age.
print(p.age)          # 50 (unchanged)

p.first_name = "Sachin"
print(p.full_name)    # Sachin Dravid

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

