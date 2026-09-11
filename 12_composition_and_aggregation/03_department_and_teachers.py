"""
## Problem 3 — Department and Teachers (Aggregation)

### Requirements

Class Teacher:
   __init__(self, name, subject, years_experience)
   get_profile(): Returns "<name> | <subject> | <years_experience> yrs exp"

Class Department:
   __init__(self, dept_name)
   self.teachers = []
   add_teacher(teacher): Appends a Teacher object.
   remove_teacher(name): Finds and removes teacher by name.
   get_all_teachers(): Prints numbered list of all teachers.
   get_count(): Returns number of teachers.

### Sample Run
t1 = Teacher("Dr. Priya", "Algorithms", 10)
t2 = Teacher("Prof. Kiran", "Databases", 7)
cs_dept = Department("Computer Science")
cs_dept.add_teacher(t1)
cs_dept.add_teacher(t2)
cs_dept.get_all_teachers()
# 1. Dr. Priya | Algorithms | 10 yrs exp
# 2. Prof. Kiran | Databases | 7 yrs exp
cs_dept.remove_teacher("Prof. Kiran")  # Prof. Kiran removed from Computer Science.
# t2 still exists even after removal:
print(t2.get_profile())   # Prof. Kiran | Databases | 7 yrs exp

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

