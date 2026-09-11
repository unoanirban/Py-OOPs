"""
## Problem 1 — Student Report Card

### What you'll learn
- How to define a class with __init__
- How to store data as attributes (self.name, etc.)
- How to write simple methods that read those attributes

### Context
A teacher wants a simple program to store a student's marks
in three subjects and calculate their average and grade.

### Requirements
Create a Student class:

1. Constructor (__init__):
   - Parameters: name, roll_no, math_marks, science_marks, english_marks
   - Store each as an attribute using self

2. Methods:
   - calculate_average(): Returns the average of the three subject marks.
       Formula: (math_marks + science_marks + english_marks) / 3

   - get_grade(): Returns a letter grade based on the average:
       >= 90 → "A"
       >= 80 → "B"
       >= 70 → "C"
       >= 60 → "D"
       Below 60 → "F"

   - display_report(): Prints a summary like:
       Roll No: 101 | Name: Rahul Sharma | Average: 86.33 | Grade: B

### Sample Run
s1 = Student("Rahul Sharma", 101, 88, 92, 79)

print(s1.calculate_average())  # 86.33333...
print(s1.get_grade())          # B
s1.display_report()
# Roll No: 101 | Name: Rahul Sharma | Average: 86.33 | Grade: B

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

class Student:

    def __init__(self, name, roll, english_marks, math_marks, science_marks):
        self.name = name
        self.roll = roll
        self.english_marks = english_marks
        self.math_marks = math_marks
        self.science_marks = science_marks

    def avg_marks(self):
        return (self.english_marks + self.math_marks + self.science_marks) / 3
    
    def grade(self):
        if self.avg_marks() >= 90:
            return "A"
        elif self.avg_marks() >= 80:
            return "B"
        elif self.avg_marks() >= 70:
            return "C"
        elif self.avg_marks() >= 60:
            return "D"
        else:
            return "F"
    
    def report(self):
        print(f"Roll No: {self.roll} | Name: {self.name} | Average: {self.avg_marks()} | Grade: {self.grade()}")

s1 = Student("Rohit Sharma", 45, 88, 92, 79)
s2 = Student("Virat Kohli", 18, 99, 91, 97)

print(s1.avg_marks())
print(s1.grade())
s1.report()
s2.report()