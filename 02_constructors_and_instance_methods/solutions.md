# Solutions: 02 — Constructors and Instance Methods

## Problem 1 — Car Fuel Tracker

```python
class Car:
    def __init__(self, brand, model, fuel_capacity, fuel_efficiency):
        if fuel_capacity <= 0 or fuel_efficiency <= 0:
            print("Invalid values")
            return

        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_efficiency = fuel_efficiency
        self.fuel_level = fuel_capacity   # Start with a full tank
        self.odometer = 0.0

    def drive(self, distance_km):
        fuel_needed = distance_km / self.fuel_efficiency
        if fuel_needed <= self.fuel_level:
            self.fuel_level = self.fuel_level - fuel_needed
            self.odometer = self.odometer + distance_km
            print(f"Drove {distance_km} km")
        else:
            print("Not enough fuel to drive that far.")

    def refuel(self, liters):
        space_left = self.fuel_capacity - self.fuel_level
        liters_added = min(liters, space_left)
        self.fuel_level = self.fuel_level + liters_added
        print(f"Added {liters_added} L")

    def get_status(self):
        print(f"{self.brand} {self.model} | Odometer: {self.odometer} km | Fuel: {self.fuel_level}/{self.fuel_capacity} L")


# Try it out
car = Car("Toyota", "Camry", 50, 15)
car.get_status()   # Toyota Camry | Odometer: 0.0 km | Fuel: 50/50 L

car.drive(300)     # Drove 300 km
car.get_status()   # Toyota Camry | Odometer: 300.0 km | Fuel: 30.0/50 L

car.drive(600)     # Not enough fuel to drive that far.

car.refuel(25)     # Added 20 L  (capped at tank capacity)
car.get_status()   # Toyota Camry | Odometer: 300.0 km | Fuel: 50/50 L
```

**How it works:**
- `__init__` sets `fuel_level = fuel_capacity` (full tank) and `odometer = 0`.
- `drive()` calculates fuel needed, checks if available, then updates both attributes.
- `min(liters, space_left)` in `refuel()` makes sure you never overflow the tank.

---

## Problem 2 — Rectangle Calculator

```python
class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            print("Length and width must be greater than zero.")
            length = 1
            width = 1
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

    def scale(self, factor):
        if factor <= 0:
            print("Scale factor must be positive.")
            return
        self.length = self.length * factor
        self.width = self.width * factor


# Try it out
r = Rectangle(10, 5)
print(r.area())       # 50
print(r.perimeter())  # 30
print(r.is_square())  # False

r.scale(2)
print(r.length)  # 20
print(r.width)   # 10
print(r.area())  # 200

r2 = Rectangle(4, 4)
print(r2.is_square())  # True

r3 = Rectangle(-1, 5)  # Length and width must be greater than zero.
```

**How it works:**
- Validation in `__init__` ensures we always have valid dimensions.
- `is_square()` just compares the two attributes — clean and simple.
- `scale()` multiplies both dimensions by the same factor.

---

## Problem 3 — Bank Account with Transaction History

```python
class BankAccount:
    def __init__(self, holder, account_number, initial_balance=0):
        if initial_balance < 0:
            print("Balance cannot be negative.")
            initial_balance = 0

        self.holder = holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = [f"Account opened with ${initial_balance}"]

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return False
        self.balance = self.balance + amount
        self.transactions.append(f"Deposited: ${amount} | Balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance = self.balance - amount
        self.transactions.append(f"Withdrew: ${amount} | Balance: ${self.balance}")
        return True

    def get_statement(self):
        for entry in self.transactions:
            print(entry)


# Try it out
acc = BankAccount("Neha Gupta", "ACC12345", 500)
acc.deposit(200)
acc.withdraw(150)
acc.withdraw(1000)   # Insufficient funds.
acc.get_statement()
# Account opened with $500
# Deposited: $200 | Balance: $700
# Withdrew: $150 | Balance: $550
```

**How it works:**
- `transactions` is a list created in `__init__` — every object gets its own separate list.
- `deposit()` and `withdraw()` both validate first, then update `balance` and append to the list.
- `get_statement()` loops through the list and prints each entry.
