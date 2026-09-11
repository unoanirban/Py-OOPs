# Solutions: 03 — Class Attributes and Class Methods

## Problem 1 — School with a Shared Name

```python
class Student:
    school_name = "Sunrise Public School"   # class attribute — shared by ALL students

    def __init__(self, name, roll_no):
        self.name = name        # instance attribute — unique to this student
        self.roll_no = roll_no

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name   # cls refers to the Student class itself

    def get_info(self):
        return f"{self.name} [Roll: {self.roll_no}] — School: {Student.school_name}"


# Try it out
s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)

print(s1.get_info())   # Rahul [Roll: 101] — School: Sunrise Public School
print(s2.get_info())   # Priya [Roll: 102] — School: Sunrise Public School

Student.change_school_name("Greenfield Academy")

print(s1.get_info())   # Rahul [Roll: 101] — School: Greenfield Academy
print(s2.get_info())   # Priya [Roll: 102] — School: Greenfield Academy
```

**How it works:**
- `school_name` is written directly inside the class body (not in `__init__`) — it belongs to the class, not to individual objects.
- `@classmethod` receives `cls` (the class itself) instead of `self`.
- Changing `cls.school_name` updates it for every existing and future student.

---

## Problem 2 — Counting How Many Objects Exist

```python
class Patient:
    total_patients = 0   # starts at 0, increments with every new patient

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Patient.total_patients += 1   # increment the shared counter

    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    def get_info(self):
        return f"Patient: {self.name}, Age: {self.age}"


# Try it out
print(Patient.get_total_patients())   # 0

p1 = Patient("Arjun", 30)
p2 = Patient("Deepa", 25)
p3 = Patient("Mohan", 45)

print(Patient.get_total_patients())   # 3
print(p1.get_info())                  # Patient: Arjun, Age: 30
```

**How it works:**
- Every time `__init__` runs, it runs `Patient.total_patients += 1` — incrementing the class-level counter.
- `get_total_patients()` is a class method that returns this shared counter.

---

## Problem 3 — Creating Objects from Different Data Formats

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @classmethod
    def from_csv(cls, csv_string):
        parts = csv_string.split(",")   # split "Title,Author,Price" by comma
        title = parts[0]
        author = parts[1]
        price = float(parts[2])
        return cls(title, author, price)   # create and return a new Book object

    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict["title"], data_dict["author"], data_dict["price"])

    def get_details(self):
        return f"'{self.title}' by {self.author} — ${self.price}"


# Try it out
b1 = Book("Python Tricks", "Dan Bader", 35.0)
b2 = Book.from_csv("Clean Code,Robert Martin,45.0")
b3 = Book.from_dict({"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "price": 50.0})

print(b1.get_details())  # 'Python Tricks' by Dan Bader — $35.0
print(b2.get_details())  # 'Clean Code' by Robert Martin — $45.0
print(b3.get_details())  # 'The Pragmatic Programmer' by Hunt & Thomas — $50.0
```

**How it works:**
- `from_csv` and `from_dict` are class methods that act as **alternative constructors**.
- They receive `cls` (the class), parse the input, and call `cls(...)` to create a new object — exactly like calling `Book(...)` directly.
- This pattern is very common in real Python code (e.g., `datetime.fromisoformat(...)`).
