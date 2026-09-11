# Practice Problems: Inheritance

Learn how one class can **inherit** attributes and methods from another class, so you don't have to rewrite the same code.

> **Key idea:** If `Dog` inherits from `Animal`, then `Dog` automatically has all of `Animal`'s attributes and methods. You can add extra ones specific to `Dog` on top. This is the **"Is-A"** relationship: a Dog *is an* Animal.

---

## Problem 1 — Animals

### Problem Statement
A rescue shelter manages animals of varying species. While all animals share universal physical traits and biological needs—such as possessing a name and age, requiring food to eat, and needing sleep—different species exhibit distinct behaviors and characteristics. For instance, dogs have breed classifications and enjoy barking and fetching objects, whereas cats may be designated as indoor or outdoor pets and exhibit purring and meowing behaviors.

Duplicating common logic across separate animal classes causes unnecessary boilerplate and makes maintenance difficult. You need to model this hierarchy using object-oriented inheritance by creating a foundational base `Animal` class that encapsulates common state and behavior, and deriving specialized `Dog` and `Cat` subclasses that inherit the shared baseline while adding species-specific functionality.

### What You'll Learn
- Establishing an "Is-A" inheritance relationship between a base class and subclasses
- Calling the parent constructor to initialize shared state
- Adding specialized attributes and behavior methods to derived classes

### Requirements & Specifications

1. **Base class `Animal`**:
   - Constructor: `__init__(self, name, age)`
   - Methods:
     - `eat(food)`: Prints `"<name> is eating <food>."`
     - `sleep()`: Prints `"<name> is sleeping."`
     - `get_info()`: Returns `"<name>, Age: <age>"`

2. **Subclass `Dog(Animal)`**:
   - Constructor: `__init__(self, name, age, breed)`
   - Call the parent constructor for `name` and `age`.
   - Add `self.breed = breed`.
   - Extra methods:
     - `bark()`: Prints `"<name> says: Woof!"`
     - `fetch(item)`: Prints `"<name> fetched the <item>!"`

3. **Subclass `Cat(Animal)`**:
   - Constructor: `__init__(self, name, age, is_indoor)`
   - Call the parent constructor for `name` and `age`.
   - Add `self.is_indoor = is_indoor`.
   - Extra methods:
     - `purr()`: Prints `"<name> is purring."`
     - `meow()`: Prints `"<name> says: Meow!"`

### Sample Run
```python
dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.get_info())     # Buddy, Age: 3    (inherited from Animal!)
dog.eat("kibble")         # Buddy is eating kibble.   (inherited!)
dog.bark()                # Buddy says: Woof!
dog.fetch("ball")         # Buddy fetched the ball!

cat = Cat("Luna", 2, is_indoor=True)
print(cat.get_info())     # Luna, Age: 2
cat.eat("fish")           # Luna is eating fish.
cat.purr()                # Luna is purring.
cat.meow()                # Luna says: Meow!
```

---

## Problem 2 — University Community

### Problem Statement
A university directory system manages identities across campus. Every member of the university community is fundamentally a person who possesses a legal name, official university email address, and unique institutional badge ID number. Both students and faculty share this foundational identity and need to display digital badge credentials.

However, their roles and operational workflows diverge significantly:
- A `Student` pursues a degree program (major), enrolls in an evolving list of semester courses (preventing duplicate enrollments), and needs enrollment status summaries.
- A `Teacher` belongs to an academic department, specializes in a teaching subject, and conducts lectures.

Your goal is to construct a clean inheritance hierarchy where a parent `Person` class handles common identity attributes and badge formatting, while specialized `Student` and `Teacher` classes extend the model with domain-specific operations.

### What You'll Learn
- Modeling multiple sibling subclasses derived from a single parent entity
- Managing collection state (course list) within a subclass
- Extending inherited behaviors while preserving universal identity methods

### Requirements & Specifications

1. **Base class `Person`**:
   - Constructor: `__init__(self, name, email, id_number)`
   - Method:
     - `display_badge()`: Returns `"ID: <id_number> | <name> (<email>)"`

