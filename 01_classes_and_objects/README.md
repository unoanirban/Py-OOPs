# Module 01 — Classes and Objects

Welcome to your first step in Object-Oriented Programming (OOP) in Python! This guide provides the core theory you need before writing code in `problems.md`.

---

## 1. What is Object-Oriented Programming (OOP)?

Until now, you may have written code in a **procedural style**: you define standalone variables and pass them into separate functions:

```python
# Procedural approach: data and functions are separated
student_name = "Aarav"
student_roll = 101
student_math = 85
student_science = 90

def print_student_report(name, roll, math, science):
    avg = (math + science) / 2
    print(f"{name} (Roll: {roll}) - Average: {avg}")

print_student_report(student_name, student_roll, student_math, student_science)
```

**The Problem with this approach:**
- What happens when you have 50 students? You would need 50 sets of loose variables or messy dictionaries.
- If you accidentally pass the wrong variable to the function, bugs happen silently.
- Data and the functions that manipulate that data live completely apart from each other.

**The OOP Solution:**
Object-Oriented Programming lets you **bundle data (attributes) and behavior (methods) together** into a single, organized unit called an **Object**.

---

## 2. The Core Analogy: Blueprint vs. House

To understand OOP, you only need to understand two key concepts: **Class** and **Object**.

```
    CLASS (The Blueprint)                OBJECTS (The Actual Houses)
   +-----------------------+              +-----------------------+
   |      class House      |              | House 1 (Blue paint,  |
   | - color               |  builds ---> |  at 123 Main Street)  |
   | - num_rooms           |              +-----------------------+
   | - open_front_door()   |              +-----------------------+
   +-----------------------+              | House 2 (Yellow paint,|
                                          |  at 456 Oak Avenue)   |
                                          +-----------------------+
```

1. **Class (The Blueprint)**:
   - A class is a template, plan, or blueprint.
   - It specifies what data an object will have and what actions it can perform.
   - **You cannot live inside a blueprint!** A class by itself does not hold real data; it defines the structure.

2. **Object / Instance (The Real Thing)**:
   - An object is an actual, concrete instance built from that blueprint.
   - From one single blueprint, you can build hundreds of independent houses, each with its own color, address, and owner.

Another great analogy:
- A **cookie cutter** is the **Class**.
- The **individual cookies** stamped out of the dough are the **Objects**.

---

## 3. Anatomy of a Python Class

Here is how you write a class in Python:

```python
class Student:
    """A blueprint for representing school students."""

    def __init__(self, name, roll_number, math_marks, science_marks):
        # Attributes (Data stored inside the object)
        self.name = name
        self.roll_number = roll_number
        self.math_marks = math_marks
        self.science_marks = science_marks

    # Method (Behavior / Action the object can perform)
    def calculate_average(self):
        average = (self.math_marks + self.science_marks) / 2
        return average

    # Another Method
    def display_details(self):
        avg = self.calculate_average()
        print(f"Student: {self.name} | Roll: {self.roll_number} | Average: {avg}")
```

Let's break down every single part of this code.

---

## 4. Understanding the Key Components

### A. The `class` Keyword and Naming
```python
class Student:
```
- Use the `class` keyword followed by the name of the class and a colon (`:`).
- **Naming Rule (PEP 8)**: Always use `UpperCamelCase` (capitalize each word, no underscores).
  - Good: `Student`, `BankAccount`, `SmartPhone`
  - Avoid: `student`, `bank_account`

---

### B. The `__init__` Initializer Method
```python
def __init__(self, name, roll_number, math_marks, science_marks):
    self.name = name
    self.roll_number = roll_number
    self.math_marks = math_marks
    self.science_marks = science_marks
```
- `__init__` is a special method (pronounced *"dunder init"*, short for **d**ouble **under**score init).
- It is the **constructor** or **initializer** of the class.
- **When does it run?** Python calls `__init__` **automatically** every time you create a new object.
- **What is its job?** To set up the starting data (called **attributes**) for that specific object.

---

### C. The Mystery of `self` Explained Simply
Beginners are often confused by `self`. Here is the plain English explanation:

> **`self` refers to the specific object currently being worked on.**

