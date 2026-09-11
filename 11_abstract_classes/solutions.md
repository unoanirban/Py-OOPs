# Solutions: 11 — Abstract Classes

## Problem 1 — Shapes with Enforced Area

```python
from abc import ABC, abstractmethod


class Shape(ABC):               # ABC = Abstract Base Class
    @abstractmethod
    def area(self):
        pass                    # no implementation here — subclasses MUST provide it

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):         # regular method — subclasses inherit this for free
        print(f"Shape area: {self.area()}, Perimeter: {self.perimeter()}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):             # must implement this (abstract)
        return 3.14 * self.radius * self.radius

    def perimeter(self):        # must implement this (abstract)
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Try it out
# Shape()  # TypeError: Can't instantiate abstract class — try it!

c = Circle(7)
print(c.area())         # 153.86
print(c.perimeter())    # 43.96
c.describe()            # Shape area: 153.86, Perimeter: 43.96

r = Rectangle(5, 3)
print(r.area())         # 15
r.describe()            # Shape area: 15, Perimeter: 16
```

**How it works:**
- `from abc import ABC, abstractmethod` imports the tools needed.
- `class Shape(ABC)` marks it as abstract.
- `@abstractmethod` marks methods that MUST be implemented by every subclass.
- `describe()` is a normal method — it calls `self.area()` which resolves to the subclass's version.

---

## Problem 2 — Payment Gateway

```python
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_transaction_id(self):
        pass

    def print_receipt(self, amount):
        if self.process_payment(amount):
            print(f"Payment of ${amount} successful! TXN: {self.get_transaction_id()}")
        else:
            print("Payment failed.")


class RazorpayGateway(PaymentGateway):
    def __init__(self, api_key):
        self.api_key = api_key
        self._txn_id = None

    def process_payment(self, amount):
        self._txn_id = f"RPY_{amount}"
        return True

    def get_transaction_id(self):
        return self._txn_id


class PayPalGateway(PaymentGateway):
    def __init__(self, email):
        self.email = email
        self._txn_id = None

    def process_payment(self, amount):
        if amount <= 10000:
            self._txn_id = f"PPL_{amount}"
            return True
        self._txn_id = None
        return False

    def get_transaction_id(self):
        return self._txn_id


# Try it out
razorpay = RazorpayGateway("key_test_abc123")
razorpay.print_receipt(500)    # Payment of $500 successful! TXN: RPY_500

paypal = PayPalGateway("user@paypal.com")
paypal.print_receipt(8000)     # Payment of $8000 successful! TXN: PPL_8000
paypal.print_receipt(15000)    # Payment failed.
```

---

## Problem 3 — Vehicle Abstract Base

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.mileage = 0

    @abstractmethod
    def refuel(self):
        pass

    @abstractmethod
    def get_range(self):
        pass

    def drive(self, km):
        self.mileage += km
        print(f"Drove {km} km. Total mileage: {self.mileage} km.")

    def get_info(self):
        return f"{self.make} {self.model} | Mileage: {self.mileage} km"


class PetrolCar(Vehicle):
    def __init__(self, make, model, tank_capacity, efficiency):
        super().__init__(make, model)
        self.tank_capacity = tank_capacity
        self.efficiency = efficiency
        self.fuel_level = 0

    def refuel(self):
        self.fuel_level = self.tank_capacity
        print("Petrol tank full.")

    def get_range(self):
        return self.fuel_level * self.efficiency


class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity, efficiency):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
        self.efficiency = efficiency
        self.battery_level = 0

    def refuel(self):    # "refueling" an EV = charging
        self.battery_level = self.battery_capacity
        print("Battery fully charged.")

    def get_range(self):
        return self.battery_level * self.efficiency


# Try it out
petrol = PetrolCar("Honda", "City", 40, 18)
petrol.refuel()               # Petrol tank full.
print(petrol.get_range())     # 720
petrol.drive(200)             # Drove 200 km. Total mileage: 200 km.
print(petrol.get_info())      # Honda City | Mileage: 200 km

print()

ev = ElectricCar("Tesla", "Model 3", 75, 6)
ev.refuel()                   # Battery fully charged.
print(ev.get_range())         # 450
ev.drive(100)                 # Drove 100 km. Total mileage: 100 km.
```
