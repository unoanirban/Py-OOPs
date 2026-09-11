# Module 11 — Abstract Base Classes (ABCs)

In Module 10, we saw that Duck Typing allows any class to act polymorphically. But what if you want to **strictly enforce** that every subclass implements a set of required methods?

That is the purpose of **Abstract Base Classes (ABCs)** and the **`abc` module**.

---

## 1. Concept Overview: What is an Abstract Base Class?

An **Abstract Base Class (ABC)** is a class that serves as a **formal contract or template**:
1. **It cannot be instantiated directly**: You cannot create an object from an ABC itself.
2. **It declares abstract methods**: Methods marked with `@abstractmethod` have no body in the base class. Any subclass **must** provide concrete implementations for them, or Python will refuse to let you create instances of the subclass!

### Analogy: The Electrical Outlet Standard
Think of the electrical sockets in your home wall.
- The government publishes a specification (an **Abstract Contract**): *"Any plug must have three prongs of specific dimensions and deliver 220V AC."*
- You cannot plug a piece of paper that says "Outlet Specification" into a toaster. The specification itself cannot power anything (it is **Abstract**).
- But companies build **concrete plugs** (for laptops, TVs, refrigerators) that adhere strictly to that contract.

```
       +---------------------------------------------+
       |             class Shape(ABC):               |  <--- Abstract Base Class
       |  @abstractmethod                            |       (Cannot instantiate!)
       |  def area(self): pass                       |
       |  @abstractmethod                            |
       |  def perimeter(self): pass                  |
       +---------------------------------------------+
                              ^
                             / \
            +---------------+   +---------------+
            |                                   |
+----------------------+             +----------------------+
| class Circle(Shape): |             | class Box(Shape):    |
|   def area(): ...    |             |   def area(): ...    |
|   def perimeter():.. |             |   # Forgot perimeter!|
+----------------------+             +----------------------+
     [INSTANTIABLE]                    [FAILS AT CREATION!]
                                       TypeError: Can't instantiate
                                       abstract class Box with
                                       abstract method perimeter
```

---

## 2. Why Use ABCs? (Enforcing Contracts)

Without an ABC, if a developer writes a new class and forgets to implement a required method, you won't discover the bug until that exact method is called during production!

```python
# WITHOUT ABC: Fails late during runtime execution!
class Box:
    def area(self):
        return 100
    # Developer forgot 'perimeter'!

b = Box()  # Creation succeeds silently!
# 3 hours later in production:
b.perimeter()  # CRASH! AttributeError: 'Box' object has no attribute 'perimeter'
```

With an **Abstract Base Class**, Python catches this mistake **immediately at instantiation time**, before any other code runs:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Box(Shape):
    def area(self):
        return 100
    # Forgot perimeter!

# Python stops you right here!
b = Box()
# TypeError: Can't instantiate abstract class Box with abstract method perimeter
```

---

## 3. Syntax Walkthrough: The `abc` Module

To create an ABC in Python:
1. Import `ABC` and `abstractmethod` from the built-in `abc` module.
2. Inherit from `ABC`: `class MyClass(ABC):`.
3. Decorate required methods with `@abstractmethod`.

```python
from abc import ABC, abstractmethod

# 1. Abstract Base Class
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Subclasses MUST implement how payment is processed."""
        pass

    @abstractmethod
    def refund(self, transaction_id):
        """Subclasses MUST implement how refunds are processed."""
        pass

    # ABCs CAN ALSO HAVE CONCRETE METHODS!
    # Common helper code can live right inside the ABC:
    def log_transaction(self, message):
        print(f"[AUDIT LOG] {message}")


# 2. Concrete Subclass (Implements all abstract methods)
class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        self.log_transaction(f"PayPal charged ${amount}")
        return True

    def refund(self, transaction_id):
        self.log_transaction(f"PayPal refunded tx #{transaction_id}")
        return True


# 3. Using the concrete subclass:
gateway = PayPalGateway()
gateway.process_payment(150.0)
gateway.refund("TX98765")
```

---

## 4. Combining `@property` with `@abstractmethod`

You can also mandate that every subclass must implement a specific `@property`:

```python
class Vehicle(ABC):
    @property
    @abstractmethod
    def fuel_type(self):
        """Subclasses must define what fuel they use."""
        pass

class ElectricCar(Vehicle):
    @property
    def fuel_type(self):
        return "Electricity"

ev = ElectricCar()
print(ev.fuel_type)  # Output: Electricity
```

> [!IMPORTANT]
> **Decorator Order Matters!**
> When combining `@property` and `@abstractmethod`, **`@property` must be on the outside (top)** and **`@abstractmethod` on the inside (bottom)**:
> ```python
> @property
> @abstractmethod
> def name(self):
>     pass
> ```

---

## 5. Comparison: Duck Typing vs. ABCs

| Feature | Duck Typing (Informal) | Abstract Base Class (Formal) |
| :--- | :--- | :--- |
| **Inheritance** | None required | Must inherit from `ABC` |
| **Enforcement** | Fails only when missing method is called | Fails immediately when creating the object |
| **Tooling & IDE** | IDE cannot guarantee method existence | IDE flags missing methods immediately |
| **Best For** | Quick scripts, lightweight utilities | Large codebases, APIs, enterprise systems |

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Forgetting to Inherit from `ABC`
```python
# BUG:
class Shape:  # Forgot (ABC)!
    @abstractmethod
    def area(self): pass

# Because Shape didn't inherit from ABC, Python will let you instantiate it!
s = Shape()  # No error! @abstractmethod has no effect without ABC!
```
Always make sure your abstract base class inherits from `ABC`!

---

### Pitfall 2: Trying to Instantiate the ABC Directly
```python
class Appliance(ABC):
    @abstractmethod
    def turn_on(self): pass

# WRONG:
a = Appliance()  # TypeError: Can't instantiate abstract class Appliance!
```
You can only instantiate concrete subclasses that have implemented all abstract methods.

---

## 7. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] How do you import and define an Abstract Base Class in Python?
- [ ] What happens if a subclass forgets to implement an `@abstractmethod`?
- [ ] Can an ABC contain regular (concrete) methods with full implementations?
- [ ] What is the correct decorator order when combining `@property` and `@abstractmethod`?
- [ ] Why do team projects use ABCs instead of relying purely on duck typing?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice enforcing contracts with Abstract Base Classes!
