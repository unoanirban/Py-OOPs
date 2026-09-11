# Practice Problems: Composition and Aggregation

Learn how objects can contain other objects — this is often a better alternative to deep inheritance hierarchies.

> **Key idea:** Instead of inheriting behaviour, an object can **own** or **use** other objects.
> - **Composition**: The child object *cannot exist* without the parent ("has-a, and owns it"). E.g., a Car *has* an Engine — if you delete the car, the engine is gone too.
> - **Aggregation**: The child object *can exist independently* of the parent ("has-a, but doesn't own it"). E.g., a Department *has* Teachers, but teachers can exist outside the department.

---

## Problem 1 — Car and Engine (Composition)

### Problem Statement
In mechanical software simulations, a motor vehicle is not an engine; rather, a vehicle *has* an engine. An engine is an essential internal subsystem whose lifecycle is intimately tied to the parent vehicle. When a car is manufactured (instantiated), its internal engine is instantiated right alongside it as an owned component.

If the car is turned on or parked, the vehicle delegates the ignition and shutdown commands directly to its internal engine component. Furthermore, when generating comprehensive vehicle specifications, the car queries its engine for horsepower and fuel type metrics. In this problem, you will model this strict ownership composition relationship between `Car` and `Engine`.

### What You'll Learn
- Implementing strong object composition ("has-a" relationship with strict lifecycle ownership)
- Instantiating internal component objects directly within the parent constructor
- Delegating operations from the outer container object to the enclosed component

### Requirements & Specifications

1. **Class `Engine`**:
   - Constructor: `__init__(self, horsepower, fuel_type)`
   - Method `start()`: Prints `"Engine started. <horsepower>hp <fuel_type> engine roaring!"`
   - Method `stop()`: Prints `"Engine stopped."`
   - Method `get_specs()`: Returns `"<horsepower>hp <fuel_type> engine"`

2. **Class `Car`**:
   - Constructor: `__init__(self, make, model, year, horsepower, fuel_type)`
   - **Create the Engine inside `__init__`**: `self.engine = Engine(horsepower, fuel_type)`
   - Method `start_car()`: Prints `"Starting <make> <model>..."`, then calls `self.engine.start()`.
   - Method `stop_car()`: Calls `self.engine.stop()`, then prints `"<make> <model> parked."`
   - Method `get_info()`: Returns `"<year> <make> <model> | {self.engine.get_specs()}"`

### Sample Run
```python
car = Car("Toyota", "Camry", 2023, 203, "Petrol")
car.start_car()
# Starting Toyota Camry...
# Engine started. 203hp Petrol engine roaring!

print(car.get_info())   # 2023 Toyota Camry | 203hp Petrol engine
car.stop_car()
# Engine stopped.
# Toyota Camry parked.
```

---

## Problem 2 — Computer and Components (Composition)

### Problem Statement
A custom PC configuration builder allows customers to assemble workstations by combining modular hardware parts: a Central Processing Unit (`CPU`), system memory (`RAM`), and persistent drive (`Storage`). Each hardware part has its own operational specifications (clock speeds, core counts, gigabytes of capacity, interface types).

A fully assembled `Computer` workstation is composed of these discrete sub-components. When a customer inspects a build, the computer must query each constituent hardware object to assemble a comprehensive, multi-line specification sheet. You need to model the hardware components as modular classes and construct a composite `Computer` class that aggregates and coordinates them.

### What You'll Learn
- Composing multiple distinct sub-objects into a single high-level system class
- Injecting pre-instantiated component instances into composite objects
- Orchestrating multi-object data aggregation into unified reports

### Requirements & Specifications

1. **Class `CPU`**:
   - Constructor: `__init__(self, brand, cores, speed_ghz)`
   - Method `get_info()`: Returns `"<brand> CPU: <cores> cores @ <speed_ghz>GHz"`

