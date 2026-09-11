# Practice Problems: Dunder Methods and Operator Overloading

Learn how to give your objects **natural Python behaviour** — like printing nicely, comparing with `==`, and adding with `+`.

> **Key idea:** Dunder methods (double underscore methods like `__str__`, `__add__`, `__len__`) let you define what Python operators *mean* for your custom objects. For example, if you define `__add__`, then `a + b` works on your objects!

---

## Problem 1 — Student Profile with `__str__`, `__repr__`, `__bool__`

### Problem Statement
An academic registrar and student records portal processes thousands of student objects daily. When developers debug objects in terminal logs or interactive Python REPL sessions, default object representations (such as `<Student object at 0x7f4b8c>`) are unhelpful and obscure crucial diagnostic data. Furthermore, school reports need clear, human-readable student summaries when printed.

In addition, school administrative workflows frequently need to evaluate whether a student is currently in good academic standing (defined as maintaining a GPA $\ge 2.0$) using idiomatic boolean checks like `if student:`. To fulfill these requirements, you need to implement special dunder methods: `__str__` for friendly end-user displays, `__repr__` for unambiguous developer debugging strings, and `__bool__` for conditional truth-value testing.

### What You'll Learn
- Distinguishing between `__str__` (user-facing presentation) and `__repr__` (developer/diagnostic format)
- Implementing `__bool__` to control truth-value testing in `if` conditions
- Making custom Python classes integrate smoothly with built-in printing and formatting protocols

### Requirements & Specifications
Create a `Student` class:

1. **Constructor**: `__init__(self, name, student_id, gpa)`

2. **`__str__`**:
   - Returns: `"Student: <name> (ID: <student_id>) | GPA: <gpa>"`

3. **`__repr__`**:
   - Returns: `"Student('<name>', '<student_id>', <gpa>)"`
   - (This is what Python shows in the REPL / in lists)

4. **`__bool__`**:
   - Returns `True` if `gpa >= 2.0` (good standing), `False` otherwise.

### Sample Run
```python
s1 = Student("Aarav Patel", "S4001", 3.85)
print(s1)           # Student: Aarav Patel (ID: S4001) | GPA: 3.85
print(repr(s1))     # Student('Aarav Patel', 'S4001', 3.85)
print(bool(s1))     # True

s2 = Student("Rohan", "S4002", 1.5)
print(bool(s2))     # False

if s1:
    print(f"{s1.name} is in good standing.")   # Aarav Patel is in good standing.
```

---

## Problem 2 — 2D Vector with `__add__`, `__sub__`, `__mul__`, `__str__`

### Problem Statement
A physics simulation and 2D game engine uses mathematical vectors to compute forces, velocities, and positional displacements in Cartesian space $(x, y)$. In mathematical algorithms, writing verbose function calls like `v1.add(v2).multiply(3)` makes code hard to read and increases error rates compared to natural mathematical syntax like `(v1 + v2) * 3`.

Python allows custom classes to hook directly into standard arithmetic operators through operator overloading dunder methods. You need to create a `Vector2D` class that supports vector addition (`+` via `__add__`), vector subtraction (`-` via `__sub__`), scalar multiplication (`*` via `__mul__`), structural equality checking (`==` via `__eq__`), and string representation (`__str__`). Crucially, arithmetic operations must preserve immutability by returning brand new `Vector2D` instances rather than mutating the original operands.

### What You'll Learn
- Overloading mathematical operators (`+`, `-`, `*`, `==`) via special dunder methods
- Writing immutable operations that generate new instances rather than modifying existing operands
- Providing natural mathematical syntax for engineering and simulation domains

### Requirements & Specifications
Create a `Vector2D` class:

1. **Constructor**: `__init__(self, x, y)`

2. **`__str__`**: Returns `"Vector2D(<x>, <y>)"`

3. **`__add__(self, other)`**:
   - Returns a NEW `Vector2D` with `x = self.x + other.x`, `y = self.y + other.y`.

4. **`__sub__(self, other)`**:
   - Returns a NEW `Vector2D` with `x = self.x - other.x`, `y = self.y - other.y`.

5. **`__mul__(self, scalar)`**:
   - Returns a NEW `Vector2D` with `x = self.x * scalar`, `y = self.y * scalar`.

6. **`__eq__(self, other)`**:
   - Returns `True` if both `x` and `y` are equal.

### Sample Run
```python
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1)               # Vector2D(3, 4)
print(v1 + v2)          # Vector2D(4, 6)
print(v1 - v2)          # Vector2D(2, 2)
print(v1 * 3)           # Vector2D(9, 12)

print(v1 == Vector2D(3, 4))   # True
print(v1 == v2)               # False
```

---

## Problem 3 — Shopping Cart with `__len__`, `__str__`, `__contains__`

### Problem Statement
An e-commerce shopping platform requires an intuitive container class to represent customer shopping carts. A shopping cart holds various named merchandise items and their corresponding quantities (e.g., 2 Apples, 3 Bananas).

To make interacting with the cart feel idiomatic and natural for Python developers, the cart should behave like a native Python container. Developers should be able to query the total count of all individual items using `len(cart)` (evaluating total item quantities rather than just unique product names), test whether a particular product is in the cart using `"Apple" in cart`, and print a concise summary of all contents and quantities via `str(cart)`. You will implement these behaviors by providing `__len__`, `__contains__`, and `__str__` alongside item addition and removal methods.

### What You'll Learn
- Emulating Python collection protocols using `__len__` and `__contains__`
- Mapping membership tests (`in` operator) directly to internal dictionary lookups
- Aggregating composite collection counts and formatting dynamic collection summaries

### Requirements & Specifications
Create a `ShoppingCart` class:

1. **Constructor**: `__init__(self, owner)`
   - `self.items = {}` (item_name → quantity)

2. **Methods**:
   - `add_item(name, quantity)`: Adds to `self.items`. If already exists, increases quantity.
   - `remove_item(name)`: Removes item if it exists, else prints `"Item not found."`.

3. **Dunder methods**:
   - `__len__`: Returns total number of items (sum of all quantities).
   - `__contains__(item_name)`: Returns `True` if `item_name` is in `self.items`.
   - `__str__`: Returns a summary like:
     ```
     Cart (Rahul): Apple x2, Banana x3, Milk x1 | Total items: 6
     ```

### Sample Run
```python
cart = ShoppingCart("Rahul")
cart.add_item("Apple", 2)
cart.add_item("Banana", 3)
cart.add_item("Milk", 1)

print(len(cart))              # 6
print("Apple" in cart)        # True
print("Juice" in cart)        # False
print(cart)
# Cart (Rahul): Apple x2, Banana x3, Milk x1 | Total items: 6

cart.add_item("Apple", 4)     # Apple quantity increases
print(cart)
# Cart (Rahul): Apple x6, Banana x3, Milk x1 | Total items: 10
```
