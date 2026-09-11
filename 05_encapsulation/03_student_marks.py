"""
## Problem 3 — Student Grade Book with Data Protection

### What you'll learn
- Private dictionary attribute
- Returning a copy to prevent external modification

### Context
A grade book stores a student's marks. The marks should be readable but
protected — external code should not directly edit the internal dictionary.

### Requirements
Create a GradeBook class:

1. Constructor (__init__):
   - Parameter: student_name
   - self.__grades = {}  (private dictionary, subject → score)

2. Methods:
   - add_grade(subject, score):
       If score < 0 or score > 100, print "Score must be between 0 and 100." and return.
       Add the subject and score to self.__grades.

   - get_grade(subject):
       Return the score for that subject, or None if not found.

   - get_average():
       If no grades, return 0. Otherwise return the average of all scores.

   - get_all_grades():
       Returns a COPY of the grades dict: dict(self.__grades)

### Sample Run
gb = GradeBook("Ananya")
gb.add_grade("Math", 92)
gb.add_grade("Science", 85)

print(gb.get_grade("Math"))   # 92
print(gb.get_average())       # 88.5

grades_copy = gb.get_all_grades()
grades_copy["Math"] = 0       # Try to tamper with it

print(gb.get_grade("Math"))   # Still 92 — the original is safe!

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

