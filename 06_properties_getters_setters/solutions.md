# Solutions: 06 — Properties, Getters, and Setters

## Problem 1 — Employee Salary with Validation

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    # this calls the @salary.setter below

    @property
    def salary(self):
        return self._salary     # getter: just returns the internal value

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative.")
            self._salary = 0
        else:
            self._salary = value

    def get_info(self):
        return f"{self.name} earns ${self._salary} per month"


# Try it out
emp = Employee("Rahul", 5000)
print(emp.salary)         # 5000
print(emp.get_info())     # Rahul earns $5000 per month

emp.salary = 7000         # calls the setter
print(emp.salary)         # 7000

emp.salary = -500         # Salary cannot be negative.
print(emp.salary)         # 0
```

**How it works:**
- We store the actual value in `self._salary` (single underscore = "internal use").
- The `@property` decorator turns the getter into something you can read like an attribute: `emp.salary`.
- The `@salary.setter` decorator runs your validation code when someone does `emp.salary = value`.
- In `__init__`, writing `self.salary = salary` triggers the setter — so validation happens at creation too!

---

## Problem 2 — Person with a Computed Full Name

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age           # calls the @age.setter

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"   # computed from two attributes

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            print("Invalid age.")
            return            # don't update — leave _age unchanged
        self._age = value

    def get_info(self):
        return f"{self.full_name}, Age: {self.age}"


# Try it out
p = Person("Rahul", "Dravid", 45)
print(p.full_name)    # Rahul Dravid
print(p.get_info())   # Rahul Dravid, Age: 45

p.age = 50
print(p.age)          # 50

p.age = -5            # Invalid age.
print(p.age)          # 50 (unchanged)

p.first_name = "Sachin"
print(p.full_name)    # Sachin Dravid (computed fresh each time!)
```

**How it works:**
- `full_name` is a **read-only property** — it has a getter but no setter. Trying `p.full_name = "..."` would raise an error.
- Since `full_name` computes from `self.first_name` and `self.last_name`, updating either one automatically updates `full_name`.
- The age setter uses `return` (without changing `self._age`) to silently ignore invalid values.

---

## Problem 3 — Product with Automatic Price Calculation

```python
class Product:
    def __init__(self, name, price, tax_rate=0.1):
        self.name = name
        self.price = price          # calls the @price.setter
        self.tax_rate = tax_rate    # calls the @tax_rate.setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
            return
        self._price = value

    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        if value < 0 or value > 1:
            print("Tax rate must be between 0 and 1.")
            return
        self._tax_rate = value

    @property
    def final_price(self):
        return self._price * (1 + self._tax_rate)   # computed, read-only

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Invalid discount.")
            return
        self.price = self._price * (1 - percent / 100)   # uses the setter


# Try it out
prod = Product("Headphones", 1000, 0.18)
print(prod.price)        # 1000
print(prod.final_price)  # 1180.0

prod.apply_discount(10)
print(prod.price)        # 900.0
print(prod.final_price)  # 1062.0

prod.price = -50         # Price cannot be negative.
print(prod.price)        # 900.0 (unchanged)

prod.tax_rate = 2.0      # Tax rate must be between 0 and 1.
```

**How it works:**
- `final_price` is a computed read-only property — it always reflects the current `price` and `tax_rate`.
- `apply_discount` sets `self.price = ...` which goes through the setter's validation.
- All three properties together show how `@property` elegantly replaces manual get/set methods.
