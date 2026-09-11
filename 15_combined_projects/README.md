# Module 15 — Capstone Combined OOP Projects

Congratulations on reaching the final milestone of the Python OOP curriculum!

In Modules 01 through 14, you learned each OOP concept as an isolated tool. In this capstone module, you will bring all those tools together to architect **complete, end-to-end applications**.

---

## 1. Concept Overview: The OOP Architecture Stack

Professional software systems are built in architectural layers. Here is how every concept you have learned fits into a real-world software stack:

```
+------------------------------------------------------------------------------------+
|                             THE OOP ARCHITECTURE STACK                             |
+------------------------------------------------------------------------------------+
|  1. CONTRACTS & INTERFACES (abc.ABC, @abstractmethod)                              |
|     Defines public contracts for payment gateways, processors, and services.       |
+------------------------------------------------------------------------------------+
|  2. CLASS TAXONOMY (Inheritance & Polymorphism)                                    |
|     Shares baseline logic and specializes variants (e.g. Savings vs Current Acct). |
+------------------------------------------------------------------------------------+
|  3. COMPONENT ASSEMBLY (Composition & Aggregation)                                 |
|     Assembles modular systems (e.g. ATM Has-A CardReader; Department Has-A Faculty).|
+------------------------------------------------------------------------------------+
|  4. STATE INVARIANTS (Encapsulation & Properties)                                  |
|     Protects financial balances, validates inputs, prevents negative inventory.    |
+------------------------------------------------------------------------------------+
|  5. PYTHON INTEGRATION (Dunder Methods)                                            |
|     Enables native Python syntax: len(cart), print(item), p1 + p2, obj1 == obj2.   |
+------------------------------------------------------------------------------------+
```

---

## 2. The 4 Capstone Systems

In this module, you will build four comprehensive, real-world systems:

### Project 1: Enterprise Library Circulation & Fine System
- **Concepts**: Object relationships, state synchronization, inventory tracking, fine calculations.
- **Key Entities**: `Book`, `Member`, `Library`.
- **Core Challenge**: Keeping `book.is_available` and `member.borrowed_books` in sync atomically while calculating overdue fines.

### Project 2: Banking Core & Multi-Tier ATM Terminal
- **Concepts**: Encapsulation, inheritance hierarchy (`BankAccount -> SavingsAccount, CurrentAccount`), overdraft limits, hardware composition (`ATM`).
- **Key Entities**: `BankAccount`, `SavingsAccount`, `CurrentAccount`, `ATM`.
- **Core Challenge**: Enforcing financial invariants (positive balances, overdraft limits) and simulating an ATM terminal interacting with accounts.

### Project 3: Full-Stack E-Commerce & Checkout Engine
- **Concepts**: Abstract payment contracts (`PaymentGateway`), polymorphic checkout, stock reservation, shopping cart dunder methods (`__len__`, `__iter__`), order fulfillment lifecycle.
- **Key Entities**: `Product`, `Cart`, `Customer`, `Order`, `PaymentGateway (UPI, Card, COD)`.
- **Core Challenge**: Processing orders polymorphically across multiple payment gateways while deducting inventory and calculating order totals.

### Project 4: Comprehensive Academic University ERP
- **Concepts**: The ultimate OOP synthesis: Abstract people hierarchy (`Person -> Student, Teacher`), courses with capacity limits, department aggregation, transcript generation, GPA computation.
- **Key Entities**: `Person`, `Student`, `Teacher`, `Course`, `Department`, `University`.
- **Core Challenge**: Designing a multi-tiered educational institution where students enroll in courses, professors teach, and departments track performance.

---

## 3. The Pre-Coding Architecture Checklist

Before writing code for any capstone project, review this 5-point checklist:

1. **Invariants Protected**:
   Are attributes validated inside `__init__` or via `@property`? Can negative money or invalid strings corrupt the system?
2. **Proper Relationships**:
   Are you using Inheritance only for genuine "Is-A" relationships, and Composition/Aggregation for "Has-A"?
3. **Coordinated State**:
   Are multi-object transitions (e.g. borrowing a book, transferring money) encapsulated inside a single coordinator method?
4. **Clean Return Values**:
   Do your methods return values (`bool`, numbers, formatted strings) rather than merely printing to the console?
5. **Pythonic Quality**:
   Are you using descriptive class and method names adhering to PEP 8, with `__repr__` or `__str__` defined for human-friendly inspection?

---

## Ready to Build!
Open **[problems.md](problems.md)** and embark on your capstone projects!
