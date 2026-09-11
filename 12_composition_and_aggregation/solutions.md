# Solutions: 12 — Composition and Aggregation

## Problem 1 — Car and Engine (Composition)

```python
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        print(f"Engine started. {self.horsepower}hp {self.fuel_type} engine roaring!")

    def stop(self):
        print("Engine stopped.")

    def get_specs(self):
        return f"{self.horsepower}hp {self.fuel_type} engine"


class Car:
    def __init__(self, make, model, year, horsepower, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(horsepower, fuel_type)   # Engine created inside Car

    def start_car(self):
        print(f"Starting {self.make} {self.model}...")
        self.engine.start()

    def stop_car(self):
        self.engine.stop()
        print(f"{self.make} {self.model} parked.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model} | {self.engine.get_specs()}"


# Try it out
car = Car("Toyota", "Camry", 2023, 203, "Petrol")
car.start_car()
# Starting Toyota Camry...
# Engine started. 203hp Petrol engine roaring!

print(car.get_info())   # 2023 Toyota Camry | 203hp Petrol engine
car.stop_car()
# Engine stopped.
# Toyota Camry parked.
```

**How it works:**
- `self.engine = Engine(horsepower, fuel_type)` creates the Engine inside the Car's constructor.
- The Engine doesn't exist independently — it was born with the Car.
- `car.start_car()` delegates work to `self.engine.start()` — the Car *uses* the Engine.

---

## Problem 2 — Computer and Components (Composition)

```python
class CPU:
    def __init__(self, brand, cores, speed_ghz):
        self.brand = brand
        self.cores = cores
        self.speed_ghz = speed_ghz

    def get_info(self):
        return f"{self.brand} CPU: {self.cores} cores @ {self.speed_ghz}GHz"


class RAM:
    def __init__(self, size_gb, speed_mhz):
        self.size_gb = size_gb
        self.speed_mhz = speed_mhz

    def get_info(self):
        return f"{self.size_gb}GB RAM @ {self.speed_mhz}MHz"


class Storage:
    def __init__(self, size_gb, storage_type):
        self.size_gb = size_gb
        self.storage_type = storage_type

    def get_info(self):
        return f"{self.size_gb}GB {self.storage_type}"


class Computer:
    def __init__(self, brand, cpu, ram, storage):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def get_full_specs(self):
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu.get_info()}")
        print(f"RAM: {self.ram.get_info()}")
        print(f"Storage: {self.storage.get_info()}")


# Try it out
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

```python
class Teacher:
    def __init__(self, name, subject, years_experience):
        self.name = name
        self.subject = subject
        self.years_experience = years_experience

    def get_profile(self):
        return f"{self.name} | {self.subject} | {self.years_experience} yrs exp"


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, name):
        for teacher in self.teachers:
            if teacher.name == name:
                self.teachers.remove(teacher)
                print(f"{name} removed from {self.dept_name}.")
                return
        print(f"{name} not found.")

    def get_all_teachers(self):
        for i, teacher in enumerate(self.teachers, start=1):
            print(f"{i}. {teacher.get_profile()}")

    def get_count(self):
        return len(self.teachers)


# Try it out
t1 = Teacher("Dr. Priya", "Algorithms", 10)
t2 = Teacher("Prof. Kiran", "Databases", 7)
t3 = Teacher("Dr. Anand", "Machine Learning", 5)

cs_dept = Department("Computer Science")
cs_dept.add_teacher(t1)
cs_dept.add_teacher(t2)
cs_dept.add_teacher(t3)

cs_dept.get_all_teachers()
print(f"Total: {cs_dept.get_count()}")   # 3

cs_dept.remove_teacher("Prof. Kiran")   # Prof. Kiran removed from Computer Science.
print(cs_dept.get_count())   # 2

# t2 still exists independently — it was never destroyed
print(t2.get_profile())   # Prof. Kiran | Databases | 7 yrs exp
```

**How it works:**
- `t1`, `t2`, `t3` exist as independent objects — they don't belong to the department.
- `cs_dept.add_teacher(t1)` just adds a *reference* to `t1` in the list — it doesn't create or own the teacher.
- Removing a teacher from the department doesn't delete the teacher object — it still lives in `t2`.
- This is **aggregation**: the Department uses Teacher objects but doesn't own them.