2. **Subclass `Student(Person)`**:
   - Constructor: `__init__(self, name, email, id_number, major)`
   - Call parent constructor.
   - Add `self.major = major`.
   - Add `self.courses = []` (list of enrolled course names).
   - Methods:
     - `enroll(course_name)`: Adds course to `self.courses` if not already in it. Prints `"Enrolled in <course>."` or `"Already enrolled."`.
     - `get_summary()`: Returns `"<name> | Major: <major> | Courses: <count> enrolled"`

3. **Subclass `Teacher(Person)`**:
   - Constructor: `__init__(self, name, email, id_number, department, subject)`
   - Call parent constructor.
   - Add `self.department` and `self.subject`.
   - Methods:
     - `teach()`: Prints `"Prof. <name> is teaching <subject> in <department>."`

### Sample Run
```python
student = Student("Aarav", "aarav@uni.edu", "S101", "Computer Science")
print(student.display_badge())   # ID: S101 | Aarav (aarav@uni.edu)
student.enroll("Math 101")       # Enrolled in Math 101.
student.enroll("Math 101")       # Already enrolled.
student.enroll("Python 201")     # Enrolled in Python 201.
print(student.get_summary())     # Aarav | Major: Computer Science | Courses: 2 enrolled

teacher = Teacher("Dr. Meera", "meera@uni.edu", "T45", "CS Dept", "Data Structures")
print(teacher.display_badge())   # ID: T45 | Dr. Meera (meera@uni.edu)
teacher.teach()                  # Prof. Dr. Meera is teaching Data Structures in CS Dept.
```

---

## Problem 3 — Vehicles

### Problem Statement
A logistics enterprise operates a heterogeneous fleet of transport vehicles. Every vehicle in the fleet shares standard baseline registration details: manufacturer make, model name, and manufacturing year, along with a universal method to generate vehicle descriptions.

Yet different types of transport equipment fulfill entirely distinct operational functions:
- A commercial cargo `Truck` carries heavy freight, defined by a maximum payload capacity. It must support loading cargo (with strict overload prevention guards) and unloading cargo.
- An `ElectricCar` is an energy-efficient passenger vehicle equipped with a high-capacity lithium-ion battery. It needs charging mechanics up to maximum capacity and range simulation based on energy efficiency ratings (km per kWh).

You must organize this fleet by establishing a base `Vehicle` class and implementing distinct `Truck` and `ElectricCar` subclasses to manage their specialized functional requirements.

### What You'll Learn
- Designing polymorphic vehicle classes that share baseline metadata
- Enforcing capacity thresholds and error guards within specialized subclass methods
- Simulating energy consumption and physical freight constraints in Python classes

### Requirements & Specifications

1. **Base class `Vehicle`**:
   - Constructor: `__init__(self, make, model, year)`
   - Method: `get_description()`: Returns `"<year> <make> <model>"`

2. **Subclass `Truck(Vehicle)`**:
   - Constructor: `__init__(self, make, model, year, payload_capacity)`
     - `payload_capacity`: max weight it can carry in kg
   - Add `self.current_load = 0`
   - Methods:
     - `load_cargo(weight)`: If `current_load + weight <= payload_capacity`, add weight and print confirmation. Else print `"Overload! Cannot carry that much."`.
     - `unload()`: Sets `current_load` to 0, prints `"Cargo unloaded."`.

3. **Subclass `ElectricCar(Vehicle)`**:
   - Constructor: `__init__(self, make, model, year, battery_capacity)`
     - `battery_capacity`: max kWh
   - Add `self.battery_level = 0`
   - Methods:
     - `charge(kwh)`: Adds `kwh` up to `battery_capacity`. Prints actual amount charged.
     - `drive(km, efficiency)`: 
       - `efficiency` = km per kWh
       - If enough battery: subtract battery used, print km driven.
       - Else: print `"Not enough battery."`

### Sample Run
```python
truck = Truck("Tata", "Ace", 2021, 1000)
print(truck.get_description())   # 2021 Tata Ace
truck.load_cargo(600)            # Loaded 600 kg.
truck.load_cargo(600)            # Overload! Cannot carry that much.
truck.unload()                   # Cargo unloaded.

ev = ElectricCar("Tesla", "Model 3", 2023, 75)
ev.charge(50)                    # Charged 50 kWh.
ev.drive(200, 6)                 # Drove 200 km.    (used 200/6 ≈ 33.3 kWh)
ev.drive(300, 6)                 # Not enough battery.
```
