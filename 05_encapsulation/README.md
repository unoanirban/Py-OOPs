# Module 05 — Encapsulation

Encapsulation is the first of the four foundational pillars of Object-Oriented Programming (along with Abstraction, Inheritance, and Polymorphism).

In this module, you will learn how to protect your objects from bad data and unwanted interference.

---

## 1. Concept Overview: What is Encapsulation?

**Encapsulation** means two things:
1. **Bundling**: Grouping related data (attributes) and the actions that operate on that data (methods) inside a single unit (the class).
2. **Data Hiding & Protection**: Restricting direct external access to an object's internal variables, exposing only a controlled, safe public interface.

### Analogy 1: The Medicinal Capsule
Where does the word "encapsulation" come from? Think of a **medicine capsule**.
- Inside the capsule are medicinal powders and chemicals.
- You don't scoop the powders directly into your hands or swallow raw chemicals in random doses.
- The capsule shell packages everything together safely and delivers it in the exact right dosage.

### Analogy 2: The Car Dashboard
When you drive a car:
- You interact with the **steering wheel**, the **accelerator pedal**, and the **brake** (this is the **Public Interface**).
- You do NOT reach under the hood to manually pump fuel into the combustion cylinders while driving at 60 mph (these are **Private Internal Details**).
- The internal engine components are *encapsulated* behind the dashboard for safety.

```
+-------------------------------------------------------------+
|                  Class: SecureBankAccount                   |
|                                                             |
|  [PUBLIC INTERFACE]  <--- Anyone can call these             |
|    + deposit(amount)         (Validates amount > 0)         |
|    + withdraw(amount, pin)   (Verifies PIN & checks balance)|
|    + get_balance(pin)        (Requires correct PIN)         |
|                                                             |
|  [PRIVATE DATA]       <--- Hidden from direct outside access|
|    - __balance               (Protected from negative money)|
|    - __pin                   (Protected from tampering)     |
+-------------------------------------------------------------+
```

---

## 2. Why Direct Access Causes Bugs

Suppose you have an un-encapsulated bank account:

```python
# UNPROTECTED CODE:
class BadAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

acc = BadAccount("Aarav", 1000)

# Disaster strikes! Anyone can do this from anywhere in the program:
acc.balance = -9999999  # State is corrupted!
acc.balance = "one million"  # Type error waiting to happen!
```

There are no rules, no validation, and no audit trail. Any part of the codebase can break your object's internal state.

With **Encapsulation**, external code cannot directly touch `balance`. It must use verified methods.

---

## 3. Access Levels in Python: The Naming Conventions

Unlike languages like Java or C++ that have strict keywords (`public`, `private`, `protected`), Python uses **naming conventions**:

| Access Level | Syntax | Meaning & Convention | Example |
| :--- | :--- | :--- | :--- |
| **Public** | `attribute` (no underscore) | Accessible freely from anywhere. This is the default. | `self.name = "Aarav"` |
| **Protected** | `_attribute` (one underscore) | "Internal use only." A gentle warning to other developers: *Do not touch this outside the class or its subclasses.* | `self._transaction_log = []` |
| **Private** | `__attribute` (two underscores) | Strictly private. Python automatically activates **Name Mangling** to prevent outside access and subclass collisions. | `self.__balance = 1000` |

---

## 4. How Name Mangling Works Under the Hood

When you prefix an attribute with two underscores (e.g., `self.__balance`), Python internally rewrites the variable name:

$$\text{Internal Name} = \text{\_ClassName\_\_attribute}$$

Let's see this in action:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Python renames this to _Account__balance

acc = Account(500)

# Trying to access __balance directly:
# print(acc.__balance)
# AttributeError: 'Account' object has no attribute '__balance'

# Let's inspect the object's internal dictionary:
print(acc.__dict__)
# Output: {'_Account__balance': 500}
```

> [!NOTE]
> *"We are all consenting adults here"* — Python's creator, Guido van Rossum.
> Python does not treat private variables as cryptographic security. You *could* technically write `acc._Account__balance`, but doing so intentionally breaks encapsulation and will cause your code to fail if the class changes. The double underscore is a strong sign saying: **"Keep out — internal implementation detail!"**

---

## 5. Controlled Access: Getters and Setters

To allow safe inspection and modification of private data, we write **Getter** and **Setter** methods.

- **Getter**: A method that returns the value of a private variable.
- **Setter**: A method that validates a new value before updating the private variable.

```python
class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        # Initialize private balance with validation
        if initial_balance < 0:
            self.__balance = 0.0
        else:
            self.__balance = float(initial_balance)

    # Getter: allows external code to READ the balance safely
    def get_balance(self):
        return self.__balance

    # Setter / Mutator: validates before modifying
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be strictly positive.")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be strictly positive.")
            return False
        if amount > self.__balance:
            print("Insufficient funds.")
            return False
        self.__balance -= amount
        return True
```

### Using the Encapsulated Class:
```python
acc = BankAccount("Aarav", 1000)

print(acc.get_balance())  # 1000.0

acc.deposit(500)
print(acc.get_balance())  # 1500.0

acc.deposit(-200)         # "Deposit amount must be strictly positive."
print(acc.get_balance())  # Still 1500.0 (protected!)
```

---

## 6. Common Beginner Pitfalls

### Pitfall 1: Writing Getters and Setters for Every Single Field (Java-style Boilerplate)
In Python, if an attribute is simple and doesn't need validation, **keep it public**:
```python
# Unnecessary overhead in Python:
class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

# Clean Python:
class Person:
    def __init__(self, name):
        self.name = name  # Public is completely fine!
```
*(In Module 06, we will see how `@property` lets you turn any public attribute into a validated property later without breaking code!)*

---

### Pitfall 2: Confusing Single Underscore with Double Underscore
- Use `_var` when you want to signal to human developers: *"This is an internal helper, please don't touch directly."*
- Use `__var` when you want Python to enforce name mangling to prevent accidental access or conflicts in subclasses.

---

## 7. Key Takeaways Checklist

Before moving to `problems.md`:
- [ ] What is encapsulation and why is direct attribute tampering dangerous?
- [ ] What is the difference between `attr`, `_attr`, and `__attr`?
- [ ] What is Name Mangling and what does Python rename `__balance` to?
- [ ] How do getter and setter methods protect object invariants?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice building well-encapsulated classes!
