# Practice Problems: Abstract Classes

Learn how to use **abstract classes** to define a *contract* — a set of methods that every subclass MUST implement.

> **Key idea:** An abstract class says "anyone who inherits from me MUST implement these methods." If you forget to implement one, Python will raise an error when you try to create an object. This forces a consistent interface across all subclasses.
>
> Use `from abc import ABC, abstractmethod` to create abstract classes.

---

## Problem 1 — Shapes with Enforced Area

### Problem Statement
In large software projects and graphical engines, developers frequently create new geometrical shape classes. If shape authors are left without architectural constraints, one developer might name their calculation `get_area()`, another `calculate_area()`, and a third might forget to implement `perimeter()` altogether. This lack of uniformity breaks polymorphic rendering pipelines and causes runtime errors.

To eliminate this inconsistency, you must define an abstract base class `Shape` that serves as a strict structural contract. Using Python's `abc.ABC` and `@abstractmethod`, `Shape` must mandate that every derived shape unconditionally implements both `area()` and `perimeter()`. The base class can also provide concrete shared methods, such as `describe()`, which safely delegate to these enforced abstract methods knowing they are guaranteed to exist at runtime.

### What You'll Learn
- Creating formal abstract contracts using Python's `abc.ABC` and `@abstractmethod`
- Forcing subclasses to fulfill required method interfaces at instantiation time
- Observing Python's compile/instantiation-time protection (`TypeError: Can't instantiate abstract class...`)

### Requirements & Specifications

1. **Abstract base class `Shape`** (inherits from `ABC`):
   - `@abstractmethod area()`: No body — subclasses must implement this.
   - `@abstractmethod perimeter()`: Same.
   - Regular method `describe()`: Prints `"Shape area: <area>, Perimeter: <perimeter>"`
     — calls `self.area()` and `self.perimeter()`.

2. **Class `Circle(Shape)`**:
   - Constructor: `__init__(self, radius)`
   - Implements `area()`: Returns `3.14 * radius * radius`
   - Implements `perimeter()`: Returns `2 * 3.14 * radius`

3. **Class `Rectangle(Shape)`**:
   - Constructor: `__init__(self, length, width)`
   - Implements `area()`: Returns `length * width`
   - Implements `perimeter()`: Returns `2 * (length + width)`

4. **Demonstrate** that you cannot create a `Shape()` object directly — it will raise a `TypeError`.

### Sample Run
```python
# Shape()    # ← This raises TypeError: Can't instantiate abstract class Shape...

c = Circle(7)
print(c.area())         # 153.86
print(c.perimeter())    # 43.96
c.describe()            # Shape area: 153.86, Perimeter: 43.96

r = Rectangle(5, 3)
print(r.area())         # 15
r.describe()            # Shape area: 15, Perimeter: 16
```

---

## Problem 2 — Payment Gateway

### Problem Statement
A multi-tenant e-commerce platform integrates with several third-party payment gateways, such as Razorpay and PayPal. Each payment provider uses unique authentication credentials and API endpoints. However, the core checkout application requires every payment gateway adapter to fulfill identical operational guarantees: executing payments (`process_payment`) and retrieving reference audit identifiers (`get_transaction_id`).

You need to establish an abstract class `PaymentGateway` that standardizes this payment contract. It must enforce that all concrete gateway adapters implement payment processing and transaction retrieval. In addition, the base class should implement a concrete template method, `print_receipt()`, which orchestrates the payment verification and outputs standard success/failure receipts regardless of which specific provider handled the checkout.

### What You'll Learn
- Defining formal abstract interfaces for external service integrations
- Combining abstract methods with concrete template methods in the parent class
- Building interchangeability and contract enforcement for business-critical workflows

### Requirements & Specifications

1. **Abstract base class `PaymentGateway`** (inherits from `ABC`):
   - `@abstractmethod process_payment(amount)`: Returns `True`/`False`.
   - `@abstractmethod get_transaction_id()`: Returns a string transaction ID.
   - Regular method `print_receipt(amount)`:
     - If payment succeeds, prints:
       ```
       Payment of $<amount> successful! TXN: <transaction_id>
       ```
     - If it fails, prints: `"Payment failed."`

2. **Class `RazorpayGateway(PaymentGateway)`**:
   - Constructor: `__init__(self, api_key)`
   - Implements `process_payment(amount)`:
     - Always succeeds for this demo — set `self._txn_id = f"RPY_{amount}"`, return `True`.
   - Implements `get_transaction_id()`: Returns `self._txn_id`

3. **Class `PayPalGateway(PaymentGateway)`**:
   - Constructor: `__init__(self, email)`
   - Implements `process_payment(amount)`:
     - Succeeds only if `amount <= 10000` — set `self._txn_id = f"PPL_{amount}"`, return `True`.
     - Else set `self._txn_id = None` and return `False`.
   - Implements `get_transaction_id()`: Returns `self._txn_id`

### Sample Run
```python
razorpay = RazorpayGateway("key_test_abc123")
razorpay.print_receipt(500)    # Payment of $500 successful! TXN: RPY_500

