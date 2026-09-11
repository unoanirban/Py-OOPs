# Solutions: 09 — Multiple Inheritance

## Problem 1 — Smartphone (Phone + Camera)

```python
class Phone:
    def __init__(self, brand, phone_number):
        self.brand = brand
        self.phone_number = phone_number

    def call(self, number):
        print(f"Calling {number} from {self.phone_number}...")

    def send_sms(self, number, message):
        print(f"SMS to {number}: {message}")


class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"Photo taken with {self.megapixels} MP camera!")

    def record_video(self, seconds):
        print(f"Recording {seconds}s video...")


class Smartphone(Phone, Camera):
    def __init__(self, brand, phone_number, megapixels, model):
        Phone.__init__(self, brand, phone_number)    # initialise Phone part
        Camera.__init__(self, megapixels)            # initialise Camera part
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model} | {self.megapixels} MP | {self.phone_number}"


# Try it out
phone = Smartphone("Samsung", "+91-9876543210", 108, "Galaxy S24")
print(phone.get_info())
phone.call("+91-9123456789")
phone.send_sms("+91-9123456789", "Hi!")
phone.take_photo()
phone.record_video(30)
```

**How it works:**
- `Smartphone` inherits from both `Phone` AND `Camera` — it gets all their methods.
- We call each parent's `__init__` separately to ensure both are properly set up.
- `phone.take_photo()` works even though `Smartphone` didn't define it — it came from `Camera`.

---

## Problem 2 — Teaching Assistant (Student + Teacher)

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

    def get_role(self):
        return "Student"


class Teacher:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def teach(self, subject):
        print(f"{self.name} is teaching {subject}.")

    def get_role(self):
        return "Teacher"


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, student_id, employee_id, department):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, employee_id)
        self.department = department

    def get_role(self):
        return f"Teaching Assistant in {self.department}"

    def full_profile(self):
        return (f"Name: {self.name} | Role: {self.get_role()} | "
                f"Student ID: {self.student_id} | Employee ID: {self.employee_id}")


# Try it out
ta = TeachingAssistant("Priya", "S2024", "E1045", "Computer Science")
print(ta.get_role())           # Teaching Assistant in Computer Science
ta.study("Algorithms")         # Priya is studying Algorithms.
ta.teach("Python Lab")         # Priya is teaching Python Lab.
print(ta.full_profile())

# Check MRO:
print(TeachingAssistant.__mro__)
# TeachingAssistant → Student → Teacher → object
```

**How it works:**
- `TeachingAssistant.get_role()` overrides both parents' versions — its own version runs.
- `ta.study()` comes from `Student`, `ta.teach()` comes from `Teacher`.
- MRO shows the order Python searches for methods: TA → Student → Teacher → object.

---

## Problem 3 — Exploring MRO

```python
class A:
    def greet(self):
        print("Hello from A")

    def who_am_i(self):
        return "A"


class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()        # continues up the MRO chain

    def who_am_i(self):
        return "B"


class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()        # continues up the MRO chain

    def who_am_i(self):
        return "C"


class D(B, C):
    pass    # inherits everything, overrides nothing


# Try it out
d = D()
d.greet()
# Hello from B   (B.greet runs first — B is first in MRO)
# Hello from C   (B's super() → C, because MRO: D → B → C → A)
# Hello from A   (C's super() → A)

print(d.who_am_i())    # B  (first class in MRO that has who_am_i)

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

**How it works:**
- MRO for `D` is: `D → B → C → A → object`.
- When `d.greet()` is called: Python finds it in `B`. `B.greet` calls `super().greet()`.
  - `super()` in `B` follows the MRO → goes to `C` (not `A`!). That's the key insight.
  - `C.greet` calls `super().greet()` → goes to `A`.
- `super()` in multiple inheritance doesn't mean "parent" — it means "next in the MRO chain".
- This cooperative multiple inheritance pattern ensures every class in the chain gets called exactly once.
