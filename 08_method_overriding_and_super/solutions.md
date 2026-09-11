# Solutions: 08 — Method Overriding and super()

## Problem 1 — Animal Sounds

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def describe(self):
        print(f"I am an animal named {self.name}.")


class Dog(Animal):
    def make_sound(self):             # overrides Animal.make_sound
        print(f"{self.name} says: Woof! Woof!")


class Cat(Animal):
    def make_sound(self):             # overrides Animal.make_sound
        print(f"{self.name} says: Meow!")


class Cow(Animal):
    def make_sound(self):             # overrides Animal.make_sound
        print(f"{self.name} says: Moo!")


# Try it out
a = Animal("Generic Animal")
a.make_sound()    # Generic Animal makes a sound.
a.describe()      # I am an animal named Generic Animal.

d = Dog("Buddy")
d.make_sound()    # Buddy says: Woof! Woof!    (overridden)
d.describe()      # I am an animal named Buddy.  (inherited, not overridden)

c = Cat("Luna")
c.make_sound()    # Luna says: Meow!

cow = Cow("Gai")
cow.make_sound()  # Gai says: Moo!
```

**How it works:**
- Each subclass defines `make_sound()` with the same name — Python uses the most specific (subclass) version.
- `describe()` is NOT overridden in `Dog`, so Python goes up and uses `Animal.describe()`.
- Inheritance + overriding = write shared code once, customise only what's different.

---

## Problem 2 — Employee Types

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_description(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

    def apply_raise(self, percent):
        self.salary = self.salary * (1 + percent / 100)
        print(f"Salary updated to ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)        # reuse Employee's constructor
        self.team_size = team_size

    def get_description(self):
        base = super().get_description()      # get the parent's description first
        return base + f", Team Size: {self.team_size}"

    def apply_raise(self, percent):
        super().apply_raise(percent + 5)      # managers get extra 5% bonus


# Try it out
emp = Employee("Ravi", 50000)
print(emp.get_description())   # Employee: Ravi, Salary: $50000
emp.apply_raise(10)            # Salary updated to $55000.0

mgr = Manager("Anita", 80000, 8)
print(mgr.get_description())   # Employee: Anita, Salary: $80000, Team Size: 8
mgr.apply_raise(10)            # 10% + 5% bonus = 15% raise → Salary updated to $92000.0
print(mgr.get_description())   # Employee: Anita, Salary: $92000.0, Team Size: 8
```

**How it works:**
- `super().get_description()` runs the parent's version and returns its result.
- We then add to it — the manager's description is the employee's description + team size.
- `super().apply_raise(percent + 5)` passes a modified argument to the parent method — clean and reusable!

---

## Problem 3 — Shapes with Area

```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0    # placeholder

    def describe(self):
        print(f"I am a {self.color} shape with area {self.area()}")
        #                                                 ^^^^^^^^^^
        # self.area() calls the overridden version in the subclass!


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Try it out
c = Circle("red", 5)
print(c.area())    # 78.5
c.describe()       # I am a red shape with area 78.5

r = Rectangle("blue", 4, 6)
print(r.area())    # 24
r.describe()       # I am a blue shape with area 24

t = Triangle("green", 3, 8)
print(t.area())    # 12.0
t.describe()       # I am a green shape with area 12.0
```

**How it works:**
- `describe()` in `Shape` calls `self.area()`. Since `self` is a `Circle`, Python calls `Circle.area()` — not `Shape.area()`.
- This is **polymorphism in action**: the same `describe()` code produces different results for different shapes.
- This is why overriding is so powerful — you change one method and all behaviour built on it updates automatically.
