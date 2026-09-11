# Practice Problems: Multiple Inheritance

Learn how a class can inherit from **more than one** parent class, and understand Python's **Method Resolution Order (MRO)** — the rule Python follows to decide which method to use when multiple parents define the same one.

> **Key idea:** In Python, a class can inherit from multiple parents: `class C(A, B)`. If both `A` and `B` have a method called `speak()`, Python uses **MRO** to decide whose version runs. The MRO order goes from left to right: `C` → `A` → `B`. Use `ClassName.__mro__` to see the order.

---

## Problem 1 — Smartphone (Phone + Camera)

### Problem Statement
Modern consumer electronics frequently merge capabilities from previously separate hardware devices into a single convergence product. A smartphone, for instance, serves as both a telecommunications handset (placing voice calls and sending SMS text messages) and a digital camera (capturing high-resolution still photos and recording video clips).

Instead of re-implementing cellular telephony logic and digital optics processing from scratch within a new monolithic class, an object-oriented design can model convergence through multiple inheritance. You need to build independent `Phone` and `Camera` base classes, and then derive a `Smartphone` subclass that inherits from both parents simultaneously, initializing their respective states and integrating both sets of device behaviors into a unified product.

### What You'll Learn
- Deriving a single subclass from multiple unrelated base classes (`class Smartphone(Phone, Camera)`)
- Initializing multiple parent classes within the subclass constructor
- Exposing combined multi-parent capabilities through a single unified instance

### Requirements & Specifications

1. **Class `Phone`**:
   - Constructor: `__init__(self, brand, phone_number)`
   - Method `call(number)`: Prints `"Calling <number> from <phone_number>..."`
   - Method `send_sms(number, message)`: Prints `"SMS to <number>: <message>"`

2. **Class `Camera`**:
   - Constructor: `__init__(self, megapixels)`
   - Method `take_photo()`: Prints `"Photo taken with <megapixels> MP camera!"`
   - Method `record_video(seconds)`: Prints `"Recording <seconds>s video..."`

3. **Class `Smartphone(Phone, Camera)`**:
   - Constructor: `__init__(self, brand, phone_number, megapixels, model)`
   - Call `Phone.__init__(self, brand, phone_number)`.
   - Call `Camera.__init__(self, megapixels)`.
   - Add `self.model = model`.
   - Method `get_info()`: Returns `"<brand> <model> | <megapixels> MP | <phone_number>"`

### Sample Run
```python
phone = Smartphone("Samsung", "+91-9876543210", 108, "Galaxy S24")
print(phone.get_info())               # Samsung Galaxy S24 | 108 MP | +91-9876543210
phone.call("+91-9123456789")          # Calling +91-9123456789 from +91-9876543210...
phone.send_sms("+91-9123456789", "Hi!")  # SMS to +91-9123456789: Hi!
phone.take_photo()                    # Photo taken with 108 MP camera!
phone.record_video(30)                # Recording 30s video...
```

---

## Problem 2 — Teaching Assistant (Student + Teacher)

### Problem Statement
In higher education administration, graduate Teaching Assistants (TAs) occupy a dual academic role. On one hand, a TA is an enrolled graduate student with a student ID who studies advanced academic subjects. On the other hand, a TA is an employed instructional staff member with an employee ID who leads lab sections and teaches undergraduate students.

When two parent classes (`Student` and `Teacher`) define overlapping method names (such as `get_role()`), a multiple inheritance collision arises. You need to model this scenario by constructing `Student` and `Teacher` classes, and then defining a `TeachingAssistant` class that inherits from both. The subclass must resolve method ambiguities by explicitly overriding `get_role()` to reflect its unique combined identity, while providing a comprehensive academic profile that unifies both identification numbers.

### What You'll Learn
- Resolving method collisions when multiple parent classes define identical method names
- Combining disparate domain identities into a coherent multi-role class
- Inspecting Python's Method Resolution Order (`__mro__`) to verify inheritance precedence

### Requirements & Specifications

1. **Class `Student`**:
   - Constructor: `__init__(self, name, student_id)`
   - Method `study(subject)`: Prints `"<name> is studying <subject>."`
   - Method `get_role()`: Returns `"Student"`

2. **Class `Teacher`**:
   - Constructor: `__init__(self, name, employee_id)`
   - Method `teach(subject)`: Prints `"<name> is teaching <subject>."`
   - Method `get_role()`: Returns `"Teacher"`

3. **Class `TeachingAssistant(Student, Teacher)`**:
   - Constructor: `__init__(self, name, student_id, employee_id, department)`
   - Call `Student.__init__(self, name, student_id)`.
   - Call `Teacher.__init__(self, name, employee_id)`.
   - Add `self.department = department`.
   - Method `get_role()`: Returns `"Teaching Assistant in <department>"`
   - Method `full_profile()`: Returns:
     ```
     Name: <name> | Role: Teaching Assistant in <dept> | Student ID: <sid> | Employee ID: <eid>
     ```

### Sample Run
```python
ta = TeachingAssistant("Priya", "S2024", "E1045", "Computer Science")
print(ta.get_role())       # Teaching Assistant in Computer Science
ta.study("Algorithms")     # Priya is studying Algorithms.
ta.teach("Python Lab")     # Priya is teaching Python Lab.
print(ta.full_profile())
# Name: Priya | Role: Teaching Assistant in Computer Science | Student ID: S2024 | Employee ID: E1045

# Check MRO:
print(TeachingAssistant.__mro__)
```

---

## Problem 3 — Exploring MRO

### Problem Statement
In object-oriented architectures utilizing multiple inheritance, the "diamond problem" occurs when a class `D` inherits from two sibling classes `B` and `C`, both of which inherit from a common ancestor `A`. Without a rigorous dispatch resolution algorithm, diamond inheritance risks duplicate method executions and ambiguous dispatch paths.

Python resolves this challenge deterministically using the C3 Linearization algorithm to produce a strict Method Resolution Order (MRO). In this exercise, you will implement the canonical diamond hierarchy (`A` $\leftarrow$ `B`, `C` $\leftarrow$ `D`) and observe cooperative method chaining via `super().greet()`. You will inspect how calls traverse the linearization chain seamlessly (`D` $\rightarrow$ `B` $\rightarrow$ `C` $\rightarrow$ `A`) and analyze how attribute lookup order works in practice.

### What You'll Learn
- Understanding the mechanics of the classic diamond inheritance pattern
- Implementing cooperative multiple inheritance where `super()` traverses sibling branches in MRO order
- Inspecting and interpreting `ClassName.__mro__` tuples

### Requirements & Specifications

1. **Class `A`** (top of diamond):
   - Method `greet()`: Prints `"Hello from A"`
   - Method `who_am_i()`: Returns `"A"`

2. **Class `B(A)`**:
   - Overrides `greet()`: Prints `"Hello from B"`, then calls `super().greet()`.
   - Overrides `who_am_i()`: Returns `"B"`

3. **Class `C(A)`**:
   - Overrides `greet()`: Prints `"Hello from C"`, then calls `super().greet()`.
   - Overrides `who_am_i()`: Returns `"C"`

4. **Class `D(B, C)`**:
   - Does NOT override any methods — inherits from both.

5. **Demonstrate**:
   - Create `d = D()`.
   - Call `d.greet()` and show what gets printed (should chain through B → C → A).
   - Call `d.who_am_i()` and show what it returns.
   - Print `D.__mro__` and explain the order.

### Sample Run
```python
d = D()
d.greet()
# Hello from B
# Hello from C
# Hello from A

print(d.who_am_i())    # B  (first in MRO after D)
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```
