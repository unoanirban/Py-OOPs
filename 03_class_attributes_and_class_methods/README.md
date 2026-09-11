# Module 03 — Class Attributes and Class Methods

Up to this point, every variable we created belonged to a single object (`self.name`, `self.balance`). But what if you need data that is **shared by every single instance** of a class?

That is where **Class Attributes** and **Class Methods** come in.

---

## 1. Instance Attributes vs. Class Attributes

Let's clearly distinguish between the two types of attributes in Python:

| Feature | Instance Attribute | Class Attribute |
| :--- | :--- | :--- |
| **Where is it defined?** | Inside `__init__` or methods using `self.variable` | Directly inside the `class` body, outside any method |
| **Who owns it?** | A specific object instance | The class itself |
| **Is it shared?** | No. Each object has its own unique copy | Yes. All objects share the same single copy in memory |
| **How do you access it?** | `object.variable` | `ClassName.variable` (or `object.variable`) |
| **Example Use Case** | Student name, roll number, bank balance | School name, bank interest rate, total student count |

```
+-------------------------------------------------------------+
|                     Class: BankAccount                      |
|                                                             |
|   Class Attributes (Shared by all accounts):                |
|     - bank_name = "Apex Global Bank"                        |
|     - interest_rate = 0.05                                  |
|     - total_accounts = 2                                    |
+-------------------------------------------------------------+
           ^                                       ^
           | (references shared class)             | (references shared class)
+------------------------+               +------------------------+
|   Instance: account_1  |               |   Instance: account_2  |
|   Instance Attributes: |               |   Instance Attributes: |
|     - holder = "Aarav" |               |     - holder = "Diya"  |
|     - balance = 5000   |               |     - balance = 8000   |
+------------------------+               +------------------------+
```

---

## 2. Defining and Accessing Class Attributes

Here is how you write both in Python:

```python
class Student:
    # Class Attribute (Shared by all students in this school)
    school_name = "Greenwood High"
    total_students = 0

    def __init__(self, name, roll_number):
        # Instance Attributes (Unique to each student)
        self.name = name
        self.roll_number = roll_number

        # Increment shared counter whenever a new student is created
        Student.total_students += 1

# Creating instances:
s1 = Student("Aarav", 101)
s2 = Student("Diya", 102)

# Accessing class attributes via the class name (RECOMMENDED):
print(Student.school_name)     # Greenwood High
print(Student.total_students)  # 2

# Accessing class attributes via instances (also works, but be careful!):
print(s1.school_name)          # Greenwood High
print(s2.school_name)          # Greenwood High
```

---

## 3. The Dreaded "Attribute Shadowing" Trap

This is the number one trap beginners fall into when working with class attributes.

### What is Attribute Lookup?
When you ask for `s1.school_name`, Python searches in this order:
1. Does `s1` have an instance attribute named `school_name` in its `self.__dict__`?
2. If not, does the class `Student` have a class attribute named `school_name`?
3. If not, check any parent classes.

### The Mistake:
```python
s1 = Student("Aarav", 101)
s2 = Student("Diya", 102)

# MISTAKE: You want to update the school name for everyone, so you do:
s1.school_name = "Oakridge International"

# Look at what happened:
print(s1.school_name)          # "Oakridge International"
print(s2.school_name)          # "Greenwood High"  <-- Why didn't s2 change?!
print(Student.school_name)     # "Greenwood High"  <-- The class attribute didn't change!
```

### Why did this happen?
When you write `s1.school_name = ...`, Python does **not** update the class attribute. Instead, it creates a **brand new instance attribute** called `school_name` on `s1` alone! This new instance attribute "shadows" (hides) the class attribute for `s1`.

### The Proper Way:
Always modify class attributes via the **class name** (or via a `@classmethod`):
```python
# CORRECT:
Student.school_name = "Oakridge International"

# Now both instances see the updated value:
print(s1.school_name)      # Oakridge International
print(s2.school_name)      # Oakridge International
```

---

## 4. Class Methods: The `@classmethod` Decorator

Just like we have regular methods that operate on an instance (`self`), Python allows us to write methods that operate on the **class itself**. These are called **Class Methods**.

To create a class method, we use the `@classmethod` decorator:

```python
class BankAccount:
    bank_name = "National Trust Bank"
    interest_rate = 0.04  # 4% annual interest

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    # Regular instance method (operates on self)
    def calculate_interest(self):
        return self.balance * BankAccount.interest_rate

    # Class method (operates on cls, the class itself!)
    @classmethod
    def set_interest_rate(cls, new_rate):
        if new_rate < 0:
            print("Interest rate cannot be negative.")
            return
        cls.interest_rate = new_rate
```

### Notice the differences:
- It has `@classmethod` above the definition.
- Its first parameter is **`cls`** (short for class), not `self`.
- Calling `BankAccount.set_interest_rate(0.06)` automatically passes `BankAccount` as `cls`.

---

## 5. Major Use Case: Alternative Constructors (Factory Methods)

One of the most powerful and common uses of `@classmethod` in professional Python is creating **alternative constructors** (also called Factory Methods).

Sometimes your input data is not in clean separate arguments. For example, what if you receive student data as a comma-separated string from a file: `"Aarav,101,88"`?

Instead of making caller code parse strings everywhere, you can give your class a factory method:

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    @classmethod
    def from_csv_string(cls, csv_text):
        """Alternative constructor: parses 'Name,Roll,Marks' and returns a Student object."""
        parts = csv_text.split(",")
        name = parts[0].strip()
        roll = int(parts[1].strip())
        marks = float(parts[2].strip())
        
        # cls(...) creates a new instance of this class!
        return cls(name, roll, marks)

# Standard creation:
s1 = Student("Aarav", 101, 88.0)

# Creation via factory method:
s2 = Student.from_csv_string("Diya, 102, 94.5")
print(s2.name)   # Output: Diya
print(s2.marks)  # Output: 94.5
```

> [!TIP]
> **Why `cls(...)` instead of `Student(...)`?**
> Always write `return cls(...)` inside a `@classmethod`. If another class later inherits from `Student`, `cls` will automatically refer to the child class, making your factory method fully reusable!

---

## 6. Common Pitfalls & Gotchas

### Pitfall 1: Mutable Objects as Class Attributes
Never put a mutable object (like a list or dict) as a class attribute unless you explicitly want every single object to share and mutate the same list!
```python
# DISASTER:
class Cart:
    items = []  # CLASS ATTRIBUTE! Shared across all shoppers!

c1 = Cart()
c1.items.append("Apple")

c2 = Cart()
print(c2.items)  # Prints: ['Apple'] <-- c2 has c1's items!

# FIX:
class Cart:
    def __init__(self):
        self.items = []  # INSTANCE ATTRIBUTE! Unique to each shopper.
```

---

### Pitfall 2: Trying to Access `self` from a `@classmethod`
```python
# WRONG:
@classmethod
def print_summary(cls):
    print(cls.name)  # AttributeError! 'name' belongs to an instance, not the class!
```
A class method only knows about the class (`cls`). It has no idea which individual object (`self`) is calling it, or if any object even exists yet.

---

## 7. Key Takeaways Checklist

Before moving to `problems.md`:
- [ ] What is the difference between an instance attribute (`self.x`) and a class attribute (`Class.x`)?
- [ ] What happens when you assign `instance.class_attr = value` (the shadowing trap)?
- [ ] How do you declare a class method using `@classmethod` and `cls`?
- [ ] Why are class methods useful as alternative constructors (factories)?
- [ ] Why should you avoid mutable class attributes like `items = []`?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and build hands-on experience with class attributes and class methods!
