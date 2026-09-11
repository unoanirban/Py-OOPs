# Solutions: 07 — Inheritance

## Problem 1 — Animals

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def get_info(self):
        return f"{self.name}, Age: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)    # call Animal's __init__
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def fetch(self, item):
        print(f"{self.name} fetched the {item}!")


class Cat(Animal):
    def __init__(self, name, age, is_indoor):
        super().__init__(name, age)    # call Animal's __init__
        self.is_indoor = is_indoor

    def purr(self):
        print(f"{self.name} is purring.")

    def meow(self):
        print(f"{self.name} says: Meow!")


# Try it out
dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.get_info())   # Buddy, Age: 3   (from Animal!)
dog.eat("kibble")       # Buddy is eating kibble.
dog.bark()              # Buddy says: Woof!
dog.fetch("ball")       # Buddy fetched the ball!

print()

cat = Cat("Luna", 2, is_indoor=True)
print(cat.get_info())   # Luna, Age: 2
cat.eat("fish")         # Luna is eating fish.
cat.purr()              # Luna is purring.
cat.meow()              # Luna says: Meow!
```

**How it works:**
- `super().__init__(name, age)` calls the parent (`Animal`) constructor — so you don't have to repeat `self.name = name` in every subclass.
- `Dog` and `Cat` inherit `eat()`, `sleep()`, and `get_info()` from `Animal` for free.
- Each subclass only defines the methods that are unique to it.

---

## Problem 2 — University Community

```python
class Person:
    def __init__(self, name, email, id_number):
        self.name = name
        self.email = email
        self.id_number = id_number

    def display_badge(self):
        return f"ID: {self.id_number} | {self.name} ({self.email})"


class Student(Person):
    def __init__(self, name, email, id_number, major):
        super().__init__(name, email, id_number)
        self.major = major
        self.courses = []

    def enroll(self, course_name):
        if course_name in self.courses:
            print("Already enrolled.")
        else:
            self.courses.append(course_name)
            print(f"Enrolled in {course_name}.")

    def get_summary(self):
        return f"{self.name} | Major: {self.major} | Courses: {len(self.courses)} enrolled"


class Teacher(Person):
    def __init__(self, name, email, id_number, department, subject):
        super().__init__(name, email, id_number)
        self.department = department
        self.subject = subject

    def teach(self):
        print(f"Prof. {self.name} is teaching {self.subject} in {self.department}.")


# Try it out
student = Student("Aarav", "aarav@uni.edu", "S101", "Computer Science")
print(student.display_badge())   # ID: S101 | Aarav (aarav@uni.edu)
student.enroll("Math 101")       # Enrolled in Math 101.
student.enroll("Math 101")       # Already enrolled.
student.enroll("Python 201")     # Enrolled in Python 201.
print(student.get_summary())     # Aarav | Major: Computer Science | Courses: 2 enrolled

print()

teacher = Teacher("Dr. Meera", "meera@uni.edu", "T45", "CS Dept", "Data Structures")
print(teacher.display_badge())   # ID: T45 | Dr. Meera (meera@uni.edu)
teacher.teach()                  # Prof. Dr. Meera is teaching Data Structures in CS Dept.
```

---

## Problem 3 — Vehicles

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight <= self.payload_capacity:
            self.current_load += weight
            print(f"Loaded {weight} kg. Total load: {self.current_load} kg.")
        else:
            print("Overload! Cannot carry that much.")

    def unload(self):
        self.current_load = 0
        print("Cargo unloaded.")


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 0

    def charge(self, kwh):
        space = self.battery_capacity - self.battery_level
        added = min(kwh, space)
        self.battery_level += added
        print(f"Charged {added} kWh. Battery: {self.battery_level}/{self.battery_capacity} kWh")

    def drive(self, km, efficiency):
        kwh_needed = km / efficiency
        if kwh_needed <= self.battery_level:
            self.battery_level -= kwh_needed
            print(f"Drove {km} km. Battery left: {self.battery_level:.1f} kWh")
        else:
            print("Not enough battery.")


# Try it out
truck = Truck("Tata", "Ace", 2021, 1000)
print(truck.get_description())   # 2021 Tata Ace
truck.load_cargo(600)            # Loaded 600 kg.
truck.load_cargo(600)            # Overload! Cannot carry that much.
truck.unload()                   # Cargo unloaded.

print()

ev = ElectricCar("Tesla", "Model 3", 2023, 75)
ev.charge(50)                    # Charged 50 kWh.
ev.drive(200, 6)                 # Drove 200 km.
ev.drive(300, 6)                 # Not enough battery.
```
