"""
## Problem 2 — Teaching Assistant (Student + Teacher)

### Requirements

Class Student:
   __init__(self, name, student_id)
   study(subject): Prints "<name> is studying <subject>."
   get_role(): Returns "Student"

Class Teacher:
   __init__(self, name, employee_id)
   teach(subject): Prints "<name> is teaching <subject>."
   get_role(): Returns "Teacher"

Class TeachingAssistant(Student, Teacher):
   __init__(self, name, student_id, employee_id, department)
       Call Student.__init__ and Teacher.__init__ separately.
   get_role(): Returns "Teaching Assistant in <department>"
   full_profile(): Returns formatted string with all details.

### Sample Run
ta = TeachingAssistant("Priya", "S2024", "E1045", "Computer Science")
print(ta.get_role())       # Teaching Assistant in Computer Science
ta.study("Algorithms")     # Priya is studying Algorithms.
ta.teach("Python Lab")     # Priya is teaching Python Lab.
print(ta.full_profile())
print(TeachingAssistant.__mro__)  # See the MRO order

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