paypal = PayPalGateway("user@paypal.com")
paypal.print_receipt(8000)     # Payment of $8000 successful! TXN: PPL_8000
paypal.print_receipt(15000)    # Payment failed.
```

---

## Problem 3 — Vehicle Abstract Base

### Problem Statement
A transportation management system manages commercial vehicle fleets comprising internal combustion engine vehicles (petrol/diesel) and modern battery electric vehicles (BEVs). All vehicles in the fleet share common physical telemetry tracking, such as accumulating total distance driven on an odometer (`drive()`) and printing fleet asset summaries (`get_info()`).

However, powertrain mechanics differ fundamentally between vehicle types: petrol vehicles refuel liquid fuel tanks in liters and calculate range from fuel efficiency (km/L), whereas electric vehicles recharge battery packs in kilowatt-hours and calculate range from battery efficiency (km/kWh). You need to design an abstract `Vehicle` class that encapsulates common mileage accounting while enforcing abstract contracts for `refuel()` and `get_range()`. Concrete subclasses (`PetrolCar` and `ElectricCar`) must provide their specific powertrain implementations.

### What You'll Learn
- Combining common concrete behavior (mileage accumulation) with abstract powertrain requirements
- Managing distinct physical resources (liquid fuel vs. electrical battery capacity) behind identical abstract interfaces
- Enforcing architectural conformity across diverse technical implementations

### Requirements & Specifications

1. **Abstract base class `Vehicle`** (inherits from `ABC`):
   - Constructor: `__init__(self, make, model)`
   - Attribute: `self.mileage = 0`
   - `@abstractmethod refuel()`: Subclasses define how to refuel.
   - `@abstractmethod get_range()`: Returns estimated range in km.
   - Regular method `drive(km)`:
     - Adds `km` to `self.mileage`.
     - Prints `"Drove <km> km. Total mileage: <mileage> km."`
   - Regular method `get_info()`: Returns `"<make> <model> | Mileage: <mileage> km"`

2. **Class `PetrolCar(Vehicle)`**:
   - Constructor: `__init__(self, make, model, tank_capacity, efficiency)`
     - `efficiency` = km per liter
   - `self.fuel_level = 0`
   - Implements `refuel()`: Sets `fuel_level = tank_capacity`. Prints `"Petrol tank full."`
   - Implements `get_range()`: Returns `fuel_level * efficiency`

3. **Class `ElectricCar(Vehicle)`**:
   - Constructor: `__init__(self, make, model, battery_capacity, efficiency)`
     - `efficiency` = km per kWh
   - `self.battery_level = 0`
   - Implements `refuel()` (charging): Sets `battery_level = battery_capacity`. Prints `"Battery fully charged."`
   - Implements `get_range()`: Returns `battery_level * efficiency`

### Sample Run
```python
petrol = PetrolCar("Honda", "City", 40, 18)
petrol.refuel()                    # Petrol tank full.
print(petrol.get_range())          # 720
petrol.drive(200)                  # Drove 200 km. Total mileage: 200 km.
print(petrol.get_info())           # Honda City | Mileage: 200 km

ev = ElectricCar("Tesla", "Model 3", 75, 6)
ev.refuel()                        # Battery fully charged.
print(ev.get_range())              # 450
ev.drive(100)                      # Drove 100 km. Total mileage: 100 km.
```
