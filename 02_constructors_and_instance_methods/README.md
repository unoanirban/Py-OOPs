# Module 02 — Constructors and Instance Methods

Now that you know how to define a class and create objects, it is time to master how objects are initialized and how their behaviors (methods) interact with their state.

---

## 1. Concept Overview: Why Constructors Matter

In Module 01, we saw that `__init__` initializes an object's attributes. But why is this so critical?

Imagine buying a new smartphone. When you take it out of the box, you expect it to have a screen, a battery, an operating system, and a serial number. You do not expect to receive an empty plastic shell and have to manually glue the battery inside before turning it on.

In programming:
- An object must be **born ready to work**.
- It should never exist in an incomplete, half-baked, or invalid state.
- The **Constructor (`__init__`)** guarantees that every object is properly set up with all required data the moment it is created.

```
       User writes: car = Car("Honda", "City", 2022)
                           |
                           v
        1. Python allocates memory for a new object
                           |
                           v
        2. Python automatically runs: Car.__init__(new_car, "Honda", "City", 2022)
                           |
                           v
        3. Attributes are attached:
             self.brand = "Honda"
             self.model = "City"
             self.year  = 2022
                           |
                           v
        4. Fully initialized object is assigned to variable 'car'
```

---

## 2. Default Parameter Values in `__init__`

Just like regular Python functions, `__init__` can have **default values** for parameters. This makes certain attributes optional when creating an object:

```python
class Book:
    def __init__(self, title, author, price, is_available=True):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available  # Defaults to True if not provided!

# Creating a book with all 4 arguments:
b1 = Book("Python Crash Course", "Eric Matthes", 25.0, False)

# Creating a book using the default is_available:
b2 = Book("Fluent Python", "Luciano Ramalho", 45.0)
print(b2.is_available)  # Output: True
```

---

## 3. Invariant Validation: Protecting Object State

In software engineering, a **class invariant** is a condition or rule that must **always remain true** for an object to be valid.

For example:
- A `Rectangle`'s width and height must never be negative or zero.
- A `BankAccount`'s balance must not start with negative money.
- A `Person`'s age cannot be negative.

We enforce these invariants right inside `__init__`:

### Approach 1: Guard Clauses with Fallbacks (Gentle / Beginner)
```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.0")
            self.balance = 0.0
        else:
            self.balance = initial_balance
```

### Approach 2: Raising Exceptions (Professional OOP)
```python
class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be strictly positive numbers!")
        self.length = length
        self.width = width
```
If someone tries to create `Rectangle(-5, 10)`, Python immediately stops execution with an error, preventing corrupted objects from polluting your program.

---

## 4. Instance Methods: Query vs. Mutator

Once an object is initialized, it interacts with the world through its **instance methods**. These methods generally fall into two broad categories:

```
                          INSTANCE METHODS
                            /          \
                           /            \
                QUERY METHODS          MUTATOR METHODS
                (Accessors)            (Modifiers / Actions)
                - Read state           - Change state
                - Return computations  - Update attributes
                - Do NOT modify self   - Often return status (bool)
                - e.g., get_area()     - e.g., deposit(500)
```

### Query Methods (Accessors)
A query method reads the object's current state, performs a calculation, and **returns the result**. It does **not** change any attribute values:
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        """Query method: computes and returns area without altering dimensions."""
        return self.length * self.width

    def get_perimeter(self):
        """Query method: computes and returns perimeter."""
        return 2 * (self.length + self.width)
```

### Mutator Methods (Actions)
A mutator method **modifies** the internal state (attributes) of the object. It often includes validation checks before making changes:
```python
class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        """Mutator: increases balance if amount is valid."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        """Mutator: decreases balance if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        return True
```

> [!TIP]
> **Best Practice**: Notice how `deposit()` and `withdraw()` return `True` or `False` to indicate whether the action succeeded. This allows the calling code to make decisions, such as displaying a confirmation or error message.

---

## 5. Critical Trap: The Mutable Default Argument Bug

This is one of the most infamous bugs in Python. **Never use a mutable object (like a list `[]` or a dictionary `{}`) as a default parameter in `__init__`!**

### The Bug Explained:
```python
# DANGEROUS CODE — DO NOT DO THIS!
class Student:
    def __init__(self, name, subjects=[]):  # The list [] is created ONCE when the class is defined!
        self.name = name
        self.subjects = subjects

s1 = Student("Aarav")
s1.subjects.append("Math")

s2 = Student("Diya")
print(s2.subjects)  # Prints: ['Math'] <-- Diya accidentally shares Aarav's list!
```

### Why did this happen?
Python creates default argument objects **once** when the function is defined, NOT each time an object is created. Because lists are mutable, all instances that use the default end up sharing the exact same list in memory!

### The Correct Pythonic Pattern:
Always use `None` as the default value, and create a fresh list inside `__init__`:
```python
# CORRECT PATTERN:
class Student:
    def __init__(self, name, subjects=None):
        self.name = name
        if subjects is None:
            self.subjects = []  # A brand new list is created for this specific object!
        else:
            self.subjects = subjects
```

---

## 6. Common Pitfalls & How to Avoid Them

### Pitfall 1: Typing `__init__` with Single Underscores
```python
# WRONG:
def _init_(self, name):  # Only 1 underscore on each side!
    self.name = name
# Python will NOT recognize this as the constructor!

# CORRECT:
def __init__(self, name):  # Two underscores on EACH side: __init__
    self.name = name
```

---

### Pitfall 2: Trying to `return` a Value from `__init__`
```python
# WRONG:
class Circle:
    def __init__(self, radius):
        self.radius = radius
        return radius  # TypeError: __init__() should return None!

# CORRECT:
class Circle:
    def __init__(self, radius):
        self.radius = radius
        # __init__ always returns None automatically.
```

---

### Pitfall 3: Printing Inside Methods Instead of Returning Values
```python
# INCONVENIENT:
def calculate_total(self):
    print(self.price * self.quantity)  # You can't use this result elsewhere in code!

# MUCH BETTER:
def calculate_total(self):
    return self.price * self.quantity  # Clean, testable, reusable!
```

---

## 7. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] Do you know how to provide default values in `__init__`?
- [ ] Why should you validate parameters inside `__init__`?
- [ ] What is the difference between a query method and a mutator method?
- [ ] Why is `subjects=None` safer than `subjects=[]` as a default parameter?
- [ ] Why should `__init__` never return a value?

---

## Ready to Practice!
Head over to **[problems.md](problems.md)** to put these concepts into action!
