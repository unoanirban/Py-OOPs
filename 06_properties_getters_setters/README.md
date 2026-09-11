# Module 06 — Properties: Getters, Setters, and Deleters

In Module 05, we saw how traditional getter and setter methods like `get_balance()` and `set_balance()` protect private data.

However, writing `obj.get_price()` and `obj.set_price(100)` can feel clunky and unpythonic. In this module, you will learn Python's elegant alternative: the **`@property` decorator**.

---

## 1. Concept Overview: Why `@property`?

In many programming languages, if you want validation, you are forced to write clunky method calls:

```python
# Clunky traditional getter/setter:
car.set_speed(car.get_speed() + 10)

# Beautiful Pythonic property:
car.speed += 10
```

With `@property`, you get the **clean syntax of a normal attribute** combined with the **validation and safety of a method**!

```
     What external code writes:            What Python runs under the hood:
   +----------------------------+         +---------------------------------+
   |   print(emp.salary)        | ------> | def salary(self):               |
   |                            |         |     return self._salary         |
   +----------------------------+         +---------------------------------+
   |   emp.salary = 75000       | ------> | @salary.setter                  |
   |                            |         | def salary(self, value):        |
   |                            |         |     # validation checks...      |
   |                            |         |     self._salary = value        |
   +----------------------------+         +---------------------------------+
```

---

## 2. The Refactoring Superpower of `@property`

Consider this common real-world software scenario:

1. **Day 1**: You create a `Product` class with a simple public attribute:
   ```python
   class Product:
       def __init__(self, name, price):
           self.name = name
           self.price = price
   ```
   Dozens of other developers on your team start using `item.price`.

2. **Day 50**: Your boss says: *"We have a bug! Someone entered a negative price! We need validation immediately."*

In languages like Java, you would have to change `price` to `setPrice()`, breaking everyone's code across the entire company!

In **Python**, you simply turn `price` into a `@property`. The external code continues to write `item.price = 50`, but Python secretly runs your validation method. **Zero lines of external code break!**

---

## 3. Syntax Walkthrough: Getter, Setter, and Backing Variable

To create a property, you need a **backing variable** (by convention, named with a leading underscore, like `_price` or `_salary`) to hold the actual value in memory.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        # We assign to self.salary (not self._salary) so it triggers the setter validation!
        self.salary = salary

    # 1. THE GETTER: Called when someone reads: emp.salary
    @property
    def salary(self):
        """Returns the private backing variable."""
        return self._salary

    # 2. THE SETTER: Called when someone assigns: emp.salary = 60000
    @salary.setter
    def salary(self, new_salary):
        """Validates before updating the backing variable."""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = float(new_salary)

    # 3. THE DELETER (Optional): Called when someone writes: del emp.salary
    @salary.deleter
    def salary(self):
        print("Salary attribute deleted.")
        del self._salary
```

### Using the Property:
```python
emp = Employee("Aarav", 50000)

# Reading (triggers getter):
print(emp.salary)  # Output: 50000.0

# Writing valid value (triggers setter):
emp.salary = 65000
print(emp.salary)  # Output: 65000.0

# Writing invalid value (triggers setter validation):
# emp.salary = -1000
# Raises ValueError: Salary cannot be negative!
```

---

## 4. Computed / Derived Properties (Read-Only)

Often, an object has values that can be calculated on the fly from other attributes.

Instead of storing redundant state (which can easily get out of sync), define a **read-only computed property** by omitting the `@setter`:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Read-only property (no setter defined!)
    @property
    def area(self):
        return 3.14159 * (self.radius ** 2)

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.area)      # Output: 78.53975
print(c.diameter)  # Output: 10

# Trying to assign to a read-only property raises an error:
# c.area = 100
# AttributeError: can't set attribute 'area'
```

Another great example is `full_name`:
```python
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

u = User("Diya", "Sharma")
print(u.full_name)  # Diya Sharma
u.last_name = "Verma"
print(u.full_name)  # Diya Verma (automatically up to date!)
```

---

## 5. The Dreaded Infinite Recursion Trap (Most Common Mistake)

This is the most common mistake made by developers learning `@property`:

```python
# DISASTER: INFINITE RECURSION!
class Account:
    @property
    def balance(self):
        return self.balance  # BUG: Calls self.balance, which calls self.balance, which...

    @balance.setter
    def balance(self, value):
        self.balance = value  # BUG: Calls self.balance = value, which calls setter, which...
```

### Why does this crash?
`self.balance` is the **property itself**. Calling `self.balance` inside the getter calls the getter again. Calling `self.balance = value` inside the setter calls the setter again. Your program crashes with:
`RecursionError: maximum recursion depth exceeded`.

### The Fix:
Always use a **backing variable** with an underscore (like `self._balance`):
```python
# CORRECT:
class Account:
    @property
    def balance(self):
        return self._balance  # Reads the backing variable

    @balance.setter
    def balance(self, value):
        self._balance = value  # Writes to the backing variable
```

---

## 6. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What decorator turns a method into a getter? (`@property`)
- [ ] What decorator defines the setter? (`@property_name.setter`)
- [ ] Why do we use a backing variable like `self._attr`?
- [ ] What happens if you define a getter without a setter? (Read-only property)
- [ ] How does `@property` prevent breaking external code during refactoring?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice implementing getters, setters, and computed properties!
