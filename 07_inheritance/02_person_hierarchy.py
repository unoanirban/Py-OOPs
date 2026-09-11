"""
## Problem 2 — University Community

### What you'll learn
- A base class shared by two different subclasses
- Each subclass extending with its own unique attributes and methods

### Requirements

Base class Person:
   __init__(self, name, email, id_number)
   display_badge(): Returns "ID: <id_number> | <name> (<email>)"

Subclass Student(Person):
   __init__(self, name, email, id_number, major)
   self.courses = []
   enroll(course_name): Add course if not already enrolled.
   get_summary(): Returns "<name> | Major: <major> | Courses: <count> enrolled"

Subclass Teacher(Person):
   __init__(self, name, email, id_number, department, subject)
   teach(): Prints "Prof. <name> is teaching <subject> in <department>."

### Sample Run
student = Student("Aarav", "aarav@uni.edu", "S101", "Computer Science")
print(student.display_badge())   # ID: S101 | Aarav (aarav@uni.edu)
student.enroll("Math 101")       # Enrolled in Math 101.
student.enroll("Math 101")       # Already enrolled.
print(student.get_summary())     # Aarav | Major: Computer Science | Courses: 1 enrolled

teacher = Teacher("Dr. Meera", "meera@uni.edu", "T45", "CS Dept", "Data Structures")
teacher.teach()   # Prof. Dr. Meera is teaching Data Structures in CS Dept.

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

