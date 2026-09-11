# Solutions: 01 — Classes and Objects

## Problem 1 — Student Report Card

```python
class Student:
    def __init__(self, name, roll_no, math_marks, science_marks, english_marks):
        self.name = name
        self.roll_no = roll_no
        self.math_marks = math_marks
        self.science_marks = science_marks
        self.english_marks = english_marks

    def calculate_average(self):
        return (self.math_marks + self.science_marks + self.english_marks) / 3

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        avg = self.calculate_average()
        grade = self.get_grade()
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Average: {avg:.2f} | Grade: {grade}")


# Try it out
s1 = Student("Rahul Sharma", 101, 88, 92, 79)

print(s1.calculate_average())  # 86.333...
print(s1.get_grade())          # B
s1.display_report()            # Roll No: 101 | Name: Rahul Sharma | Average: 86.33 | Grade: B

s2 = Student("Priya Mehta", 102, 95, 98, 91)
s2.display_report()            # Roll No: 102 | Name: Priya Mehta | Average: 94.67 | Grade: A
```

**How it works:**
- `__init__` stores each subject mark as a separate attribute — simple and readable.
- `calculate_average()` adds all three marks and divides by 3.
- `get_grade()` calls `self.calculate_average()` — one method reusing another.
- No `hasattr`, no dicts, no advanced tricks needed!

---

## Problem 2 — Bookstore Inventory

```python
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def apply_discount(self, percentage):
        if percentage < 1 or percentage > 100:
            print("Invalid discount")
            return
        discount_amount = self.price * (percentage / 100)
        self.price = self.price - discount_amount

    def is_in_stock(self):
        return self.stock > 0

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - quantity
            return True
        else:
            print("Not enough stock")
            return False

    def get_details(self):
        return f"'{self.title}' by {self.author} - ${self.price:.2f} (Stock: {self.stock} copies)"


# Try it out
b = Book("Clean Code", "Robert C. Martin", 45.0, 5)

print(b.get_details())   # 'Clean Code' by Robert C. Martin - $45.00 (Stock: 5 copies)
b.apply_discount(20)
print(b.price)           # 36.0
print(b.sell(3))         # True
print(b.sell(5))         # Not enough stock → False
print(b.is_in_stock())   # True
print(b.get_details())   # 'Clean Code' by Robert C. Martin - $36.00 (Stock: 2 copies)
```

**How it works:**
- `apply_discount` calculates the discount amount and subtracts it from `self.price`.
- `sell` checks if enough copies exist before reducing stock.
- Methods work with `self.attribute` — they read and update the object's own data.

---

## Problem 3 — Smartphone Storage Tracker

```python
class Mobile:
    def __init__(self, brand, model, total_storage, used_storage):
        self.brand = brand
        self.model = model
        self.total_storage = total_storage
        self.used_storage = used_storage

    def get_free_storage(self):
        return self.total_storage - self.used_storage

    def install_app(self, app_name, app_size):
        if app_size <= self.get_free_storage():
            self.used_storage = self.used_storage + app_size
            print(f"Installed {app_name}")
            return True
        else:
            print(f"Not enough storage for {app_name}")
            return False

    def uninstall_app(self, app_name, app_size):
        self.used_storage = self.used_storage - app_size
        print(f"Uninstalled {app_name}. Freed {app_size} GB")

    def display_specs(self):
        print(f"{self.brand} {self.model} | Storage: {self.used_storage}/{self.total_storage} GB used")


# Try it out
m = Mobile("Google", "Pixel 8", 128.0, 30.0)

print(m.get_free_storage())        # 98.0
m.install_app("PhotoEditor", 5.0)  # Installed PhotoEditor
m.install_app("HugeGame", 100.0)   # Not enough storage for HugeGame
m.display_specs()                  # Google Pixel 8 | Storage: 35.0/128.0 GB used
m.uninstall_app("PhotoEditor", 5.0)
m.display_specs()                  # Google Pixel 8 | Storage: 30.0/128.0 GB used
```

**How it works:**
- `install_app` calls `self.get_free_storage()` to check available space — one method calling another.
- This is a great pattern: break your logic into small, focused methods.
