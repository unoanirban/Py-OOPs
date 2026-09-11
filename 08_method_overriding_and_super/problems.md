# Practice Problems: Method Overriding and super()

Learn how a subclass can **override** (replace) a method it inherited from its parent class — and how to use `super()` to still run the parent's version alongside the new one.

> **Key idea:** When a subclass defines a method with the **same name** as the parent's method, it **overrides** it. The subclass's version runs instead. But sometimes you want both — run the parent's version first, then add more. That's what `super().method_name()` does.

---

## Problem 1 — Animal Sounds

### Problem Statement
A virtual wildlife sanctuary application simulates different animal species in their natural habitats. Every animal in the park has a name and belongs to the base `Animal` category with generic descriptions. 

However, when vocalizing, different species make completely distinct sounds: dogs bark, cats meow, and cows moo. If the base class provides only a generic vocalization method, calling it on specific animals would produce inaccurate simulations. You must design an inheritance hierarchy where subclasses override the base vocalization behavior (`make_sound()`) with their authentic calls while continuing to inherit common behaviors like `describe()` without code duplication.

### What You'll Learn
- Overriding an inherited method in derived classes
- Understanding dynamic dispatch (Python calling the subclass's version of a method at runtime)
- Distinguishing between inherited methods and overridden methods

### Requirements & Specifications

1. **Base class `Animal`**:
   - Constructor: `__init__(self, name)`
   - Method `make_sound()`: Prints `"<name> makes a sound."`
   - Method `describe()`: Prints `"I am an animal named <name>."`

2. **Subclass `Dog(Animal)`**:
   - Overrides `make_sound()`: Prints `"<name> says: Woof! Woof!"`

3. **Subclass `Cat(Animal)`**:
   - Overrides `make_sound()`: Prints `"<name> says: Meow!"`

4. **Subclass `Cow(Animal)`**:
   - Overrides `make_sound()`: Prints `"<name> says: Moo!"`

### Sample Run
```python
a = Animal("Generic Animal")
a.make_sound()    # Generic Animal makes a sound.
a.describe()      # I am an animal named Generic Animal.

d = Dog("Buddy")
d.make_sound()    # Buddy says: Woof! Woof!
d.describe()      # I am an animal named Buddy.  (inherited, not overridden)

c = Cat("Luna")
c.make_sound()    # Luna says: Meow!

cow = Cow("Gai")
cow.make_sound()  # Gai says: Moo!
```

---

## Problem 2 — Employee Types

### Problem Statement
A corporate payroll and talent management system maintains staff profiles across hierarchical job tiers. All company employees have standard compensation attributes (name, base salary) and shared operations like descriptive summaries and annual percentage raises.

Management-tier personnel (`Manager`), however, possess additional responsibilities: they oversee teams of direct reports (`team_size`) and receive specialized compensation terms (such as an executive +5% raise bonus on top of standard company raises). Rather than rewriting description formatting and salary adjustment logic from scratch in `Manager`, you should leverage `super()`. By calling the parent's implementation and augmenting it with managerial attributes and executive bonus percentages, you keep the codebase DRY and maintainable.

### What You'll Learn
- Calling `super().__init__()` to initialize base class attributes from a subclass constructor
- Using `super().method_name()` to extend (rather than completely replace) parent method logic
- Reusing core business operations while layering on role-specific enhancements

### Requirements & Specifications

1. **Base class `Employee`**:
   - Constructor: `__init__(self, name, salary)`
   - Method `get_description()`: Returns `"Employee: <name>, Salary: $<salary>"`
   - Method `apply_raise(percent)`: Increases `salary` by the given percentage. Prints `"Salary updated to $<new_salary>"`

2. **Subclass `Manager(Employee)`**:
   - Constructor: `__init__(self, name, salary, team_size)`
   - Call `super().__init__(name, salary)`.
   - Add `self.team_size = team_size`.
   - Overrides `get_description()`:
     - Call `super().get_description()` to get the base description.
     - Return that description + `", Team Size: <team_size>"`.
   - Overrides `apply_raise(percent)`:
     - Managers get an extra 5% bonus on top of the given raise.
     - So call `super().apply_raise(percent + 5)`.

### Sample Run
```python
emp = Employee("Ravi", 50000)
print(emp.get_description())   # Employee: Ravi, Salary: $50000
emp.apply_raise(10)            # Salary updated to $55000.0

mgr = Manager("Anita", 80000, 8)
print(mgr.get_description())   # Employee: Anita, Salary: $80000, Team Size: 8
mgr.apply_raise(10)            # Salary updated to $92000.0  (10% + 5% bonus = 15%)
print(mgr.get_description())   # Employee: Anita, Salary: $92000.0, Team Size: 8
```

---

## Problem 3 — Shapes with Area

### Problem Statement
A computer graphics vector engine renders and inspects diverse geometric shapes on a visual canvas. Every shape has an assigned color and needs a standardized interface to describe itself, including its surface area.

Because different geometric primitives require completely different mathematical area calculations (e.g., circles use $\pi r^2$, rectangles use length $\times$ width, and triangles use $\frac{1}{2} \text{base} \times \text{height}$), the base `Shape` class cannot provide a single universal formula. Instead, `Shape` defines a baseline area interface, which each concrete shape subclass overrides. When the inherited `describe()` method calls `self.area()`, Python automatically executes the appropriate subclass's calculation dynamically.

### What You'll Learn
- Defining a unified method interface across divergent subclasses
- Understanding how base class methods can call overridden subclass methods via `self`
- Implementing geometric formula overrides across multiple shape types

### Requirements & Specifications

1. **Base class `Shape`**:
   - Constructor: `__init__(self, color)`
   - Method `area()`: Returns `0` (default placeholder).
   - Method `describe()`: Prints `"I am a <color> shape with area <area>"`
     - This calls `self.area()` — so it uses the overridden version automatically!

2. **Subclass `Circle(Shape)`**:
   - Constructor: `__init__(self, color, radius)`
   - Overrides `area()`: Returns `3.14 * radius * radius`

3. **Subclass `Rectangle(Shape)`**:
   - Constructor: `__init__(self, color, length, width)`
   - Overrides `area()`: Returns `length * width`

4. **Subclass `Triangle(Shape)`**:
   - Constructor: `__init__(self, color, base, height)`
   - Overrides `area()`: Returns `0.5 * base * height`

### Sample Run
```python
c = Circle("red", 5)
print(c.area())      # 78.5
c.describe()         # I am a red shape with area 78.5

r = Rectangle("blue", 4, 6)
print(r.area())      # 24
r.describe()         # I am a blue shape with area 24

t = Triangle("green", 3, 8)
print(t.area())      # 12.0
t.describe()         # I am a green shape with area 12.0
```
