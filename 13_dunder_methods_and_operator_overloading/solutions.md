# Solutions: 13 — Dunder Methods and Operator Overloading

## Problem 1 — Student Profile with __str__, __repr__, __bool__

```python
class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        # Called by print() — meant to be human-readable
        return f"Student: {self.name} (ID: {self.student_id}) | GPA: {self.gpa}"

    def __repr__(self):
        # Called by repr() — meant for developers/debugging
        return f"Student('{self.name}', '{self.student_id}', {self.gpa})"

    def __bool__(self):
        # Called by bool() and if statements
        return self.gpa >= 2.0


# Try it out
s1 = Student("Aarav Patel", "S4001", 3.85)
print(s1)           # Student: Aarav Patel (ID: S4001) | GPA: 3.85
print(repr(s1))     # Student('Aarav Patel', 'S4001', 3.85)
print(bool(s1))     # True

s2 = Student("Rohan", "S4002", 1.5)
print(bool(s2))     # False

if s1:
    print(f"{s1.name} is in good standing.")   # Aarav Patel is in good standing.
if not s2:
    print(f"{s2.name} is on academic probation.")
```

**How it works:**
- Without `__str__`, `print(s1)` would show something ugly like `<__main__.Student object at 0x7f...>`.
- `__repr__` should ideally show how to recreate the object.
- `__bool__` makes `if s1:` work naturally — no need to write `if s1.gpa >= 2.0:` everywhere.

---

## Problem 2 — 2D Vector with __add__, __sub__, __mul__, __str__

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)   # new object!

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Try it out
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1)               # Vector2D(3, 4)
print(v1 + v2)          # Vector2D(4, 6)   (calls __add__)
print(v1 - v2)          # Vector2D(2, 2)   (calls __sub__)
print(v1 * 3)           # Vector2D(9, 12)  (calls __mul__)

print(v1 == Vector2D(3, 4))   # True   (calls __eq__)
print(v1 == v2)               # False
```

**How it works:**
- `v1 + v2` calls `v1.__add__(v2)`.
- These methods return a **new** Vector2D — they don't modify the originals.
- `v1 * 3` calls `v1.__mul__(3)`. Note: `3 * v1` would need `__rmul__` (right multiply) — that's a stretch goal!

---

## Problem 3 — Shopping Cart with __len__, __str__, __contains__

```python
class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = {}    # item_name → quantity

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity    # increase existing quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print("Item not found.")

    def __len__(self):
        return sum(self.items.values())   # total quantity across all items

    def __contains__(self, item_name):
        return item_name in self.items

    def __str__(self):
        if not self.items:
            return f"Cart ({self.owner}): Empty"
        items_str = ", ".join(f"{name} x{qty}" for name, qty in self.items.items())
        return f"Cart ({self.owner}): {items_str} | Total items: {len(self)}"


# Try it out
cart = ShoppingCart("Rahul")
cart.add_item("Apple", 2)
cart.add_item("Banana", 3)
cart.add_item("Milk", 1)

print(len(cart))              # 6    (calls __len__)
print("Apple" in cart)        # True  (calls __contains__)
print("Juice" in cart)        # False
print(cart)
# Cart (Rahul): Apple x2, Banana x3, Milk x1 | Total items: 6

cart.add_item("Apple", 4)
print(cart)
# Cart (Rahul): Apple x6, Banana x3, Milk x1 | Total items: 10

cart.remove_item("Milk")
print(cart)
# Cart (Rahul): Apple x6, Banana x3 | Total items: 9
```
