# Practice Problems: Constructors and Instance Methods

Learn how `__init__` sets up an object when it's created, and how instance methods update and read the object's state.

> **Key idea:** The constructor (`__init__`) runs automatically when you create an object. It's the right place to set up all the starting values. Methods can then read those values via `self` and update them over time.

---

## Problem 1 — Car Fuel Tracker

### Problem Statement
An automotive software company is developing a dashboard telemetry module to monitor vehicle fuel consumption and mileage in real time. 

When a vehicle is initialized, it comes with a predefined fuel tank capacity (in liters) and fuel efficiency rating (kilometers per liter). The car starts with a full fuel tank and zero kilometers on the odometer. As the driver commands the vehicle to drive specific distances, the system must calculate the required fuel consumption based on fuel efficiency. If the tank holds enough fuel, the trip is authorized, the odometer increases, and the fuel level decreases accordingly; otherwise, the journey is rejected to prevent running out of fuel on the road. The system also supports refueling up to the tank's maximum capacity without overfilling, along with real-time status reporting.

### What You'll Learn
- Using `__init__` to initialize baseline and derived attributes
- Validating constructor arguments to ensure physical realism (e.g., positive capacities)
- Managing interconnected state changes (distance driven reducing fuel reserves)

### Requirements & Specifications
Create a `Car` class:

1. **Constructor (`__init__`)**:
   - Parameters: `brand`, `model`, `fuel_capacity`, `fuel_efficiency`
     - `fuel_capacity`: how many liters the tank can hold (e.g., 50)
     - `fuel_efficiency`: how many km you get per liter (e.g., 15)
   - Set `fuel_level` to `fuel_capacity` at the start (full tank)
   - Set `odometer` to `0` (no km driven yet)
   - If `fuel_capacity <= 0` or `fuel_efficiency <= 0`, print `"Invalid values"` and don't create the car properly.

2. **Methods**:
   - `drive(distance_km)`:
     - Calculate fuel needed: `distance_km / fuel_efficiency`
     - If enough fuel is available: subtract the fuel used, add distance to `odometer`, print how far you drove.
     - If not enough fuel: print `"Not enough fuel to drive that far."` and don't drive.
   - `refuel(liters)`:
     - Add `liters` to `fuel_level`, but don't go over `fuel_capacity`.
     - Print how many liters were actually added.
   - `get_status()`:
     - Prints something like:
       ```
       Toyota Camry | Odometer: 300.0 km | Fuel: 30.0/50.0 L
       ```

### Sample Run
```python
car = Car("Toyota", "Camry", 50, 15)
car.get_status()
# Toyota Camry | Odometer: 0.0 km | Fuel: 50.0/50.0 L

car.drive(300)
# Drove 300 km
car.get_status()
# Toyota Camry | Odometer: 300.0 km | Fuel: 30.0/50.0 L

car.drive(600)
# Not enough fuel to drive that far.

car.refuel(25)
# Added 20.0 L (tank is full)
```

---

## Problem 2 — Rectangle Calculator

### Problem Statement
A computer-aided design (CAD) application requires a geometric model for two-dimensional rectangles. In geometric modeling, dimensions such as length and width can never be zero or negative, making robust input validation essential during shape initialization.

The `Rectangle` model needs to calculate essential geometric properties dynamically, specifically its total area and perimeter. It must also verify whether the current dimensions form a square. Furthermore, designers frequently need to scale shapes up or down by a uniform magnification factor. The class must protect against invalid non-positive scale factors while accurately adjusting both dimensions when a valid scale is applied.

### What You'll Learn
- Validating constructor arguments and implementing safe fallbacks
- Implementing mathematical calculations as instance methods
- Mutating geometric dimensions through uniform scaling operations

### Requirements & Specifications
Create a `Rectangle` class:

1. **Constructor (`__init__`)**:
   - Parameters: `length`, `width`
   - If either is `<= 0`, print `"Length and width must be greater than zero."` and set them to `1` as a fallback.

2. **Methods**:
   - `area()`: Returns `length * width`.
   - `perimeter()`: Returns `2 * (length + width)`.
   - `is_square()`: Returns `True` if `length == width`, else `False`.
   - `scale(factor)`:
     - If `factor <= 0`, print `"Scale factor must be positive."` and do nothing.
     - Otherwise, multiply both `length` and `width` by `factor`.

### Sample Run
```python
r = Rectangle(10, 5)
print(r.area())        # 50
print(r.perimeter())   # 30
print(r.is_square())   # False

r.scale(2)
print(r.length)        # 20
print(r.width)         # 10
print(r.area())        # 200

r2 = Rectangle(4, 4)
print(r2.is_square())  # True
```

---

## Problem 3 — Bank Account with Transaction History

### Problem Statement
A retail banking platform requires an account management module capable of processing customer transactions while maintaining a strict, chronological audit trail. 

Every account is opened with a designated account holder name, account number, and an optional initial deposit balance. Because money cannot be negative, invalid starting balances must be caught and defaulted to zero. When deposits or withdrawals occur, the system must guard against non-positive transaction amounts and prevent overdrafts (withdrawing more money than currently available). Every successful operation—starting from account opening down to each deposit and withdrawal—must record a timestamped or formatted entry into an internal transaction log so customers can print complete account statements.

### What You'll Learn
- Maintaining complex internal state (such as a list of logs) inside an object attribute
- Handling multi-condition guards and returning success/failure boolean indicators
- Formatting and outputting historical ledger records

### Requirements & Specifications
Create a `BankAccount` class:

1. **Constructor (`__init__`)**:
   - Parameters: `holder`, `account_number`, `initial_balance` (default = `0`)
   - If `initial_balance < 0`, print `"Balance cannot be negative."` and set it to `0`.
   - Create a `transactions` list and add the first entry:
     `"Account opened with $<amount>"`

2. **Methods**:
   - `deposit(amount)`:
     - If `amount <= 0`, print `"Deposit must be greater than zero."` and return `False`.
     - Add `amount` to `balance`, record `"Deposited: $<amount> | Balance: $<balance>"`, return `True`.
   - `withdraw(amount)`:
     - If `amount <= 0`, print `"Withdrawal must be greater than zero."` and return `False`.
     - If `amount > balance`, print `"Insufficient funds."` and return `False`.
     - Subtract `amount` from `balance`, record `"Withdrew: $<amount> | Balance: $<balance>"`, return `True`.
   - `get_statement()`:
     - Prints all transaction entries, one per line.

### Sample Run
```python
acc = BankAccount("Neha Gupta", "ACC12345", 500)
acc.deposit(200)
acc.withdraw(150)
acc.withdraw(1000)   # Insufficient funds
acc.get_statement()

# Account opened with $500
# Deposited: $200 | Balance: $700
# Withdrew: $150 | Balance: $550
```
