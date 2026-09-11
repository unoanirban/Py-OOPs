# Module 09 — Multiple Inheritance & Method Resolution Order (MRO)

In Modules 07 and 08, every child class had exactly one parent class (Single Inheritance). 

Python, however, supports **Multiple Inheritance**—a class can inherit attributes and methods from **two or more parent classes** simultaneously!

---

## 1. Concept Overview: What is Multiple Inheritance?

In the real world, an entity often belongs to multiple categories at the same time:
- A **Smartphone** is both a **Phone** and a **DigitalCamera**.
- A **FlyingCar** is both a **Car** and an **Airplane**.
- A **TeachingAssistant** is both a **Student** and an **Employee**.

In Python, you specify multiple parents by listing them inside parentheses, separated by commas:

```python
class Smartphone(Phone, Camera):
    pass
```

```
           +----------------+        +----------------+
           |  class Phone   |        |  class Camera  |
           |  + make_call() |        |  + take_photo()|
           +----------------+        +----------------+
                    \                       /
                     \                     /
                  +---------------------------+
                  |     class Smartphone      |
                  |  (Inherits from both!)    |
                  +---------------------------+
```

---

## 2. The Classic "Diamond Problem"

While multiple inheritance is powerful, it introduces a famous dilemma known as **The Diamond Problem**:

```
               +---------------+
               |    Class A    |  <--- Root Superclass (has greet())
               +---------------+
                  /         \
                 /           \
        +---------------+  +---------------+
        |    Class B    |  |    Class C    |  <--- Both override greet()!
        +---------------+  +---------------+
                 \           /
                  \         /
               +---------------+
               |    Class D    |  <--- Which greet() does D run? B or C?
               +---------------+
```

If both `B` and `C` provide their own version of `greet()`, which one should `D` call? And if both `B` and `C` call `A.__init__()`, does `A` get initialized twice?

---

## 3. Python's Deterministic Solution: MRO (Method Resolution Order)

Python solves this problem completely and deterministically using an algorithm called **C3 Linearization**.

This algorithm calculates a single, unambiguous search path for every class, known as the **Method Resolution Order (MRO)**.

### Inspecting the MRO:
You can check the exact lookup order of any class at runtime using `.mro()`:

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# Output: [D, B, C, A, object]
```

### The Three Golden Rules of MRO:
1. **Children before Parents**: A subclass (`D`) is always checked before any of its ancestors (`B`, `C`, `A`).
2. **Left-to-Right Order**: Parents listed first in the class declaration are searched first:
   - `class D(B, C)` searches `B` before `C`.
   - `class D(C, B)` searches `C` before `B`.
3. **No Duplicates**: The root ancestor (`A`) is checked only once, at the very end of the branch.

---

## 4. How `super()` Navigates the MRO (The Sibling Wonder)

Here is the most important insight about Python's `super()`:

> **`super()` does NOT mean "my direct parent". It means "the NEXT class in the current object's MRO sequence"!**

Let's watch `super()` traverse through siblings:

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()  # Calls NEXT in MRO: which is C!

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()  # Calls NEXT in MRO: which is A!

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()  # Calls NEXT in MRO: which is B!

# Running D's greet:
d = D()
d.greet()
```

### What gets printed?
```
Hello from D
Hello from B
Hello from C  <--- Notice B passed control to sibling C!
Hello from A
```
Because `super()` follows the MRO list `[D, B, C, A]`, every single class in the diamond executes its logic cooperatively, and `A` is executed exactly once!

---

## 5. The Mixin Pattern: The Cleanest Use of Multiple Inheritance

In professional software development, you should rarely create complex, deep multi-parent hierarchies. Instead, the best practice is using **Mixins**.

### What is a Mixin?
A **Mixin** is a small, focused class designed to provide a single, reusable feature or capability to other classes. A Mixin is not meant to be instantiated on its own.

```python
import json

# Mixin: Adds the ability to serialize any object to JSON!
class JSONSerializableMixin:
    def to_json(self):
        """Converts the object's attributes dictionary to a JSON string."""
        return json.dumps(self.__dict__, indent=2)


# Mixin: Adds formatted logging!
class LoggableMixin:
    def log(self, action):
        print(f"[AUDIT LOG] {self.__class__.__name__}: {action}")


# Main Class using both Mixins:
class User(JSONSerializableMixin, LoggableMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Using the mixin capabilities:
u = User("aarav", "aarav@example.com")
u.log("Account created")
print(u.to_json())
```

Mixins provide plug-and-play functionality across completely unrelated classes!

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Inconsistent MRO (`TypeError`)
If your inheritance declarations contradict each other:
```python
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass  # TypeError: Cannot create a consistent method resolution order (MRO)!
```
Here, `X` demands `A` before `B`, but `Y` demands `B` before `A`. Python detects this contradiction and refuses to create class `Z`.

---

### Pitfall 2: Hardcoding Parent Initializers Instead of Using Cooperative `super()`
```python
# AVOID:
class D(B, C):
    def __init__(self):
        B.__init__(self)  # B initializes A
        C.__init__(self)  # C initializes A AGAIN! (A runs twice)

# USE COOPERATIVE super():
class D(B, C):
    def __init__(self):
        super().__init__()  # MRO guarantees A runs only once!
```

---

## 7. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] How do you declare multiple parents in a class header?
- [ ] What is the Diamond Problem and how does MRO resolve it?
- [ ] How do you view a class's lookup order? (`Class.mro()`)
- [ ] Why does `super()` call the next class in the MRO, rather than just the first parent?
- [ ] What is a Mixin and why is it preferred over deep multiple inheritance?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice multiple inheritance, MRO, and mixins!