2. **Class `RAM`**:
   - Constructor: `__init__(self, size_gb, speed_mhz)`
   - Method `get_info()`: Returns `"<size_gb>GB RAM @ <speed_mhz>MHz"`

3. **Class `Storage`**:
   - Constructor: `__init__(self, size_gb, storage_type)` (`storage_type` is "SSD" or "HDD")
   - Method `get_info()`: Returns `"<size_gb>GB <storage_type>"`

4. **Class `Computer`**:
   - Constructor: `__init__(self, brand, cpu, ram, storage)`
     - Parameters `cpu`, `ram`, `storage` are already-created objects.
   - Method `get_full_specs()`: Prints a full spec sheet:
     ```
     Brand: <brand>
     CPU: <cpu.get_info()>
     RAM: <ram.get_info()>
     Storage: <storage.get_info()>
     ```

### Sample Run
```python
cpu = CPU("Intel", 8, 3.6)
ram = RAM(16, 3200)
storage = Storage(512, "SSD")

pc = Computer("Dell", cpu, ram, storage)
pc.get_full_specs()
# Brand: Dell
# CPU: Intel CPU: 8 cores @ 3.6GHz
# RAM: 16GB RAM @ 3200MHz
# Storage: 512GB SSD
```

---

## Problem 3 — Department and Teachers (Aggregation)

### Problem Statement
An academic administration portal manages faculty staffing across university departments. An academic `Department` maintains an internal roster of faculty members (`Teacher`). However, unlike a mechanical car part, a teacher's existence is independent of any single department: if a department is reorganized, dissolved, or if a faculty member transfers, the teacher continues to exist as an independent professional.

This loose association represents **aggregation** ("has-a, but does not strictly own life-cycle"). The `Department` class needs to support adding teachers to its faculty list, removing teachers by name when they depart, querying current roster headcounts, and formatting a numbered directory of all affiliated instructors. Crucially, removing an instructor from a department must leave that `Teacher` instance completely intact and functional.

### What You'll Learn
- Distinguishing aggregation (loose reference association) from composition (strict ownership)
- Managing collections of independent external domain objects
- Searching and removing items from an internal collection without destroying the referenced object

### Requirements & Specifications

1. **Class `Teacher`**:
   - Constructor: `__init__(self, name, subject, years_experience)`
   - Method `get_profile()`: Returns `"<name> | <subject> | <years_experience> yrs exp"`

2. **Class `Department`**:
   - Constructor: `__init__(self, dept_name)`
   - Attribute: `self.teachers = []`
   - Methods:
     - `add_teacher(teacher)`: Appends a `Teacher` object to `self.teachers`.
     - `remove_teacher(name)`:
       - Finds a teacher by name and removes them from the list.
       - Prints `"<name> removed from <dept_name>."` or `"<name> not found."` if not there.
     - `get_all_teachers()`: Prints all teachers' profiles, numbered from 1.
     - `get_count()`: Returns the number of teachers in the department.

### Sample Run
```python
t1 = Teacher("Dr. Priya", "Algorithms", 10)
t2 = Teacher("Prof. Kiran", "Databases", 7)
t3 = Teacher("Dr. Anand", "Machine Learning", 5)

cs_dept = Department("Computer Science")
cs_dept.add_teacher(t1)
cs_dept.add_teacher(t2)
cs_dept.add_teacher(t3)

cs_dept.get_all_teachers()
# 1. Dr. Priya | Algorithms | 10 yrs exp
# 2. Prof. Kiran | Databases | 7 yrs exp
# 3. Dr. Anand | Machine Learning | 5 yrs exp

print(cs_dept.get_count())   # 3

cs_dept.remove_teacher("Prof. Kiran")   # Prof. Kiran removed from Computer Science.
print(cs_dept.get_count())   # 2

# Teachers exist independently — t2 still works even after removal:
print(t2.get_profile())   # Prof. Kiran | Databases | 7 yrs exp
```
