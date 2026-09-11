# Practice Problems: Class Attributes and Class Methods

Learn the difference between data that belongs to *all* objects of a class (class attributes) and data that belongs to *one specific* object (instance attributes).

> **Key idea:** An *instance attribute* (like `self.name`) is unique to each object. A *class attribute* (like `Student.school_name`) is shared across ALL objects of that class — changing it changes it for everyone.

> **Class methods** are defined with `@classmethod` and receive `cls` (the class itself) instead of `self`. They can read and change class attributes.

---

## Problem 1 — School with a Shared Name

### Problem Statement
A regional educational authority manages student enrollment records across affiliated institutions. While every student possesses individual attributes such as their personal name and assigned roll number, they all share an institutional identity: the name of the school they attend.

If a school undergoes a formal rebranding or structural change (such as renaming from "Sunrise Public School" to "Greenfield Academy"), updating the school name on thousands of individual student records manually is inefficient and prone to synchronization bugs. You need to design an object model where the institution name is stored as shared class-level state. Changing the name via a centralized class method must instantly reflect across all existing and future student profiles.

### What You'll Learn
- Defining class-level attributes shared across all instances of a class
- Writing and invoking `@classmethod` methods that operate on `cls` rather than `self`
- Understanding when to use class state vs. instance state

### Requirements & Specifications
Create a `Student` class:

1. **Class attribute**: `school_name = "Sunrise Public School"` (defined directly in the class body, not in `__init__`)

2. **Constructor (`__init__`)**:
   - Parameters: `name`, `roll_no`

3. **Class method**:
   - `change_school_name(new_name)`: Updates `school_name` for ALL students.

4. **Instance method**:
   - `get_info()`: Returns a string like:
     ```
     Rahul [Roll: 101] — School: Sunrise Public School
     ```

### Sample Run
```python
s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)

print(s1.get_info())   # Rahul [Roll: 101] — School: Sunrise Public School
print(s2.get_info())   # Priya [Roll: 102] — School: Sunrise Public School

Student.change_school_name("Greenfield Academy")

print(s1.get_info())   # Rahul [Roll: 101] — School: Greenfield Academy
print(s2.get_info())   # Priya [Roll: 102] — School: Greenfield Academy
```

---

## Problem 2 — Counting How Many Objects Exist

### Problem Statement
A clinic admission desk needs to keep an accurate live census of all patients admitted for care throughout the day. While each patient instance tracks personal records (name and age), clinic administrators need a centralized counter indicating the total population of `Patient` instances created so far.

Instead of maintaining an external counter or polling an external database, the class itself should maintain an internal census counter. Every time a new patient is registered and instantiated, the class counter must increment automatically. Administrators can query this global tally at any time through a class-level accessor method without needing to inspect individual patient records.

### What You'll Learn
- Maintaining global instance counters using class attributes
- Incrementing class state inside `__init__` during object instantiation
- Querying class metrics via `@classmethod` without instantiating an object first

### Requirements & Specifications
Create a `Patient` class:

1. **Class attribute**: `total_patients = 0`

2. **Constructor (`__init__`)**:
   - Parameters: `name`, `age`
   - Increment `Patient.total_patients` by 1 each time a new patient is created.

3. **Class method**:
   - `get_total_patients()`: Returns the value of `total_patients`.

4. **Instance method**:
   - `get_info()`: Returns `"Patient: <name>, Age: <age>"`

### Sample Run
```python
print(Patient.get_total_patients())   # 0

p1 = Patient("Arjun", 30)
p2 = Patient("Deepa", 25)
p3 = Patient("Mohan", 45)

print(Patient.get_total_patients())   # 3
print(p1.get_info())                  # Patient: Arjun, Age: 30
```

---

## Problem 3 — Creating Objects from Different Data Formats

### Problem Statement
An online bookstore ingests product records from multiple third-party suppliers and data pipelines. The core application creates `Book` objects with standard constructor arguments (`title`, `author`, `price`), but incoming feeds provide data in diverse formats:
1. Legacy supplier feeds stream data as comma-separated values (CSV), such as `"Clean Code,Robert Martin,45.0"`.
2. REST API webhooks deliver structured JSON-like Python dictionaries, such as `{"title": "...", "author": "...", "price": ...}`.

Rather than cluttering client code with repetitive parsing routines before instantiating books, the `Book` class must provide alternative constructors (factory methods) using `@classmethod`. These methods parse the incoming data representations and return fully configured `Book` instances.

### What You'll Learn
- Using `@classmethod` to implement the Factory Method design pattern
- Parsing structured strings and dictionaries into constructor arguments
- Providing clean alternative initialization interfaces for varied data sources

### Requirements & Specifications
Create a `Book` class:

1. **Constructor (`__init__`)**:
   - Parameters: `title`, `author`, `price`

2. **Class methods (alternative constructors)**:
   - `from_csv(csv_string)`:
     - Input: `"Clean Code,Robert Martin,45.0"`
     - Split by comma, create and return a `Book` object.
   - `from_dict(data_dict)`:
     - Input: `{"title": "Clean Code", "author": "Robert Martin", "price": 45.0}`
     - Pull values from the dict and return a `Book` object.

3. **Instance method**:
   - `get_details()`: Returns `"'<title>' by <author> — $<price>"`

### Sample Run
```python
b1 = Book("Python Tricks", "Dan Bader", 35.0)
b2 = Book.from_csv("Clean Code,Robert Martin,45.0")
b3 = Book.from_dict({"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "price": 50.0})

print(b1.get_details())  # 'Python Tricks' by Dan Bader — $35.0
print(b2.get_details())  # 'Clean Code' by Robert Martin — $45.0
print(b3.get_details())  # 'The Pragmatic Programmer' by Hunt & Thomas — $50.0
```
