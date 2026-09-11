# Module 12 — Composition and Aggregation

A common beginner mistake in OOP is using inheritance for everything. However, in real-world software architecture, most systems are built not by inheriting, but by **assembling smaller components into larger systems**.

This is the principle of **"Favor Object Composition Over Class Inheritance"**.

---

## 1. Concept Overview: "Is-A" vs. "Has-A"

In OOP, we distinguish between two fundamental relationships:

1. **"Is-A" (Inheritance)**:
   - A `SavingsAccount` *is a* `BankAccount`.
   - A `Dog` *is an* `Animal`.
   - Use when one class is truly a specialized variation of another.

2. **"Has-A" (Composition & Aggregation)**:
   - A `Car` *has an* `Engine`. (A car is NOT an engine!).
   - A `Computer` *has a* `CPU`.
   - A `Department` *has* `Teachers`.
   - Use when one class *contains*, *manages*, or *uses* other classes.

---

## 2. The Two Types of "Has-A": Composition vs. Aggregation

The "Has-A" relationship comes in two distinct flavors depending on **lifecycle ownership**:

| Relationship | Coupling | Lifecycle Dependency | Real-World Example |
| :--- | :--- | :--- | :--- |
| **Composition** | Strong (Tightly bound) | **Dependent**: If the container is destroyed, its parts die too. | `Car` and `Engine`. `House` and `Rooms`. |
| **Aggregation** | Weak (Loosely bound) | **Independent**: The parts exist on their own and survive if the container is destroyed. | `Department` and `Teachers`. `Playlist` and `Songs`. |

```
   COMPOSITION (Strong "Has-A")             AGGREGATION (Weak "Has-A")
   +--------------------------+             +--------------------------+
   | class Car:               |             | class Department:        |
   |   def __init__(self):    |             |   def __init__(teachers):|
   |     self.engine = Engine |             |     self.teachers =      |
   |     (Created inside;     |             |         teachers         |
   |      dies with the car)  |             |   (Passed from outside;  |
   +--------------------------+             |    teachers survive if   |
                                            |    dept is deleted!)     |
                                            +--------------------------+
```

---

## 3. Composition in Code (Car and Engine)

In pure **Composition**, the container class creates and owns its internal components. When the container ceases to exist, the components are discarded with it:

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"Engine ({self.horsepower} HP) started roaring!"

    def stop(self):
        self.is_running = False
        return "Engine stopped."


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        # COMPOSITION: The Car creates and owns its Engine internally!
        self.engine = Engine(horsepower)

    def drive(self):
        start_msg = self.engine.start()
        return f"{self.brand} is moving! {start_msg}"

# Using Composition:
my_car = Car("Ford Mustang", 450)
print(my_car.drive())
# Output: Ford Mustang is moving! Engine (450 HP) started roaring!
```

---

## 4. Aggregation in Code (Department and Teachers)

In **Aggregation**, the parts exist independently in memory and are passed into the container from the outside. If the department closes down, the teachers still exist:

```python
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_info(self):
        return f"{self.name} ({self.subject})"


class Department:
    def __init__(self, dept_name, teachers=None):
        self.dept_name = dept_name
        # AGGREGATION: Teachers are passed in from outside!
        self.teachers = teachers if teachers is not None else []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def list_faculty(self):
        names = [t.get_info() for t in self.teachers]
        return f"Department of {self.dept_name}: {', '.join(names)}"

# Step 1: Create teachers independently:
t1 = Teacher("Dr. Sharma", "Physics")
t2 = Teacher("Prof. Sen", "Mathematics")

# Step 2: Aggregate them into a Department:
dept = Department("Science", [t1, t2])
print(dept.list_faculty())

# Step 3: What happens if the department is deleted?
del dept

# The teachers are STILL ALIVE in memory:
print(t1.get_info())  # Dr. Sharma (Physics) — Still exists!
```

---

## 5. Why "Favor Composition Over Inheritance"?

Joe Armstrong, creator of Erlang, famously described the inheritance trap:
> *"You wanted a banana, but what you got was a gorilla holding the banana and the entire jungle."*

When you inherit from a class, you inherit **everything**, even things you don't need or want.
- If the parent class changes, your child class can break unexpectedly.
- You cannot swap out behaviors easily at runtime.

With **Composition**:
- Your classes remain small, focused, and loosely coupled.
- You can easily mock or swap components during testing.
- You can swap components at runtime (e.g. replacing a `GasEngine` with an `ElectricMotor` inside an existing car).

---

## 6. How to Choose: The Decision Rule

When designing your classes, ask these questions in order:

```
Is Object A a specialized kind of Object B?
  ├── YES ---> Use INHERITANCE ("Is-A")
  │            Example: Dog is an Animal.
  └── NO
        Can Component B exist independently if Container A is deleted?
          ├── YES ---> Use AGGREGATION ("Has-A" loose)
          │            Example: A Playlist has Songs.
          └── NO  ---> Use COMPOSITION ("Has-A" strong)
                       Example: A Building has Rooms.
```

---

## 7. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What is the difference between an "Is-A" and a "Has-A" relationship?
- [ ] In Composition, who creates and owns the component?
- [ ] In Aggregation, how do components enter the container?
- [ ] What happens to the components if an Aggregation container is destroyed?
- [ ] Why is composition often preferred over deep inheritance trees?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice modeling objects with composition and aggregation!
