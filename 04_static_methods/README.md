# Module 04 — Static Methods

In Modules 01 to 03, we learned about methods that work on an individual object (`self`) and methods that work on the class (`cls`).

Now we meet the third member of Python's method family: the **Static Method** (`@staticmethod`).

---

## 1. Concept Overview: What is a Static Method?

A **Static Method** is a function defined inside a class that:
- **Does NOT receive `self`** (it does not know about any specific object instance).
- **Does NOT receive `cls`** (it does not know about the class itself).
- Works like a regular, standalone function, but lives **inside the class's namespace** because it is conceptually related to the class.

### Analogy: The Toolbox in a Workshop
Think of a class as a **Carpentry Workshop**.
- The workshop produces tables and chairs (objects).
- Some actions require a specific chair (e.g., `chair.paint("brown")` -> instance method).
- Some actions apply to the whole workshop (e.g., `Workshop.set_working_hours(8)` -> class method).
- But on the wall hangs a **tape measure** or **calculator**. The calculator doesn't care which chair you are building, nor does it care about the workshop's opening hours. It simply performs a calculation: `convert_inches_to_cm(12)`.
- It belongs in the workshop because that's where you need it, but it operates purely on the inputs you hand it. That is a **Static Method**.

---

## 2. The Triad of Python Methods (Comparison Table)

To never confuse the three types of methods again, bookmark this table:

| Feature | Instance Method | Class Method | Static Method |
| :--- | :--- | :--- | :--- |
| **Decorator** | None (default) | `@classmethod` | `@staticmethod` |
| **First Argument** | `self` (the instance) | `cls` (the class) | *None* (just normal parameters) |
| **Can Access Instance Data?** | Yes (`self.name`, etc.) | No | No |
| **Can Access Class Data?** | Yes | Yes (`cls.bank_name`) | No |
| **Primary Purpose** | Read or modify an object's state | Manage class-wide state or build factory constructors | Utility or helper functions related to the domain |
| **How to Call** | `instance.method()` | `Class.method()` or `instance.method()` | `Class.method()` or `instance.method()` |

---

## 3. Syntax and Walkthrough

Here is a practical, clear example showing all three in harmony:

```python
class TemperatureConverter:
    """A class representing temperature tools and records."""
    
    # Class attribute
    default_unit = "Celsius"

    def __init__(self, temperature_value):
        # Instance attribute
        self.temperature_value = temperature_value

    # 1. Instance Method: needs self to read the object's value
    def describe(self):
        return f"Current temperature is {self.temperature_value}° {self.default_unit}"

    # 2. Class Method: needs cls to modify class state
    @classmethod
    def set_default_unit(cls, new_unit):
        cls.default_unit = new_unit

    # 3. Static Method: pure math! Doesn't need self or cls!
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit: (C * 9/5) + 32"""
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Converts Fahrenheit to Celsius: (F - 32) * 5/9"""
        return (fahrenheit - 32) * 5 / 9
```

### Calling the Static Method:
Notice how you do not need to create an object to use a static method:
```python
# Call directly on the class:
f = TemperatureConverter.celsius_to_fahrenheit(100)
print(f)  # 212.0

c = TemperatureConverter.fahrenheit_to_celsius(32)
print(c)  # 0.0

# You can also call it on an instance, though calling via Class is cleaner:
temp_obj = TemperatureConverter(25)
print(temp_obj.celsius_to_fahrenheit(0))  # 32.0
```

---

## 4. Why Not Just Use a Regular Top-Level Function?

Beginners often ask: *"If a static method doesn't use `self` or `cls`, why not just define a normal function outside the class?"*

```python
# Approach A: Standalone function outside
def is_valid_password(pwd):
    return len(pwd) >= 8

# Approach B: Static method inside a class
class UserAccount:
    @staticmethod
    def is_valid_password(pwd):
        return len(pwd) >= 8
```

Both work identically. However, **Approach B offers significant advantages in large projects**:
1. **Clear Organization (Namespacing)**:
   When reading code, `UserAccount.is_valid_password()` immediately tells the developer what domain this validation belongs to.
2. **Discoverability via Autocomplete**:
   Typing `UserAccount.` in an IDE brings up all related methods, including validators and helpers, in one convenient popup.
3. **Inheritance and Overriding**:
   Unlike loose functions, static methods can be inherited and cleanly overridden by subclasses if needed.

---

## 5. Common Use Cases for Static Methods

1. **Input Validation**:
   Checking if an email, phone number, or password is valid before attempting to create an account.
2. **Unit Conversions**:
   Converting between metric and imperial units (km to miles, Celsius to Fahrenheit).
3. **Mathematical Utilities**:
   Checking if a number is prime, calculating a tax percentage, or rounding money values.

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Trying to Access `self` or `cls` Inside a Static Method
```python
class Logger:
    prefix = "[INFO]"

    @staticmethod
    def log(message):
        # BUG: self is not defined!
        print(f"{self.prefix} {message}")  # NameError: name 'self' is not defined!

# FIX: If you need class attributes like prefix, use @classmethod:
class Logger:
    prefix = "[INFO]"

    @classmethod
    def log(cls, message):
        print(f"{cls.prefix} {message}")
```

---

### Pitfall 2: Forgetting the `@staticmethod` Decorator
If you omit `@staticmethod`:
```python
class MathTool:
    def add(a, b):  # Forgot @staticmethod!
        return a + b

# If called via an instance:
tool = MathTool()
tool.add(2, 3)  # TypeError: MathTool.add() takes 2 positional arguments but 3 were given!
# Why? Python automatically passed 'tool' as the first argument!
```
Adding `@staticmethod` tells Python: *"Do not pass `self` or `cls` automatically. Only pass the arguments the user provides."*

---

## 7. Key Takeaways Checklist

Before moving to `problems.md`:
- [ ] What decorator is used to define a static method?
- [ ] Does a static method receive `self` or `cls` as its first argument?
- [ ] How is a static method invoked? (`ClassName.method_name(args)`)
- [ ] When should you choose `@staticmethod` over `@classmethod`?
- [ ] When should you choose `@staticmethod` over a regular standalone function?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice writing clean static methods!
