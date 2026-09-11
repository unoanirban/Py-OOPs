# Module 08 — Method Overriding and `super()`

In Module 07, you learned how a child class inherits methods from its parent. But what if the child class needs to do something **different** or **more specialized** than the parent?

That is where **Method Overriding** and **`super()`** come into play.

---

## 1. Concept Overview: What is Method Overriding?

**Method Overriding** occurs when a child class defines a method with the **exact same name** as a method in its parent class.

When you call that method on an instance of the child class, Python executes the child's version, effectively "overriding" (replacing or customizing) the parent's version.

```
       +---------------------------------------------+
       |             class Employee:                 |
       |  def calculate_pay(self):                   |
       |      return self.base_salary                |
       +---------------------------------------------+
                               ^
                               | inherits & overrides
       +---------------------------------------------+
       |             class Manager:                  |
       |  def calculate_pay(self):                   |
       |      # Calls parent to get base salary:     |
       |      base = super().calculate_pay()         |
       |      # Adds specialized manager bonus:      |
       |      return base + self.bonus               |
       +---------------------------------------------+
```

---

## 2. The Two Strategies for Overriding

When overriding a parent method, you typically choose between two approaches:

### Strategy A: Complete Replacement
The child completely discards what the parent did and replaces it with its own behavior:

```python
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        # Completely replaces parent string:
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

d = Dog()
print(d.make_sound())  # Output: Woof! Woof!
```

---

### Strategy B: Cooperative Extension (Using `super()`)
Often, the parent method already does 90% of the useful work, and the child just needs to add extra steps.

Instead of copy-pasting the parent's code into the child, the child calls **`super().method()`** to run the parent's logic, and then adds its own specialization:

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def get_details(self):
        return f"Employee: {self.name} | Pay: ${self.calculate_pay()}"


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        # 1. Let Employee initialize name and base_salary
        super().__init__(name, base_salary)
        # 2. Add Manager-specific attribute
        self.bonus = bonus

    def calculate_pay(self):
        # 3. Extend: get base salary from parent, then add bonus!
        base = super().calculate_pay()
        return base + self.bonus

    def get_details(self):
        # 4. Extend parent details string:
        parent_details = super().get_details()
        return f"{parent_details} (Bonus: ${self.bonus})"
```

### Testing the Extension:
```python
emp = Employee("Aarav", 50000)
print(emp.calculate_pay())  # 50000
print(emp.get_details())    # Employee: Aarav | Pay: $50000

mgr = Manager("Diya", 70000, 15000)
print(mgr.calculate_pay())  # 85000 (70000 + 15000)
print(mgr.get_details())    # Employee: Diya | Pay: $85000 (Bonus: $15000)
```

---

## 3. How Python Finds Methods: The Lookup Rule

When you call `mgr.calculate_pay()`, how does Python know which version to execute?

Python searches strictly from the bottom of the inheritance hierarchy upwards:
1. **Step 1**: Check `Manager.__dict__`. Does `Manager` define `calculate_pay`? **Yes! Run it.**
2. If not, check `Employee.__dict__`.
3. If not, check `object.__dict__` (the root of all Python classes).
4. If nowhere to be found, raise `AttributeError`.

Because Python finds `Manager`'s version first, the child method is chosen!

---

## 4. Why Use `super()` Instead of Hardcoding the Parent Class Name?

You might wonder: *"Can't I just write `Employee.calculate_pay(self)` instead of `super().calculate_pay()`?"*

While direct calls appear to work in simple single-inheritance examples, they are bad practice:
1. **Hard to maintain**: If you later change the parent class from `Employee` to `StaffMember`, you would have to find and rename every hardcoded `Employee` reference in every child class.
2. **Breaks Multiple Inheritance**: Direct calls cannot resolve complex multi-parent hierarchies (the Diamond Problem). Only `super()` follows Python's cooperative Method Resolution Order (covered in Module 09).

---

## 5. Common Beginner Pitfalls

### Pitfall 1: Accidental Infinite Recursion
```python
# DISASTER:
class Manager(Employee):
    def calculate_pay(self):
        # MISTAKE: Called self.calculate_pay() instead of super().calculate_pay()!
        return self.calculate_pay() + self.bonus
```
Calling `self.calculate_pay()` inside `calculate_pay()` calls itself in an endless loop until Python crashes with `RecursionError`. Always use `super().calculate_pay()` when delegating to the parent!

---

### Pitfall 2: Changing the Method Signature in an Incompatible Way
If a parent method accepts arguments:
```python
class Parent:
    def greet(self, message):
        print(f"Parent says: {message}")

class Child(Parent):
    def greet(self):  # Missing parameter!
        print("Child says hello!")
```
Now, if existing code passes a message: `obj.greet("Welcome")`, calling it on `Child` crashes with a `TypeError`! When overriding methods, preserve compatible parameter signatures.

---

## 6. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What is method overriding and how does a child class achieve it?
- [ ] What is the difference between complete replacement and extending with `super()`?
- [ ] How does `super().method_name()` allow child classes to reuse parent logic?
- [ ] Why must you write `super().method()` instead of `self.method()` inside an overridden method?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice overriding methods and using `super()`!