When you create two students:
```python
student1 = Student("Aarav", 101, 85, 90)
student2 = Student("Diya", 102, 95, 92)
```
Inside the class code, Python needs to know: *"Whose name should I print? Aarav's or Diya's?"*

- When `student1` calls a method, `self` is `student1`.
- When `student2` calls a method, `self` is `student2`.

**Behind the Scenes:**
When you write:
```python
student1.display_details()
```
Python secretly translates that into:
```python
Student.display_details(student1)  # Python passes student1 as the 'self' parameter!
```
That is why every instance method **must** have `self` as its first parameter!

---

### D. Instance Attributes (Data)
Inside `__init__`, you see lines like:
```python
self.name = name
```
- `name` (on the right) is the temporary parameter passed into the function.
- `self.name` (on the left) attaches that value permanently to this specific object instance.
- This creates an **instance attribute**. Every object gets its own private copy:
  - `student1.name` holds `"Aarav"`
  - `student2.name` holds `"Diya"`
  - Changing `student1.name` has zero effect on `student2.name`.

---

### E. Instance Methods (Actions / Behaviors)
```python
def calculate_average(self):
    return (self.math_marks + self.science_marks) / 2
```
- An **instance method** is a function defined inside a class that operates on the object's data.
- Notice how it uses `self.math_marks` and `self.science_marks` to read the object's own attributes.
- Methods can return values (like numbers or strings) or perform actions.

---

## 5. How to Create and Use Objects (Step-by-Step)

Here is how you use the class in your program:

```python
# Step 1: Instantiate (create) objects from the class
s1 = Student("Aarav", 101, 85, 90)
s2 = Student("Diya", 102, 92, 96)

# Step 2: Access attributes using dot notation (.)
print(s1.name)         # Output: Aarav
print(s2.roll_number)  # Output: 102

# Step 3: Call methods using dot notation (.)
avg1 = s1.calculate_average()
print(f"Aarav's Average: {avg1}")  # Output: 87.5

# Step 4: Call display methods
s1.display_details()  # Output: Student: Aarav | Roll: 101 | Average: 87.5
s2.display_details()  # Output: Student: Diya | Roll: 102 | Average: 94.0
```

### Checking Object Identity:
Each object lives at a different memory location:
```python
print(id(s1))        # e.g., 140238492083280
print(id(s2))        # e.g., 140238492083408 (different!)
print(s1 is s2)      # False: they are two separate objects
```

---

## 6. Common Beginner Pitfalls & How to Avoid Them

### Pitfall 1: Forgetting `self` in Method Definitions
```python
# WRONG:
class Dog:
    def bark():  # Missing self!
        print("Woof!")

d = Dog()
d.bark()  # TypeError: Dog.bark() takes 0 positional arguments but 1 was given!

# CORRECT:
class Dog:
    def bark(self):  # Always include self
        print("Woof!")
```

---

### Pitfall 2: Forgetting `self.` when Accessing Attributes Inside Methods
```python
# WRONG:
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {name}")  # NameError: name 'name' is not defined!

# CORRECT:
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")  # Use self.name!
```

---

### Pitfall 3: Forgetting Parentheses When Calling a Method
```python
# WRONG:
avg = s1.calculate_average   # Missing parentheses ()
print(avg)                   # Prints: <bound method Student.calculate_average of ...>

# CORRECT:
avg = s1.calculate_average() # Added () to actually EXECUTE the method!
print(avg)                   # Prints: 87.5
```

---

### Pitfall 4: Confusing the Class Name with the Instance Variable
```python
# WRONG:
Student.calculate_average()  # TypeError: missing 1 required argument: 'self'

# CORRECT:
s1 = Student("Aarav", 101, 85, 90)  # Create the instance first
s1.calculate_average()               # Call on the instance!
```

---

## 7. Key Takeaways Checklist

Before moving on to the exercises in `problems.md`, ensure you can answer:
- [ ] What is the difference between a class (blueprint) and an object (instance)?
- [ ] What is the purpose of `__init__` and when does it execute?
- [ ] Why must every instance method have `self` as its first parameter?
- [ ] How do you read an attribute using dot notation (`object.attribute`)?
- [ ] How do you call a method using dot notation (`object.method()`)?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and begin solving the exercises step-by-step.
