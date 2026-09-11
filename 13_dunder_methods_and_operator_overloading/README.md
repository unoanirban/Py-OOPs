# Module 13 — Dunder Methods and Operator Overloading

In Python, custom objects can behave just like built-in types (like integers, lists, or strings) through **Dunder Methods** (also known as **Magic Methods** or the **Python Data Model**).

---

## 1. Concept Overview: What are Dunder Methods?

**Dunder** is short for **D**ouble **Under**score. These are special methods that start and end with two underscores, like `__init__`, `__str__`, and `__add__`.

Whenever you use Python syntax on an object, Python secretly translates that syntax into a dunder method call behind the scenes:

```
     What you write:                     What Python secretly runs:
   +---------------------+             +-----------------------------+
   |   print(student)    |  -------->  |   student.__str__()         |
   |   len(book_shelf)   |  -------->  |   book_shelf.__len__()      |
   |   item1 + item2     |  -------->  |   item1.__add__(item2)      |
   |   item1 == item2    |  -------->  |   item1.__eq__(item2)       |
   |   shelf[0]          |  -------->  |   shelf.__getitem__(0)      |
   +---------------------+             +-----------------------------+
```

By defining these methods in your classes, you can make your objects feel natural, elegant, and fully integrated with Python's built-in syntax.

---

## 2. String Representations: `__str__` vs. `__repr__`

Without string representation methods, printing an object outputs an ugly memory address:
```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Aarav")
print(s)  # <__main__.Student object at 0x7fa2341b> (Not helpful!)
```

Python provides two dunder methods to fix this:

| Method | Intended Audience | Purpose | Triggered By |
| :--- | :--- | :--- | :--- |
| **`__str__`** | End Users | Human-friendly, readable text | `print(obj)`, `str(obj)`, `f"{obj}"` |
| **`__repr__`** | Developers & Debuggers | Unambiguous, technical detail (ideally shows how to recreate the object) | `repr(obj)`, interactive console, inside lists `[obj]` |

### Implementation Example:
```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # For end users (clean and readable):
    def __str__(self):
        return f"'{self.title}' by {self.author} (${self.price})"

    # For developers (precise and unambiguous):
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price})"

b = Book("1984", "George Orwell", 15.0)

print(str(b))   # '1984' by George Orwell ($15.0)
print(repr(b))  # Book(title='1984', author='George Orwell', price=15.0)
```

> [!TIP]
> **Golden Rule**: If you only implement one, implement `__repr__`! If `__str__` is not defined, Python will automatically use `__repr__` as a fallback.

---

## 3. Container Methods: `__len__` and `__getitem__`

You can make your custom objects support `len()` and square bracket indexing `[i]`:

```python
class BookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)

    # Enables: len(shelf)
    def __len__(self):
        return len(self.books)

    # Enables: shelf[index]
    def __getitem__(self, index):
        return self.books[index]

shelf = BookShelf()
shelf.add_book("Python Basics")
shelf.add_book("Fluent Python")

print(len(shelf))     # Output: 2
print(shelf[0])       # Output: Python Basics
```

---

## 4. Operator Overloading: Mathematical Operators (`+`, `-`, `*`)

**Operator Overloading** allows standard arithmetic operators to work on your custom classes:

| Operator | Dunder Method | Example Syntax |
| :--- | :--- | :--- |
| `+` | `__add__(self, other)` | `obj1 + obj2` |
| `-` | `__sub__(self, other)` | `obj1 - obj2` |
| `*` | `__mul__(self, other)` | `obj1 * obj2` |
| `/` | `__truediv__(self, other)`| `obj1 / obj2` |

### Overloading Example: 2D Points
```python
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    # Overload the '+' operator:
    def __add__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented  # Let Python try reflected operation or raise TypeError!
        # Return a BRAND NEW Point2D object:
        return Point2D(self.x + other.x, self.y + other.y)

p1 = Point2D(2, 3)
p2 = Point2D(4, 5)

p3 = p1 + p2
print(p3)  # Point2D(6, 8)
```

> [!IMPORTANT]
> **Never mutate operands in `+`!**
> `p1 + p2` must always return a **new object**. It should never modify `p1` or `p2` in place!

---

## 5. Comparison Operators & `@total_ordering`

You can customize how objects are compared (`==`, `<`, `>`, etc.):

- `__eq__(self, other)`: Overloads `==`
- `__lt__(self, other)`: Overloads `<`
- `__le__(self, other)`: Overloads `<=`
- `__gt__(self, other)`: Overloads `>`
- `__ge__(self, other)`: Overloads `>=`

### The `@functools.total_ordering` Decorator
Writing all 5 comparison methods is repetitive. Python gives you `@functools.total_ordering`:
- You define `__eq__` and **one** comparison method (usually `__lt__`).
- Python automatically generates all the remaining comparisons (`<=`, `>`, `>=`) for you!

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa == other.gpa

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa < other.gpa

s1 = Student("Aarav", 3.8)
s2 = Student("Diya", 3.9)

print(s1 < s2)   # True
print(s1 >= s2)  # False (Automatically generated by total_ordering!)
```

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Mutating the Original Object in `__add__`
```python
# WRONG:
def __add__(self, other):
    self.x += other.x  # Mutates self!
    return self

# CORRECT:
def __add__(self, other):
    return Point2D(self.x + other.x, self.y + other.y)  # Returns a fresh object!
```

---

### Pitfall 2: Raising `TypeError` Inside `__eq__`
If someone checks `student == "some string"`, `__eq__` should **return `False` or `NotImplemented`**, never raise an unhandled `TypeError`! Returning `False` allows clean, crash-free comparisons.

---

## 7. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What is the difference between `__str__` and `__repr__`?
- [ ] Which dunder method allows an object to use `len(obj)`?
- [ ] Which dunder method overloads the `+` operator?
- [ ] Why should binary operations like `+` return a new object rather than mutating `self`?
- [ ] What does `@functools.total_ordering` do?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice implementing Python magic methods!
