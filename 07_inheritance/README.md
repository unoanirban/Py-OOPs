# Module 07 — Inheritance

Inheritance is the second foundational pillar of Object-Oriented Programming. It allows you to create new classes based on existing ones, avoiding code repetition and modeling real-world hierarchies.

---

## 1. Concept Overview: The "Is-A" Relationship

In the real world, things are naturally grouped in categories:
- A **Dog** *is an* **Animal**.
- A **Student** *is a* **Person**.
- A **SavingsAccount** *is a* **BankAccount**.
- A **Sedan** *is a* **Car**, which *is a* **Vehicle**.

When one category is a specialized version of another, we model it in OOP using **Inheritance**:
- **Parent Class (Base Class / Superclass)**: The general class containing common attributes and behaviors.
- **Child Class (Derived Class / Subclass)**: The specialized class that inherits everything from the parent and adds its own unique features.

```
                    +--------------------+
                    |    class Animal    |  <--- Parent / Superclass
                    |  - name            |       (Defines shared basics)
                    |  - age             |
                    |  + eat()           |
                    |  + sleep()         |
                    +--------------------+
                              ^
                             / \
                            /   \
   +-----------------------+     +-----------------------+
   |       class Dog       |     |       class Bird      |  <--- Child / Subclasses
   | (inherits name, age)  |     | (inherits name, age)  |       (Specialized features)
   | + bark()              |     | + fly()               |
   +-----------------------+     +-----------------------+
```

---

## 2. Why Use Inheritance? (The DRY Principle)

Suppose you are building a school management system. Without inheritance, you would write:

```python
# WITHOUT INHERITANCE: Code duplication everywhere!
class Student:
    def __init__(self, name, email, student_id):
        self.name = name
        self.email = email
        self.student_id = student_id

    def send_email(self, message):
        print(f"Email sent to {self.email}: {message}")

class Teacher:
    def __init__(self, name, email, employee_id):
        self.name = name       # Duplicate!
        self.email = email     # Duplicate!
        self.employee_id = employee_id

    def send_email(self, message):  # Duplicate method!
        print(f"Email sent to {self.email}: {message}")
```

Notice how `name`, `email`, and `send_email()` are duplicated! If email logic changes, you must fix it in multiple places.

With **Inheritance**, you write common code **once** in a `Person` class, and let `Student` and `Teacher` inherit it.

---

## 3. Syntax Walkthrough: Creating Child Classes

Here is the clean, inherited implementation:

```python
# 1. Base / Parent Class
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")

    def get_details(self):
        return f"{self.name} ({self.email})"


# 2. Child Class: Put the parent class inside parentheses: class Child(Parent):
class Student(Person):
    def __init__(self, name, email, student_id):
        # Call the parent's __init__ to set up name and email!
        super().__init__(name, email)
        # Add the student-specific attribute
        self.student_id = student_id

    # Add a student-specific method
    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


# 3. Another Child Class
class Teacher(Person):
    def __init__(self, name, email, subject_taught):
        super().__init__(name, email)
        self.subject_taught = subject_taught

    def teach(self):
        print(f"{self.name} is teaching {self.subject_taught}.")
```

---

## 4. Understanding `super().__init__()`

Look closely at this line inside `Student`:
```python
super().__init__(name, email)
```

### What does `super()` do?
`super()` returns a proxy object that delegates method calls to the parent class (`Person`).
- When `Student` runs `super().__init__(name, email)`, it says: *"Hey Person class! Please do your job of initializing `name` and `email` for this new student."*
- Then, `self.student_id = student_id` sets up the attribute unique to `Student`.

### Using the Objects:
```python
s = Student("Aarav", "aarav@school.com", "STU101")

# Child class has access to PARENT methods:
print(s.get_details())                  # Output: Aarav (aarav@school.com)
s.send_email("Exam schedule released")  # Output: Sending email to aarav@school.com: Exam schedule released

# Child class has access to its OWN methods:
s.study("Mathematics")                  # Output: Aarav is studying Mathematics.
```

---

## 5. Type Checking: `isinstance()` and `issubclass()`

Python gives you two built-in functions to test inheritance relationships:

### 1. `isinstance(object, Class)`:
Checks if an object is an instance of a class, OR any of its parent classes:
```python
s = Student("Aarav", "aarav@school.com", "STU101")

print(isinstance(s, Student))  # True: s is a Student
print(isinstance(s, Person))   # True: s is ALSO a Person!
print(isinstance(s, object))   # True: Everything in Python inherits from 'object'!
print(isinstance(s, Teacher))  # False: A Student is not a Teacher
```

### 2. `issubclass(ChildClass, ParentClass)`:
Checks if a class inherits from another class:
```python
print(issubclass(Student, Person))  # True
print(issubclass(Teacher, Person))  # True
print(issubclass(Person, Student))  # False: Person is the parent, not the subclass
```

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Forgetting to Call `super().__init__()` in the Child Class
```python
# WRONG:
class Student(Person):
    def __init__(self, name, email, student_id):
        # Forgot super().__init__(name, email)!
        self.student_id = student_id

s = Student("Aarav", "aarav@mail.com", "STU101")
print(s.name)  # AttributeError: 'Student' object has no attribute 'name'!
```
If you override `__init__` in the child without calling `super().__init__()`, the parent's attributes are never created!

---

### Pitfall 2: Passing `self` to `super()`
```python
# WRONG (Python 2 syntax):
super(self).__init__(name, email)

# CORRECT (Python 3):
super().__init__(name, email)
```
In Python 3, simply call `super().method(...)`. Do not pass `self` as an argument to `super()`.

---

### Pitfall 3: Forcing Inheritance where it Doesn't Belong
Inheritance must represent a true **"Is-A"** relationship:
- A `Dog` is an `Animal` -> **Inheritance is correct!**
- A `Car` has an `Engine` -> **Inheritance is WRONG!** A car is *not* an engine; a car *contains* an engine. (That is **Composition**, covered in Module 12).

---

## 7. Key Takeaways Checklist

Before moving to `problems.md`:
- [ ] What is the syntax for creating a child class? (`class Child(Parent):`)
- [ ] What does `super().__init__(...)` do and why is it necessary?
- [ ] Can a child object call methods defined in its parent class?
- [ ] What is the difference between `isinstance()` and `issubclass()`?
- [ ] Why should you only use inheritance for true "Is-A" relationships?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and start practicing inheritance!
